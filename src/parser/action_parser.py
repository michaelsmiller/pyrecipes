from typing import Tuple, Sequence
from parser.cooking_types import Action, Condition, Tool, Container, Ingredient, Expression

import re

# verb(arg1=expr, arg2=expr, arg3=expr, ...)

name_number_regex = re.compile(r"^([a-z][a-z_]*)(\d*)$")

# TODO: fill these out
def parse_ingredient(s : str | Sequence[str]) -> Ingredient:
    # TODO: amounts as well, need default amounts to work
    if isinstance(s, list):
        return [parse_ingredient(x) for x in s]
    return Ingredient(s.lower())

def parse_tool(s : str) -> Tool:
    if isinstance(s, list):
        return [parse_tool(x) for x in s]
    s = s.lower()
    m = re.match(name_number_regex, s)
    tool = Tool(m.group(1))
    if len(num := m.group(2)) > 0:
        tool.number = int(num)
    return tool

def parse_container(s : str) -> Container:
    if isinstance(s, list):
        return [parse_container(x) for x in s]
    s = s.lower()
    m = re.match(name_number_regex, s)
    container = Container(m.group(1))
    if len(num := m.group(2)) > 0:
        container.number = int(num)
    return container

def parse_until(s : str) -> Condition:
    if isinstance(s, list):
        return [parse_until(x) for x in s]
    return None

def parse_action(line : str) -> Action:
    # 1. parse into IR of verb, (key1, val1), (key2, val2), ..., all are strings
    assert line.count("(") == line.count(")")
    assert line.count("(") > 0

    print(line)

    pstart = line.find("(")
    pend = line.rfind(")")
    verb = line[:pstart].strip()
    print(" ", verb)

    def parse_arg(arg : str) -> Tuple[str, Sequence[str]]:
        arg = arg.strip()
        print(arg)
        assert arg.count("=") == 1
        keyval = tuple([s.strip() for s in arg.split("=")])
        assert(len(keyval) == 2)
        key, val = keyval
        assert val[0] == "[" or "[" not in val
        if val[0] == "[":
            assert val[-1] == "]"
            val = val[1:-1]
            return key, [s.strip() for s in val.split(",")]
        else:
            return key, [val]

        return keyval

    line = line[pstart+1:pend].strip()
    args = []
    pcount, pstart = 0, 0
    bcount = 0
    for i in range(len(line)):
        c = line[i]
        if pcount == 0 and c == "," and bcount == 0:
            args.append(parse_arg(line[pstart:i]))
            pstart = i+1
        elif c == "(":
            pcount += 1
        elif c == ")":
            pcount -= 1
        elif c == "[":
            bcount += 1
        elif c == "]":
            bcount -= 1

    if len(arg := line[pstart:]) > 0:
        args.append(parse_arg(arg))


    a = Action(verb)
    for key, value in args:
        assert arg.count("=") == 1
        # key, value = [s.strip() for s in arg.split("=")]
        print(" ", key, "=", value)
        key = key.lower()
        match key:
            case "ingredient":
                a.ingredient = parse_ingredient(value)
            case "container":
                a.container = parse_container(value)
            case "tool":
                a.tool = parse_tool(value)
            case "until":
                a.until = parse_until(value)

    # 2. Create the Action object and populate corresponding entries
    return None
