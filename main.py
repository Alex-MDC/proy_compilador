# -----------------------------------------------------------------------------
# main.py
# Note: 
# Grammar
# terminals: caps   ----------------------------------
# non terminal: lowercase ----------------------------
# TODO: update when needed
#  <program>  : dv df dc MAIN block 
#
#  <dv>       : dec_vars dv
#             | empty
#
#  <df>       : function df
#             | empty
#
#  <dc>       : class dc
#             | empty
# ------------------------------
#
#  <block>    : { block2 }
#
#  <block2>   :  block3
#             | empty
#
#  <block3>   :  statement block2
# ------------------------------
#
#  <statement> : assignment
#              | condition
#              | writing
#              | return
#              | loop
#              | input
#              | call
#              | arr_assign
# ------------------------------
#
#  <dv_func> : dec_vars dv_func
#              | empty
# ------------------------------
#
#  <dec_vars>       : VAR dec_vars2
#                   | VAR dec_vars3
#
#  <dec_vars2>      : simple_type dec_vars4
#
#  <dec_vars4>      : ID dec_vars6 dec_vars5 
#
#  <dec_vars5>      : , dec_vars4
#                   | empty
# 
#  <dec_vars6>      : [ CTE_INT ] dec_vars7
#                   | empty
#
#  <dec_vars7>      : [ CTE_INT ]
#                   | empty
#
#  <dec_vars3>      : compound_type ID dec_vars8
#
#  <dec_vars8>      : , ID dec_vars8
#                   | empty
# ------------------------------
#
#  <function>      : function2 ID ( function3 ) dv_func block
#
#  <function2>     : simple_type
#                  | VOID
#
#  <function3>     : parameter
#                  | empty
# ------------------------------
#
#  <class>         : CLASS ID { class4 class2 function class3 } ;
#
#  <class2>        : class4 class2
#                  | empty
#
#  <class3>        : function class3
#                  | empty
#
#  <class4>        : simple_type ID ;
#       
# ------------------------------
#
#  <compund_type> : id      
# ------------------------------
#
#  <simple_type>  : INT
#                 | FLOAT
#                 | CHAR
#                 | BOOL
# ------------------------------
#
#  <assignment>   : id = super_expression ;
# ------------------------------
#
#  <parameter>     : simple_type ID parameter2
#
#  <parameter2>    : , parameter
#                  | empty
# ------------------------------
# 
#  <var_cte>   : + CTE_INT  
#              | + CTE_FLOAT
#              | - CTE_INT
#              | - CTE_FLOAT
#              | CTE_INT
#              | CTE_FLOAT
#              | CTE_CHAR
#
# ------------------------------
# 
#  <super_expression>     : expression super_expression2
# 
#  <super_expression2>    : super_expression3 expression  
#                         | empty
#
#  <super_expression3>    : &&
#                         | ||
# ------------------------------
# 
#  <expression>     : exp expression2
# 
#  <expression2>    : expression3 exp  
#                   | empty
#
#  <expression3>    : >
#                   | < 
#                   | <> 
#                   | == 
# ------------------------------
#
#  <exp>   : term exp2
# 
#  <exp2>  :  + exp
#          |  - exp 
#          | empty
# ------------------------------
# 
#  <term>     : factor term2
# 
#  <term2>    : * term
#             | / term
#             |  empty
# ------------------------------
#
#  <factor>    : ( super_expression )
#              | var_cte
#              | variable
#              | call
#
# ------------------------------
#
#  <variable>   : ID variable2
# 
#  <variable2>  : [ exp ] variable3
#               | empty
# 
#  <variable3>  : [ exp ] 
#               | empty
# ------------------------------
#
#  <call>       : ID call2 
#               | ID call3
#
#  <call2>      : ( call4 )
#
#  <call4>      : exp call5
#               | empty
#
#  <call5>      : , exp call5
#               | empty
#
#  <call3>      : . ID 
#               | . ID call6
#
#  <call6>      : ( call7 )
#
#  <call7>      : exp call8
#               | empty
#
#  <call8>      : , exp call8
#               | empty
# ------------------------------
#
#  <condition>  : IF ( super_expression ) block condition2 
# 
#  <condition2> :  ELSE block 
#               | empty
# ------------------------------
#
#  <writing>    : print ( writing2 ) ;
#
#  <writing2>   : CTE_STR writing3
#               | super_expression writing3
#
#  <writing3>   : COMMA writing2
#               | empty
# ------------------------------
#
#  <return>        : RETURN super_expression
# ------------------------------
#
#  <loop>          : while ( super_expression ) block
# ------------------------------
#
#  <input>     : INPUT ( variable ) ;
# ------------------------------
#  <arr_assign>    : ID arr_assign1 = expression ;
#
# -----------------------------------------------------------------------------

from ply.lex import lex

# --- Tokenizer

reserved = {
    'if' : 'IF',
    'else' : 'ELSE',
    'print' : 'PRINT',
    'var' : 'VAR',
    "input": "INPUT",
    "void": "VOID", # TODO: Check if this is valid. Also check null
    "class": "CLASS",
    "main": "MAIN",
    "int": "INT",
    "float": "FLOAT",
    "char": "CHAR",
    "bool": "BOOL",
    "return": "RETURN",
    "and": "AND",
    "or": "OR",
    "while": "WHILE",
    "endl": "ENDLINE"
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
    'CTE_STR',
    'CTE_BOOL',
    
    'EQUALS',
    'EQEQ',
    'GT', 
    'LT', 
    'NOTEQ',
    'LESS_OR_EQ_THAN',
    'GREATER_OR_EQ_THAN',

    # --- TOKENS NOT USED ---
    # 'ISEQ',
    # 'VALUE',
    # 'LTEQ',
    # 'GTEQ',
    # 'PLUSEQ',
    # 'MINUSEQ',
    # 'TIMESEQ',
    # 'DIVEQ'
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
t_CTE_CHAR      = r"'[^']'"
t_CTE_STR       = r'"([^"\\]|\\.)*"'

t_EQUALS                   = r'='
t_GT                       = r'>'
t_LT                       = r'<'
t_NOTEQ                    = r'<>'
t_LESS_OR_EQ_THAN          = r'<='
t_GREATER_OR_EQ_THAN       = r'>='
t_EQEQ                     = r'=='

# A function can be used if there is an associated action.
# Write the matching regex in the docstring.
def t_CTE_BOOL(t):
    r'\b(True|False)\b'
    return t

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value,'ID')    # Check for reserved words
    return t

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
data = f''' False true
2
0.5 True
'''

# Give the lexer some input
lexer.input(data)

# Tokenize
while True:
    tok = lexer.token()
    if not tok:
        break      # No more input
    print(tok)