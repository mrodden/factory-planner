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

from typing import List


registry = {}


class Recipe:
    def __init__(self, name: str, time: int, outputs: List, inputs: List, factory: str):
        self.name = name
        self.time = time
        self.outputs = outputs
        self.inputs = inputs
        self.factory = factory

        if self.name in registry:
            raise ValueError("Recipe with name='%s' already registered" % self.name)

        registry[self.name] = self

    def __repr__(self):
        return "<%s(name='%s')>" % (self.__class__.__name__, self.name)


Recipe(
    "purplematrix",
    time=10,
    outputs=[("purplematrix", 1)],
    inputs=[("processor", 2), ("broadband", 1)],
    factory="lab",
)

Recipe(
    "processor",
    time=3,
    outputs=[("processor", 1)],
    inputs=[("circuit", 2), ("component", 2)],
    factory="assembler",
)

Recipe(
    "circuit",
    time=1,
    outputs=[("circuit", 2)],
    inputs=[("iron", 2), ("copper", 1)],
    factory="assembler",
)

Recipe(
    "component",
    time=2,
    outputs=[("component", 1)],
    inputs=[("silicon", 2), ("copper", 1)],
    factory="assembler",
)

Recipe(
    "broadband",
    time=8,
    outputs=[("broadband", 1)],
    inputs=[("nanotube", 2), ("silicon-crystal", 2), ("plastic", 1)],
    factory="assembler",
)

Recipe(
    "nanotube",
    time=4,
    outputs=[("nanotube", 2)],
    inputs=[("graphene", 3), ("titanium", 1)],
    factory="chemlab",
)

Recipe(
    "graphene",
    time=3,
    outputs=[("graphene", 2)],
    inputs=[("graphite", 3), ("sulfuric-acid", 1)],
    factory="chemlab",
)

Recipe(
    "graphite",
    time=2,
    outputs=[("graphite", 1)],
    inputs=[("coal", 2)],
    factory="smelter",
)

Recipe(
    "sulfuric-acid",
    time=6,
    outputs=[("sulfuric-acid", 4)],
    inputs=[("oil", 6), ("stone", 8), ("water", 4)],
    factory="chemlab",
)

Recipe(
    "silicon-crystal",
    time=2,
    outputs=[("silicon-crystal", 1)],
    inputs=[("silicon", 1)],
    factory="smelter",
)

Recipe(
    "plastic",
    time=3,
    outputs=[("plastic", 1)],
    inputs=[("oil", 2), ("graphite", 1)],
    factory="chemlab",
)
