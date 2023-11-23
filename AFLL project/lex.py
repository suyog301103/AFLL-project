import ply.lex as lex
import re

tokens = [
    'NUMBER',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'LPAREN',
    'RPAREN',
    'LSQUARE',
    'RSQUARE',
    'ID',
    'EQUAL',
    'POINT',
    'COLON',
    'COMMA',
    'CONDITIONAL',
    'STRING',
    'INDENT',
    'DEDENT',
    'IF',
    'ELSE',
    'WHILE',
    'ELIF',
    'FOR',
    'CLASS',
    'INIT',
    'range',
    'in',
]

reserved = {
    'if': 'IF',
    'else': 'ELSE',
    'while': 'WHILE',
    'elif': 'ELIF',
    'for': 'FOR',
    'range': 'range',
    'in': 'in',
    'class': 'CLASS',
    '__init__': 'INIT',
    'INDENT' : 'INDENT',
    'DEDENT' : 'DEDENT',
    'def' : 'DEF',
    'self' : 'SELF',
}

t_EQUAL = r'\='
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LSQUARE = r'\['
t_RSQUARE = r'\]'
t_COLON = r'\:'
t_COMMA = r'\,'
t_POINT = r'\.'
t_CONDITIONAL = r'\>|<|<=|>=|=='
t_STRING = r'\"[a-zA-Z_0-9]*\"'
t_INDENT = r'INDENT'
t_DEDENT = r'DEDENT'

tokens = tokens + list(reserved.values())


def preprocess(data):
    lines = data.split('\n')
    processed_lines = []

    current_indent = 0
    for line in lines:
        line = line.rstrip()  # Remove trailing spaces

        if line:  # Ignore empty lines
            indent = len(re.match(r'^\s*', line).group(0))  # Calculate leading spaces

            while current_indent < indent:
                processed_lines.append('INDENT')
                current_indent += 4  # Assuming 4 spaces per indent level

            while current_indent > indent:
                processed_lines.append('DEDENT')
                current_indent -= 4  # Assuming 4 spaces per indent level

            processed_lines.append(line.lstrip())  # Add stripped line content

    # Add DEDENT tokens for any remaining indentation levels
    while current_indent > 0:
        processed_lines.append('DEDENT')
        current_indent -= 4  # Assuming 4 spaces per indent level

    processed_data = '\n'.join(processed_lines)
    return processed_data


t_ignore = ' '


def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'ID')
    return t


def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)


lexer = lex.lex()

# Sample input for testing
data = '''
else: 
    a
'''

# Preprocess the input to introduce INDENT and DEDENT tokens
processed_data = preprocess(data)
print(processed_data)
# Give the lexer some input
lexer.input(processed_data)
# Tokenize
while True:
    tok = lexer.token()
    if not tok:
        break  # No more input
    print(tok)
