# factory-planner

A basic but flexible tool/framework that handles the math behind creating production pipelines with as few bottlenecks as possible.

I created and use this tool while building large factory blocks in Dyson Sphere Program, but the Domain Specific Language for defining recipes and requesting a new production chain can be used for almost any production chain type system.

## usage

A quick sample for creating a production line for about 80 purple matrix science per minute.

Contents of `example.py`
```
import solve

totals = {}
t = solve.Request("purplematrix", 1.33).resolve(totals)

print("Deficits: %s" % totals)
print(str(t))
```

Use python3.x to run the script.
```
$ python3 example.py
No recipe found for item='iron'
No recipe found for item='copper'
No recipe found for item='silicon'
No recipe found for item='copper'
No recipe found for item='coal'
No recipe found for item='oil'
No recipe found for item='stone'
No recipe found for item='water'
No recipe found for item='titanium'
No recipe found for item='silicon'
No recipe found for item='oil'
No recipe found for item='coal'
Deficits: {'iron': -6.0, 'copper': -9.0, 'silicon': -15.0, 'coal': -18.0, 'oil': -7.333333333333334, 'stone': -5.333333333333333, 'water': -2.6666666666666665, 'titanium': -1.5}
14 lab (1.4 purplematrix/s, -2.8 processor/s, -1.4 broadband/s)
  9 assembler (3 processor/s, -6 circuit/s, -6 component/s)
    3 assembler (6 circuit/s, -6 iron/s, -3 copper/s)
    12 assembler (6 component/s, -12 silicon/s, -6 copper/s)
  12 assembler (1.5 broadband/s, -3 nanotube/s, -3 silicon-crystal/s, -1.5 plastic/s)
    6 chemlab (3 nanotube/s, -4.5 graphene/s, -1.5 titanium/s)
      7 chemlab (4.667 graphene/s, -7 graphite/s, -2.333 sulfuric-acid/s)
        14 smelter (7 graphite/s, -14 coal/s)
        4 chemlab (2.667 sulfuric-acid/s, -4 oil/s, -5.333 stone/s, -2.667 water/s)
    6 smelter (3 silicon-crystal/s, -3 silicon/s)
    5 chemlab (1.667 plastic/s, -3.333 oil/s, -1.667 graphite/s)
      4 smelter (2 graphite/s, -4 coal/s)
```
