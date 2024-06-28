JSON_QUOTE = '"'

def lex_string(string):
    """
    Check is the first character is a quote.
    Remove the initial quote.
    Return None if there is no initial quote.
    """
    json_string = ''
    if string[0] == JSON_QUOTE:
        string = string[1:]
    else:
        return None, string
    
    """
    Iterate over the string till the ending quote
    Found the ending quote, return the lexed string and the rest
    """
    for i in string:
        if i == JSON_QUOTE:
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
    """
    Check if the length of the string is at least as long as length of 'true'.
    Check if the beginning of the string matches 'true'.
    If both matches, return 'True' and the rest of the string.
    Else if not true, then do the same for false.
    """
    if len(string) >= len('true') and string[:len('true')] == 'true':
        return True, string[len('true'):]
    elif len(string) >= len('false') and string[:len('false')] == 'false':
        return False, string[len('false'):]
    
    # Return None and the string if neither true or false.
    return None, string


def lex_null(string):
    """
    Check if the length of the string is at least as long as length of 'null'.
    Check if the beginning of the string matches 'null'.
    If both matches, return 'True' and the rest of the string.
    """
    if len(string) >= len('null') and string[:len('null')] == 'null':
        return True, string[len('null'):]
    
    # Return None if the string is not null
    return None, string


print(lex_string("hello"))
print(lex_number("-123.45abc"))
print(lex_true_false("trueabc"))
print(lex_null("nullxyz"))
