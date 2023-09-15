import re


# Function to validate snake-case-with-dashes
def is_snake_case_with_dashes(name):
    return bool(re.match(r"^[a-z][a-z0-9]*(-[a-z0-9]+)*$", name))
