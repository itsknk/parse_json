from .lex import lex
from .parse import parse

# Conver json-like string into python object
"""
Tokenize input string into list of tokens using lexer.
Parse the tokens into structured python object. is_root = True indicates that the parsing  starts at root level.
[0] returns the first element of the parsed result.
"""
def str_to_pyo(string):
    tokens = lex(string)
    return parse(tokens, is_root=True)[0]

# Convert python object back into corresponding json-like string.
"""
Check the type of the json:
Dictionary - construct a json object string '{}' by iterating over the items, recursively calling to_string.
List - construct a json array string '[]' by iterating over its elements, recursively calling to_string.
String - Enclose json in double quotes '"'.
Boolean - Return 'true' if json is true, otherwise 'false'.
None - Returns 'null'
Other - converts json to a string representation using str().
"""
def to_string(json):
    json_type = type(json)
    if json_type is dict:
        string = '{'
        dict_len = len(json)

        for i, (key, val) in enumerate(json.items()):
            string += '"{}": {}'.format(key, to_string(val))

            if i < dict_len-1:
                string += ', '
            else:
                string += '}'
        
        return string
    elif json_type is list:
        string = '['
        list_len = len(json)

        for i, val in enumerate(json):
            string += to_string(val)

            if i < list_len-1:
                string += ', '
            else:
                string += ']'
            
            return string
    elif json_type is str:
        return '"{}"'.format(json)
    elif json_type is bool:
        return 'true' if json else 'false'
    elif json_type is None:
        return 'null'
    
    return str(json)
