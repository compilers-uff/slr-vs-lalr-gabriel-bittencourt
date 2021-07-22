tokens = ('EQUALS', 'TIMES', 'ID')

t_TIMES = r'\*'
t_EQUALS = r'='
t_ID = r'id'

t_ignore = ' \t'


def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")


# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


# Build the lexer
import ply.lex as lex

lexer = lex.lex()

'''
S : L = R
  | R
 
L : * R
  | id

R : L
'''

def p_expression_S(p):
    ''' 
        S : L EQUALS R
          | R
    '''


def p_expression_L(p):
    ''' 
        L : TIMES R
          | ID
    '''


def p_expression_R(p):
    ''' 
        R : L
    '''


def p_error(p):
    print("Syntax error at '%s'" % p.value)


import ply.yacc as yacc

parser = yacc.yacc(method="LALR")
# parser = yacc.yacc(method="SLR")

while True:
    try:
        s = input('calc >')
    except EOFError:
        break
    parser.parse(s)
