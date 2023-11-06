import ply.lex as lex

tokens = [
   'NUMBER',
   'PLUS',
   'MINUS',
   'TIMES',
   'DIVIDE',
   'LPAREN',
   'RPAREN',
   'ID',
   'EQUAL',
   'DOLLAR',
   'POINT',
   'COLON',
   'CONDITIONAL',
#    'SQUOTE',
#    'DQUOTE',
   'SEMICOLON',
   'STRING',
]

reserved = {
   'if': 'IF',
   'then': 'THEN',
   'else': 'ELSE',
   'while': 'WHILE',
   'elif' : 'ELIF',
   'def' : 'DEF',
}


t_EQUAL = r'\='
t_DOLLAR = r'\$'
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_COLON = r'\:'
# t_SQUOTE = r'\''
# t_DQUOTE = r'\"'
t_SEMICOLON = r';'
t_POINT = r'\.'
t_CONDITIONAL=r'\>|<|<=|>=|=='



tokens = tokens + list(reserved.values())


def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


t_ignore = ' \t'


def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'ID')
    return t


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)
data='''"hi"=="hi"'''
lexer = lex.lex()
# Give the lexer some input
lexer.input(data)


# Tokenize
while True:
    tok = lexer.token()
    if not tok: 
        break      # No more input
    # print(tok.type, tok.value, tok.lineno, tok.lexpos)
    print(tok)

