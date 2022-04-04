from parser.cooking_types import Action

# Templates should take in (verb, ingredient, container, tool, until)
#   0 = verb
#   1 = ingredient
#   2 = container
#   3 = tool
#   4 = until_condition

verb_template1 = "{0} {1} to {2}" # verb, ingredient, container
verb_template2 = "{0} {2}"        # verb, container
verb_template3 = "{0} {1}"        # verb, ingredient

# with clause

with_template1 = "with {3}"


# until clause

until_template1 = "until {4}"



# Action template maps

verb_map = {
    "add"  : verb_template1,
    "mix"  : verb_template2,
    "shape": verb_template3,
}

def format_action(a : Action) -> str:
    assert a.name is not None
    assert a.ingredient is not None or a.container is not None
    format_tuple = (a.name, a.ingredient.name, a.container.name, a.tool.name, str(a.until))

    clauses = []
    clauses.append(verb_map[a.name].format(*format_tuple))
    if a.tool is not None:
        clauses.append(with_template1.format(*format_tuple))
    if a.until is not None:
        clauses.append(until_template1.format(*format_tuple))
    return " ".join(clauses)


