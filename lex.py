from helper import *

def lex_string(string):
    """
    Check is the first character is a quote.
    Remove the initial quote.
    Return None if there is no initial quote.
    """
    json_string = ''
    if string[0] == json_quote:
        string = string[1:]
    else:
        return None, string
    
    """
    Iterate over the string till the ending quote
    Found the ending quote, return the lexed string and the rest
    """
    for i in string:
        if i == json_quote:
            return json_string, string[len(json_string)+1:]
        else:
            json_string += i
    
    raise Exception('Expected end-of-string quote')


def lex_number(string):
    json_number = ''

    # Set valid characters for a number
    number_characters = [str(i) for i in range(0,10)] + ['-', 'e', '.']

    """
    Iterate over the string.
    Accumulate number characters.
    Stop when a non-number character is found
    """
    for i in string:
        if i in number_characters:
            json_number += i
        else:
            break

    # Remaining part of the string
    rest = string[len(json_number):]

    # Check if no number was found
    if not len(json_number):
        return None, string
    
    # Return the number as float or int
    if '.' in json_number:
        return float(json_number), rest
    
    return int(json_number), rest


def lex_true_false(string):
    string_length = len(string)
    """
    Check if the length of the string is at least as long as length of 'true'.
    Check if the beginning of the string matches 'true'.
    If both matches, return 'True' and the rest of the string.
    Else if not true, then do the same for false.
    """
    if string_length >= true_length and string[:true_length] == 'true':
        return True, string[true_length:]
    elif string_length >= false_length and string[:false_length] == 'false':
        return False, string[false_length:]
    
    # Return None and the string if neither true or false.
    return None, string


def lex_null(string):
    string_length = len(string)
    """
    Check if the length of the string is at least as long as length of 'null'.
    Check if the beginning of the string matches 'null'.
    If both matches, return 'True' and the rest of the string.
    """
    if string_length >= null_length and string[:null_length] == 'null':
        return True, string[null_length:]
    
    # Return None if the string is not null
    return None, string


def lex(string):
    # List of tokens
    array = []

    while len(string):
        # Lexing a string
        json_string, string = lex_string(string)
        if json_string is not None:
            array.append(json_string)
            continue

        # Lexing a boolen
        json_bool, string = lex_true_false(string)
        if json_bool is not None:
            array.append(json_bool)
            continue

        # Lexing a null
        json_null, string = lex_null(string)
        if json_null is not None:
            array.append(None)
            continue

        # Lexing a number
        json_number, string = lex_number(string)
        if json_number is not None:
            array.append(json_number)
            continue

        """
        Find whitespace characters and skip them
        Check for syntax charcaters and add them as tokens to the array
        """
        s = string[0]
        if s in json_ignore:
            string = string[1:]
        elif s in json_syntax:
            array.append(s)
            string = string[1:]
        # Raise an exception for unexpected characters
        else:
            raise Exception('Unexpected character: {}'.format(string[0]))
        
    return array


print(lex_string("hello"))
print(lex_number("-123.45abc"))
print(lex_true_false("trueabc"))
print(lex_null("nullxyz"))
print(lex('{"foo": [1, 2, {"bar": 2}]}'))
