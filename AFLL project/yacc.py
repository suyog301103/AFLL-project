import ply.yacc as yacc
from lex import tokens
import re

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



def p_statement(p):
    '''statement : assign
    statement : statement statement
    statement : if
    statement : elif
    statement : else
    statement : for
    statement : in
    statement : range
    statement : expression
                | check
                | while
                | def
'''
    
def p_check(p):
    'check : INDENT statement'

# Python 
def p_assign(p):
    '''assign : ID EQUAL expression 
    | ID EQUAL MINUS expression
    | ID EQUAL MINUS expression POINT expression
    | ID EQUAL PLUS expression POINT expression'''

def p_if(p):
    '''if : IF LPAREN expression CONDITIONAL expression RPAREN COLON INDENT statement DEDENT
          | IF expression CONDITIONAL expression COLON INDENT statement DEDENT
          | IF expression COLON INDENT statement DEDENT'''

def p_elif(p):
    '''elif : ELIF LPAREN expression CONDITIONAL expression RPAREN COLON INDENT statement DEDENT
            | ELIF expression CONDITIONAL COLON INDENT statement DEDENT
            | ELIF expression COLON INDENT statement DEDENT'''

def p_for(p):
    '''for : FOR expression in range LPAREN expression RPAREN COLON INDENT statement DEDENT
           | FOR expression in expression COLON INDENT statement DEDENT'''

def p_else(p):
    'else : ELSE COLON INDENT statement DEDENT'

def p_while(p):
    '''while : WHILE LPAREN expression CONDITIONAL expression RPAREN COLON INDENT statement DEDENT
            | WHILE expression CONDITIONAL COLON INDENT statement DEDENT
            | WHILE expression COLON INDENT statement DEDENT '''
    
def p_func(p):
    '''def : DEF ID LPAREN params RPAREN COLON INDENT statement DEDENT
    '''

def p_params(p):
    '''params : ID
              | params COMMA ID
    '''

def p_expression_list(p):
    '''expression : list_declaration
                  | list_addition'''

def p_list_declaration(p):
    '''list_declaration : LSQUARE RSQUARE
                        | LSQUARE elements RSQUARE'''

def p_elements(p):
    '''elements : expression
                | elements COMMA expression'''

def p_list_addition(p):
    '''list_addition : expression LSQUARE expression RSQUARE'''
    
def p_string(p):
    'expression : STRING'

def p_id(p):
    'expression : ID'

def p_expression_plus(p):
    'expression : expression PLUS term'

def p_expression_minus(p):
    'expression : expression MINUS term'

def p_expression_term(p):
    'expression : term'

def p_term_times(p):
    'term : term TIMES factor'

def p_term_div(p):
    'term : term DIVIDE factor'

def p_term_factor(p):
    'term : factor'

def p_factor_num(p):
    'factor : NUMBER'

def p_factor_expr(p):
    'factor : LPAREN expression RPAREN'

def p_error(p):
    print("Syntax error in input!",p.value,p.lineno)


parser = yacc.yacc()

# Multiline input handling
input_lines = []
print("Enter your code (press Enter on an empty line to finish):")

while True:
    line = input()

    if not line.strip():
        break

    input_lines.append(line)

# Join the input lines into a single string
multiline_input = '\n'.join(input_lines)
multiline_input = preprocess(multiline_input)

# Parse the multiline input
result = parser.parse(multiline_input)
print(result)