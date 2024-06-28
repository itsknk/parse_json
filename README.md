## parse_json
A simple json parser written in python.


### Overview

This project provides a simple JSON parser implemented in Python. It includes functionality to parse a JSON-like string into a Python object and convert a Python object back into a JSON-like string.

### Directory Structure

```
parse_json/
├── __init__.py
├── helper.py
├── lex.py
└── parse.py
```

### Installation

To use this JSON parser, you can clone this repository:

```bash
git clone <this repo>
```

Then, navigate to the project directory:

```bash
cd parse_json
```

### Usage

#### Converting JSON-like String to Python Object

You can convert a JSON-like string to a Python object using the `str_to_pyo` function:

```python
from parse_json import str_to_pyo

json_string = '{"foo": [1, 2, {"bar": 2}]}'
python_obj = str_to_pyo(json_string)
print(python_obj)
# Output: {'foo': [1, 2, {'bar': 2}]}
```

#### Converting Python Object to JSON-like String

You can convert a Python object back to a JSON-like string using the `to_string` function:

```python
from parse_json import to_string

python_obj = {'foo': [1, 2, {'bar': 2}]}
json_string = to_string(python_obj)
print(json_string)
# Output: {"foo": [1, 2, {"bar": 2}]}
```

### Code Explanation

#### `__init__.py`

- Contains the main interface functions `str_to_pyo` and `to_string`.
- `str_to_pyo` converts a JSON-like string to a Python object.
- `to_string` converts a Python object back to a JSON-like string.

#### `helper.py`

- Contains constants and helper variables used throughout the lexer and parser.

#### `lex.py`

- Implements the lexer which converts a JSON-like string into tokens.
- Functions include `lex_string`, `lex_number`, `lex_true_false`, `lex_null`, and `lex`.

#### `parse.py`

- Implements the parser which converts tokens into a structured Python object.
- Functions include `objects_parse`, `array_parse`, and `parse`.

### To Do

- Write unit tests.

### Motivation
John Crickett's coding challenge. [Challenge 2](https://codingchallenges.fyi/challenges/challenge-json-parser/) involves writing a JSON Parser.

