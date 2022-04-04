from dataclasses import dataclass
from typing import Any, Sequence, Dict
# TODO: replace dataclasses with the parser thing (pygment?)

class CookingObject:
    pass

Expression = Sequence[CookingObject] | CookingObject

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
    comparison : Any = None

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
    steps       : Sequence[Action]
    stipulation : Condition | None = None

@dataclass
class Recipe:
    ingredients          : Sequence[Ingredient]
    implicit_ingredients : Sequence[Ingredient]
    tools                : Sequence[Tool]
    containers           : Sequence[Container]
    steps                : Sequence[Action]
    header               : Dict[str, str]



##########################################

# TODO: database for tools, containers
