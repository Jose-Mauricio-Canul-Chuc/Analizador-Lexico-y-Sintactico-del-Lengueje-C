#Analizador lexico para c++

# Integrantes
#Jose Ricardo May Estrella
#Jose Mauricio Canul Chuc
#Marco Antonio Tuz Pech

import ply.lex as lex
from ply.lex import Lexer
import sys

# lista de tokens
tokens = (

    # Palabras Reservadas
    'INCLUDE',
    'USING',
    'NAMESPACE',
    'STD',
    'COUT',
    'CIN',
    'GET',
    'ENDL',
    'ELSE',
    'IF',
    'INT',
    'STRING',
    'RETURN',
    'VOID',
    'WHILE',
    'FOR',

    # Symbolos
    'HASH',
    'POINT',
    'PLUS',
    'PLUSPLUS',
    'MINUS',
    'MINUSMINUS',
    'TIMES',
    'DIVIDE',
    'LESS',
    'LESSEQUAL',
    'GREATER',
    'GREATEREQUAL',
    'EQUAL',
    'DEQUAL',
    'DISTINT',
    'SEMICOLON',
    'COMMA',
    'LGREATER',
    'RGREATER',
    'LPAREN',
    'RPAREN',
    'LBRACKET',
    'RBRACKET',
    'LBLOCK',
    'RBLOCK',
    'QUOTES',


    #Otros
    'ID',
    'NUMBER',
)


# Reglas de Expresiones Regualres para token de Contexto simple

t_PLUS = r'\+'
t_MINUS = r'-'
t_MINUSMINUS = r'\-\-'
t_POINT = r'\.'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_EQUAL = r'='
t_LESS = r'<'
t_GREATER = r'>'
t_SEMICOLON = ';'
t_COMMA = r','
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_LBLOCK = r'{'
t_RBLOCK = r'}'
t_QUOTES = r'\"'


def t_INCLUDE(t):
    r'include'
    return t


def t_USING(t):
    r'using'
    return t


def t_NAMESPACE(t):
    r'namespace'
    return t


def t_STD(t):
    r'std'
    return t


def t_COUT(t):
    r'cout'
    return t


def t_CIN(t):
    r'cin'
    return t


def t_GET(t):
    r'get'
    return t


def t_ENDL(t):
    r'endl'
    return t


def t_ELSE(t):
    r'else'
    return t


def t_IF(t):
    r'if'
    return t


def t_INT(t):
    r'int'
    return t


def t_RETURN(t):
    r'return'
    return t


def t_VOID(t):
    r'void'
    return t


def t_WHILE(t):
    r'while'
    return t


def t_FOR(t):
    r'for'
    return t


def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

#exprecion regular para reconocer los identificadores


def t_ID(t):
    r'\w+(_\d\w)*'
    return t


def t_STRING(t):
#expresion RE para reconocer los String
    r'\"?(\w+ \ *\w*\d* \ *)\"?'
    return t


def t_HASH(t):
    r'\#'
    return t


def t_PLUSPLUS(t):
    r'\+\+'
    return t


def t_LESSEQUAL(t):
    r'<='
    return t


def t_GREATEREQUAL(t):
    r'>='
    return t


def t_DEQUAL(t):
    r'=='
    return t


def t_LGREATER(t):
    r'<<'
    return t


def t_RGREATER(t):
    r'>>'
    return t


def t_DISTINT(t):
    r'!='
    return t


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

t_ignore = ' \t'


def t_comments(t):
    r'/\*(.|\n)*?\*/'
    t.lexer.lineno += t.value.count('\n')


def t_comments_C99(t):
    r'//(.)*?\n'
    t.lexer.lineno += 1

def t_error(t):
    t.type = t.value[0]
    t.value = t.value[0]
    t.lexer.skip(1)
    return t

def test(data, lexer):
    lexer.input(data)
    i = 1  # Representa la línea
    while True:
        tok = lexer.token()
        if not tok:
            break
        print("\t" + str(i) + " - " + "Linea: " + str(tok.lineno) + "\t" + str(tok.type) + "\t -->  " + str(tok.value))
        i += 1
    # print(tok)


lexer: Lexer = lex.lex()

if __name__ == '__main__':
    if (len(sys.argv) > 1):
        fin = sys.argv[1]
    else:
        fin = 'index.txt'
    f = open(fin, 'r')
    data = f.read()
    #print (data)
    # lexer.input(data)
    test(data, lexer)
