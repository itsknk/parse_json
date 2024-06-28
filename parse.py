from .helper import *

# Parse a json object into a python dictionary.
"""
Check if the first element is Right Brace }, if yes, then return empty dictionary and rest.
Continue to parse key-value pairs. The key must be a string.
After parsing the key, next token must be colon. If not, raise exception.
Value is parsed using parse function, and key-value pair is added to the dictionary.
If right brace reached, it's the end of the object. Return json_object and the rest.
If no comma between key-value pairs, raise exception.
If found comma, continue parsing the next key-value pair.
"""
def objects_parse(tokens):
    json_objects = {}
    i = tokens[0]
    if i == json_syntax[3]:
        return json_objects, tokens[1:]
    
    while True:
        json_key = tokens[0]
        if type(json_key) is str:
            tokens = tokens[1:]
        else:
            raise Exception('Expecyed string key, got  {}'.format(json_key))
        
        if tokens[0] != json_syntax[0]:
            raise Exception('Expected colon after key')
        
        json_value, tokens = parse(tokens[1:])
        json_objects[json_key] = json_value

        i = tokens[0]
        if i == json_syntax[3]:
            return json_objects, tokens[1:]
        elif i != json_syntax[1]:
            raise Exception('Expected comma after pair in object')
        tokens = tokens[1:]
    # If the loop exits without finding the right brace
    raise Exception('Expected end-of-the-object brace')


# Parse a json array into a python list.
"""
Check if the first element is Right Bracket ], if yes, then return empty list and rest.
Continue to parse tokens and append the parsed ones
If right bracket ] is reached, it means end of the array, return the json_array and rest.
If no comma between array elements, raise excpetion.
If comma found, continue parsing.
"""
def array_parse(tokens):
    json_array = []
    i = tokens[0]
    if i == json_syntax[5]:
        return json_array, tokens[1:]
    
    while True:
        json, tokens = parse(tokens)
        json_array.append(json)

        i = tokens[0]
        if i == json_syntax[5]:
            return json_array, tokens[1:]
        elif i != json_syntax[1]:
            raise Exception('Expected comma in between array elements')
        tokens = tokens[1:]
    # If the loop exits without finding the right bracket
    raise Exception('Expected end-of-array')


# Delegate parsing to the function based on the type of the current token.
"""
If the first token is a left bracket then call the array_parse function
Else if it is a left brace then call the objects_parse function
"""
def parse(tokens, is_root=False):
    i = tokens[0]

    if is_root and i!= json_syntax[2]:
        raise Exception('Root must be an object')

    if i == json_syntax[4]:
        return array_parse(tokens[1:])
    elif i == json_syntax[2]:
        return objects_parse(tokens[1:])
    else:
        return i, tokens[1:]
    