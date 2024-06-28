from helper import *

# Parse a json object into a python dictionary.
def objects_parse(tokens):
    return {}, tokens

# Parse a json array into a python list.
def array_parse(tokens):
    return [], tokens

# Delegate parsing to the function based on the type of the current token.
def parse(tokens):
    i = tokens[0]

    if i == json_syntax[4]:
        return array_parse(tokens[1:])
    elif i == json_syntax[2]:
        return objects_parse(tokens[1:])
    else:
        return i, tokens[1:]
    
