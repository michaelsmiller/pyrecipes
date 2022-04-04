#!/usr/bin/env python

import re

from parser.cooking_types import Condition, Action, Tool, Ingredient, Amount, Unit, Recipe
from parser.templates     import format_action
from parser.action_parser import parse_action

# TODO: allow multiline descriptions
header_regex = re.compile(r"^(\w+)\s*:\s*(.*)$")

def parse_recipe(filename : str) -> Recipe:
    with open(filename) as f:
        lines = f.readlines()

    # Filter out comments and whitespace
    lines = [s for line in lines if len(s := line.strip()) > 0 and not (len(s) >= 2 and s[:2] == "//")]

    if len(lines) == 0:
        print("Recipe is empty!")
        return None

    ingredients = []
    implicit_ingredients = []
    tools = []
    containers = []
    steps = []
    header = {}

    # Populate header data
    while (m := re.match(header_regex, lines[0])) is not None:
        key, value = m.groups()
        assert key not in header # TODO logic of numbering redundant keys
        header[key] = value
        lines.remove(lines[0])

    # Action sequence
    # TODO: Action parser
    for line in lines:
        action = parse_action(line)

    recipe = Recipe(ingredients=ingredients, implicit_ingredients=implicit_ingredients, tools=tools, containers=containers, steps=steps, header=header)
    return recipe

def pprint(recipe : Recipe):
    # Header
    for key in recipe.header:
        print(f"{key.capitalize()}: {recipe.header[key]}")

    # TODO: print steps correctly as well

if __name__ == "__main__":
    recipe = parse_recipe("recipes/example.rec")
    pprint(recipe)
