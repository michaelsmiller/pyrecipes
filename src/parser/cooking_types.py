from dataclasses import dataclass
from typing import Any
# TODO: replace dataclasses with the parser thing (pydantic is made for parsing)

class CookingObject:
    pass

Expression = list[CookingObject] | CookingObject

# internal representation of parser, not in data format
@dataclass
class Unit:
    name      : str
    dimension : str

@dataclass
class Amount:
    number : float
    unit   : Unit

@dataclass
class Ingredient:
    name   : str
    amount : Amount = None
    # TODO: number here too?

@dataclass
class Container(CookingObject):
    name   : str
    volume : Amount = None # TODO: default volume
    number : int = None

@dataclass
class Tool:
    name : str
    number : int = None

@dataclass
class Condition:
    name       : str
    obj        : CookingObject
    comparison : Any = None # TODO: figure out typing here

@dataclass
class Action:
    name       : str
    ingredient : Ingredient | None = None
    container  : Container  | None = None
    tool       : Tool       | None = None
    until      : Condition  | None = None
    # needs to only be one that involves container and ingredients

@dataclass
class Block:
    steps       : list[Action]
    stipulation : Condition | None = None

@dataclass
class Recipe:
    ingredients          : list[Ingredient]
    implicit_ingredients : list[Ingredient]
    tools                : list[Tool]
    containers           : list[Container]
    steps                : list[Action]
    header               : dict[str, str]



##########################################

# TODO: database for tools, containers
