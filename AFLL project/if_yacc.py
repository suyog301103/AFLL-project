import ply.yacc as yacc
from if_lex import tokens

def p_statement(p):
    '''statement : assign
    statement : statement statement
    statement : if
    statement : elif
    statement : else'''

# perl
def p_assign(p):
    '''assign : DOLLAR ID EQUAL expression SEMICOLON 
    | DOLLAR ID EQUAL MINUS expression SEMICOLON
    | DOLLAR ID EQUAL PLUS expression SEMICOLON'''
    # 'assign : DOLLAR ID EQUAL expression SEMICOLON'
    # print(p[4])


# Python 
def p_assign(p):
    '''assign : ID EQUAL expression 
    | ID EQUAL MINUS expression POINT expression
    | ID EQUAL PLUS expression POINT expression'''
    # 'assign : DOLLAR ID EQUAL expression SEMICOLON'
    # print(p[4])

def p_if(p):
    'if : IF LPAREN expression CONDITIONAL expression RPAREN COLON'

def p_elif(p):
    'elif : ELIF LPAREN expression CONDITIONAL expression RPAREN COLON'

def p_else(p):
    'else : ELSE COLON'

def p_string(p):
    'expression : STRING'

def p_expression_plus(p):
    'expression : expression PLUS term'
    p[0] = p[1] + p[3]

def p_expression_minus(p):
    'expression : expression MINUS term'
    p[0] = p[1] - p[3]

def p_expression_term(p):
    'expression : term'
    p[0] = p[1]

def p_term_times(p):
    'term : term TIMES factor'
    p[0] = p[1] * p[3]

def p_term_div(p):
    'term : term DIVIDE factor'
    p[0] = p[1] / p[3]

def p_term_factor(p):
    'term : factor'
    p[0] = p[1]

def p_factor_num(p):
    'factor : NUMBER'
    p[0] = p[1]

def p_factor_expr(p):
    'factor : LPAREN expression RPAREN'
    p[0] = p[2]

def p_error(p):
    print("Syntax error in input!")

parser = yacc.yacc()

while True:
    try:
        s = input('calc > ')
    except EOFError:
        break
    if not s: continue
    result = parser.parse(s)
    print(result)