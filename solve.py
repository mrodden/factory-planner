# Copyright (C) 2021 Mathew Odden <mathewrodden@gmail.com>
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301
# USA

import io
import math
import logging

import recipes


LOG = logging.getLogger(__name__)

class Task:

    def __init__(self, recipe, amount):
        self.recipe = recipe
        self.amount = amount
        self.subtasks = []

    @property
    def amount_n(self):
        return math.ceil(self.amount)

    def __repr__(self):
        return "<Task(recipe='%s', amount=%f)>" % (self.recipe, self.amount)

    def __str__(self):
        def ftos(n):
            return ("%.3f" % n).rstrip("0").rstrip(".")

        outputs = ["%s %s/s" % (ftos(o[1] * self.amount_n / self.recipe.time), o[0]) for o in self.recipe.outputs]
        output_str = ", ".join(outputs)

        inputs = ["-%s %s/s" % (ftos(o[1] * self.amount_n / self.recipe.time), o[0]) for o in self.recipe.inputs]
        input_str = ", ".join(inputs)

        var = {
            "iter_n": self.amount_n,
            "iter": self.amount,
            "factory": self.recipe.factory,
            "outputs": output_str,
            "inputs": input_str,
        }

        buf = io.StringIO()
        this = "%(iter_n)s %(factory)s (%(outputs)s, %(inputs)s)\n" % var
        buf.write(this)
        for sub in self.subtasks:
            for line in str(sub).split("\n"):
                if line:
                    buf.write("  %s\n" % line)

        return buf.getvalue()


class Request:

    def __init__(self, item_name, amount):
        self.item_name = item_name
        self.amount = amount

    def resolve(self, totals=None):
        if totals is None:
            totals = {}

        recipe = recipes.registry.get(self.item_name)
        if not recipe:
            LOG.warning("No recipe found for item='%s'" % self.item_name)
            totals[self.item_name] = totals.get(self.item_name, 0) - self.amount
            return

        for output in recipe.outputs:
            if output[0] == self.item_name:
                output_amt = output[1]
                break

        rate = output_amt / recipe.time
        iterations = self.amount / rate

        ct = Task(recipe, iterations)

        for inp in recipe.inputs:
            amt = ct.amount_n * inp[1] / recipe.time
            t = Request(inp[0], amt).resolve(totals)
            if t:
                ct.subtasks.append(t)

        return ct


