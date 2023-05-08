# -----------------------------------------------------------------------------
# main.py
# Note: 
# Grammar
# terminals: caps   ----------------------------------
# non terminal: lowercase ----------------------------
#
#   <program>   : dec_variable dvp MAIN block ;
#   <dvp>   : dec_variable dvp
#              | empty
#
#  <statement> : assignment
#              | condition
#              | writing
#              | dec_funct
#              | loop
#              | dec_var
#              | input
#              | function
#              | call
#  
# <block>    : { bp }
#
#  <bp>        :  b
#              | empty
#
#  <B>         :  statement bp
#
#  <DEC_VARS>  : VAR sp
#              | VAR cp
#
#  <SP>        : simple_type ID da spp
#
#  <SPP>       : , ID da spp 
#              | empty
#
#  <DA>        : [ CTE_I ] db
#              | empty
#
#  <DB>        : [ CTE_I ]
#              | empty
#
#  <CP>        : compound_type ID cpp
#
#  <CPP>       : , ID cpp
#              | empty
#
#   <FACTOR>   : ( expression )
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
# <var_cte>   : CTE_I  
#             | CTE_F 
#             | CTE_CH
# 
# <input>   : ID = INPUT ( variable ) ;
#
# <statement>   : assignment 
#               | condition 
#               | writing
#               | dec_funct
#               | loop
#               | dec_var
#               | input
#               | function
#               | call
#
# <call>        : ID callp
#
# <callp>        : cfun
#                | cc
#
# <cfun>        : ( exp cfp )
#
# <cfp>        : , exp cfp 
#              | empty
#
# <cc>        : . ID ccp
#
# <ccp>        : ( ccpp )
#              | empty
#
# <ccpp>       : exp cl
#              | empty
#
# <cl>         : , exp cl 
#              | empty
#
# <assignment>   : = expression ;
# 
# <expression>   : exp ep
# 
#  <ep>    : epp EXP  
#          | empty
#
# <epp>    : >
#          | < 
#          | <> 
#          | == 
#
#  <exp>   : term xp
# 
#   <xp>        :  + EXP
#               |  - EXP 
#               | empty
# 
#  <term>       : factor tp
# 
#    <tp>       : * term
#               | / term
#               |  empty
# 
#  <condition>  : IF ( expression ) block cp ;
# 
#  <cp>         :  ELSE block 
#               | empty
# 
# <write>       : print ( expression ) ;
# 
#  <variable>   :  vsp
#               | VAR vcp
# 
#  <vsp>        :  simple_type ID a 
# 
#  <a>          :  [ exp ] b
#               | empty
# 
#  <b>          :  [ exp ] 
#               | empty
#
# <compund_type> : id      
#
#  <simple_type>  : INT
#                 | FLOAT
#                 | CHAR
#                 | BOOL
#
# <loop>          : FOR ( for_initial for_condition for_update ) block
#
# <for_initial>   : type ID = vi;   
#
#  <vi>           : VALUE   
#                 | ID
#
# <for_update>   : ID fu
#
# <fu>            : fua vi   
#                 | fub
#
# <fua>           : +=
#                 | -=
#                 | *=
#                 | /=
#
# <fub>           : ++
#                 | --
#
# <for_condition> : ID fc vi ;
#
# <fc>            : >
#                 | <
#                 | ==
#                 | <>
#                 | <=
#                 | >=
#
# <class>         : CLASS ID { simple_type ID ; lt function lf } ;
#
# <lt>            : simple_type ID ; lt
#                 | empty
#
# <lf>            : function lf
#                 | empty
#
# <function>      : fs ID ( fp ) block
#
# <fs>            : simple_type
#                 | void
#
# <fp>            : parameter
#                 | empty
#
# <parameter>     : simple_type ID pl
#
# <pl>            : , simple_type ID pl
#                 | empty
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
    "void": "VOID", # Check if this is valid. Also check null
    "class": "CLASS",
    "main": "MAIN",
    "int": "INT",
    "float": "FLOAT",
    "char": "CHAR",
    "bool": "BOOL",
    "return": "RETURN"
}

# All tokens must be named in advance.
tokens = [
    'ID',

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
     
    'INT', 
    'FLOAT', 
    'CHAR',
    
    'EQUALS',
    'GT', 
    'LT', 
    'NOTEQ',
    'LESS_OR_EQ_THAN',
    'GREATER_OR_EQ_THAN',

    'INCREMENT_ONE',
    'DECREMENT_ONE',

    'LSQRE', 
    'RSQRE',
    'ISEQ',
    'BOOL',
    'VALUE',
    'LTEQ',
    'GTEQ',
    'PLUSEQ',
    'MINUSEQ',
    'TIMESEQ',
    'DIVEQ',
    'CTE_I',
    'CTE_F',
    'CTE_CHAR'
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
#t_VAR      = r'[a-zA-Z_][a-zA-Z0-9_]*'
#t_VAR      = r'(var)'

t_INT       = r'\d+'
t_FLOAT     = r'((\d*\.\d+)(E[\+-]?\d+)?|([1-9]\d*E[\+-]?\d+))'
#t_STRING   = r'\".*?\"'

t_EQUALS    = r'='
t_GT        = r'>'
t_LT        = r'<'
t_NOTEQ     = r'<>'
t_LESS_OR_EQ_THAN = r'<='
t_GREATER_OR_EQ_THAN = r'>='

t_INCREMENT_ONE = r'\++'
t_DECREMENT_ONE = r'--'
# Missing +=, -=, *=, /=

#t_CTEL     = r'(ctel)'
#t_CTEF     = r'(ctef)'
#t_CTESTRING= r'(ctestring)'


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
var id ,; 5 > <> 4.5 pelos
if (largo >= 5)
void suma() {{
    largo++;
    otro --;
    5/2
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