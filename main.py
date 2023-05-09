# -----------------------------------------------------------------------------
# main.py
# Note: 
# Grammar
# terminals: caps   ----------------------------------
# non terminal: lowercase ----------------------------
# TODO: update when needed
#   <program>   : dv df dc MAIN block 
#   <dv>       : dec_vars dv
#              | empty
#   <df>       : function df
#              | empty
#   <dc>       : class dc
#              | empty
#
#
#  <statement> : assignment
#              | condition
#              | writing
#              | return
#              | loop
#              | input
#              | call
#              | arr_assign
#  
# <block>    : { bp }
#
#  <bp>        :  b
#              | empty
#
#  <b>         :  statement bp
#
#  <dec_vars>  : VAR sp
#              | VAR cp
#
#  <sp>        : simple_type spp
#
#  <spp>       : ID da sppp 
#  <sppp >     : , spp
#              | empty
# 
#  <da>        : [ CTE_INT ] db
#              | [ CTE_INT ] arr_init
#              | assignment
#              | empty
#
#  <db>        : [ CTE_Int ]
#              | [ CTE_Int ] arr_init
#              | empty
#
#  <cp>        : compound_type ID cpp
#
#  <cpp>       : , ID cpp
#              | empty
#
#   <factor>   : ( expression )
#              | fp
#              | variable
#              | call
#   
#   <fp>       : mp var_cte 
#         
#  <mp>      : +
#            | - 
#            | empty 
# 
# 
# <var_cte>   : CTE_INT  
#             | CTE_FLOAT
#             | CTE_CHAR
# 
# <input>   : ID = INPUT ( variable ) ;
#
# <call>        : ID callp 
#               | ID callpp
#
# <callp>        : ( callppp )
#
# <callppp>     : exp callpppp
#               | empty
#
# <callpppp>     : , exp callpppp
#               | empty
#
# <callpp>       : . ID 
#               | . ID q
#
# <q>           : ( qp )
#
# <qp>          : exp qpp
#               | empty
#
# <qpp>         : , exp qpp
#               | empty
#
# <assignment>   : assignmentp = expression ;
# <assignmentp> : id
#                | empty
# 
# <expression>   : exp ep
# 
#  <ep>    : epp exp  
#          | empty
#
# <epp>    : >
#          | < 
#          | <> 
#          | == 
#
#  <exp>   : term xp
# 
#   <xp>        :  + exp
#               |  - exp 
#               | empty
# 
#  <term>       : factor tp
# 
#    <tp>       : * term
#               | / term
#               |  empty
# 
#  <condition>  : IF ( expression ) block cp 
# 
#  <cp>         :  ELSE block 
#               | empty
# 
# <writing>       : print ( expression ) ;
# 
#  <variable>   : ID ap
# 
#  <ap>          :  [ exp ] bp
#               | empty
# 
#  <bp>          :  [ exp ] 
#               | empty
#
# <compund_type> : id      
#
#  <simple_type>  : INT
#                 | FLOAT
#                 | CHAR
#                 | BOOL
#
# <loop>          : FOR ID = exp TO exp DO statement ;
#
# <class>         : CLASS ID { simple_type ID ; lt function lf } ;
#
# <lt>            : simple_type ID ; lt
#                 | empty
#
# <lf>            : function lf
#                 | empty
#
# <function>      : fs ID ( fp ) dec_vars block
#
# <fs>            : simple_type
#                 | VOID
#
# <fp>            : parameter
#                 | empty
#
# <parameter>     : simple_type ID pl
#
# <pl>            : , parameter
#                 | empty
#
# <arr_init>       : = { aip }
#
# <aip>            : var_cte aipp
#                 | { var_cte aipp } aippp
#
# <aipp>            : , var_cte aipp
#                 | empty
#
# <aippp>         : , { var_cte aipp } aippp
#                 | empty
#
# <arr_assign>    : ID arr_assign1 = expression ;
# 
#  <arr_assign1>  :  [ exp ] arr_assign2
# 
#  <arr_assign2> :  [ exp ] 
#                | empty
#
# <return>        : RETURN id
#                 | RETURN expression
#
# -----------------------------------------------------------------------------

from ply.lex import lex

# --- Tokenizer

reserved = {
    'if' : 'IF',
    'else' : 'ELSE',
    'print' : 'PRINT',
    'var' : 'VAR',
    'for' : 'FOR',
    "input": "INPUT",
    "void": "VOID", # TODO: Check if this is valid. Also check null
    "class": "CLASS",
    "main": "MAIN",
    "int": "INT",
    "float": "FLOAT",
    "char": "CHAR",
    "bool": "BOOL",
    "return": "RETURN",
    "to" : "TO",
    "do" : "DO",
}

# All tokens must be named in advance.
tokens = [
    'ID', #TODO check id doesnt overwrite 

    'PLUS',
    'MINUS', 
    'TIMES', 
    'DIVIDE',

    'SEMIC',
    'COMMA',
    'DOT',
     
    'LPAREN', 
    'RPAREN',
    'LCURL', 
    'RCURL',
    'LBRACKET',
    'RBRACKET',
     
    'CTE_INT', 
    'CTE_FLOAT', 
    'CTE_CHAR',
    'CTE_BOOL',
    
    'EQUALS',
    'EQEQ',
    'GT', 
    'LT', 
    'NOTEQ',
    'LESS_OR_EQ_THAN',
    'GREATER_OR_EQ_THAN',

    'ISEQ',
    'VALUE',
    'LTEQ',
    'GTEQ',
    'PLUSEQ',
    'MINUSEQ',
    'TIMESEQ',
    'DIVEQ'
] + list(reserved.values())

# Ignored characters
t_ignore = ' \t'

# Token matching rules are written as REGEX
t_PLUS      = r'\+'
t_MINUS     = r'-'
t_TIMES     = r'\*'
t_DIVIDE    = r'/'

t_SEMIC     = r'\;'
t_COMMA     = r','
t_DOT       = r'\.'

t_LPAREN    = r'\('
t_RPAREN    = r'\)'
t_LCURL     = r'\{'
t_RCURL     = r'\}'
t_LBRACKET  = r'\['
t_RBRACKET  = r'\]'

t_CTE_INT       = r'\d+'
t_CTE_FLOAT     = r'((\d*\.\d+)(E[\+-]?\d+)?|([1-9]\d*E[\+-]?\d+))'
t_CTE_CHAR      = r'"[^"]"'
t_CTE_BOOL      = r'^(True|False)$'

t_EQUALS    = r'='
t_GT        = r'>'
t_LT        = r'<'
t_NOTEQ     = r'<>'
t_LESS_OR_EQ_THAN = r'<='
t_GREATER_OR_EQ_THAN = r'>='
t_EQEQ     = r'=='

# A function can be used if there is an associated action.
# Write the matching regex in the docstring.

# Reserved words
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value,'ID')    # Check for reserved words
    return t

#def t_FLOAT(t):
#    r'\d+'
#    t.value = float(t.value)
#    return t


# Ignored token with an action associated with it
def t_ignore_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count('\n')

# Error handler for illegal characters
def t_error(t):
    print(f'Illegal character {t.value[0]!r}')
    t.lexer.skip(1)

# Build the lexer object
lexer = lex()

# Test it out
data = f'''
float rf
if (largo >= 5)
void suma() {{
    int a , b
    a==b
    a=b
    rf==a
    char c = "r"
}}
'''

# Give the lexer some input
lexer.input(data)

# Tokenize
while True:
    tok = lexer.token()
    if not tok:
        break      # No more input
    print(tok)