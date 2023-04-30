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
# <block>    : { BP }
#
#  <BP>        :  b
#              | empty
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
from ply.yacc import yacc

# --- Tokenizer

reserved = {
   'if' : 'IF',
   'else' : 'ELSE',
   'print' : 'PRINT',
 #  'program' : 'PROGRAM',
   'var' : 'VAR',
  # 'ctel' : 'CTEL',
 #  'ctef' : 'CTEF',
  # 'ctestring' : 'CTESTRING'
   'for' : 'FOR',
   "input": "INPUT",
   "void": "VOID", #check if this is valid. also check null
   "class": "CLASS",

}

# All tokens must be named in advance.
tokens = [ 'ID','COLON', 'SEMIC','PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'LPAREN', 'RPAREN',
 'COMMA', 'INT', 'FLOAT', 'LCURL', 'RCURL','EQUALS',
 'GT', 'LT', 'NOTEQ' ] + list(reserved.values())

# Ignored characters
t_ignore = ' \t'

# Token matching rules are written as regexs
#t_PROGRAM = r'(program)'
t_PLUS = r'\+'
t_COLON = r'\:'
t_SEMIC = r'\;'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
#t_VAR = r'[a-zA-Z_][a-zA-Z0-9_]*'
#t_VAR = r'(var)'
t_COMMA = r','
t_LCURL = r'\{'
t_RCURL = r'\}'
t_EQUALS = r'='
t_INT = r'\d+'
t_FLOAT = r'((\d*\.\d+)(E[\+-]?\d+)?|([1-9]\d*E[\+-]?\d+))'
#t_STRING = r'\".*?\"'
t_GT = r'>'
t_LT = r'<'
t_NOTEQ = r'<>'
#t_CTEL = r'(ctel)'
#t_CTEF = r'(ctef)'
#t_CTESTRING = r'(ctestring)'



# A function can be used if there is an associated action.
# Write the matching regex in the docstring.

# reserved words
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

#---------------------------
# --- Parser

# Write functions for each grammar rule which is
# specified in the docstring.
#terminales en mayus. no term en minsuc
def p_programa(p):
    '''
    programa : PROGRAM ID SEMIC varsp bloque
    '''
    # p is a sequence that represents rule contents.
    #
    # expression : term PLUS term
    #   p[0]     : p[1] p[2] p[3]
    # 
    p[0] = ('inicio_prog', p[1], p[2], p[3],p[4],p[5])

def p_empty(p):
    'empty :'
    pass

def p_varsp(p):
    '''
    varsp : vars
          | empty
    '''
    p[0] = p[1]

def p_vars(p):
    '''
    vars : VAR ID idp COLON tipo SEMIC vp
    '''
    p[0] = ('vars',p[1], p[2], p[3] ,p[4], p[5] ,p[6], p[7])

def p_idp(p):
    '''
    idp : COMMA ID idp
        | empty
    '''
    if (len(p) == 4):
     p[0] = (p[1],p[2],p[3])
    else:
        p[0] = p[1]

def p_vp(p):
    '''
    vp : ID idp COLON tipo SEMIC vp
        | empty
    '''
    if (len(p) == 7):
     p[0] = (p[1],p[2],p[3],p[4],p[5],p[6])
    else:
        p[0] = p[1]

def p_tipo(p):
    '''
    tipo : INT
         | FLOAT
    '''
    p[0]=('tipo',p[1])

def p_bloque(p):
    '''
    bloque : LCURL bp RCURL
    '''
    p[0]=('bloque',p[2])

def p_bp(p):
    '''
    bp : estatuto bp
        | empty
    '''
    if (len(p) == 3):
     p[0] = (p[1],p[2])
    else:
        p[0] = p[1]

def p_factor(p):
    '''
    factor : LPAREN expresion RPAREN
           | fp
    '''
    if (len(p) == 4):
     p[0] = ('factor',p[2])
    else:
        p[0] = p[1]    

def p_fp(p):
    '''
    fp : mp varkte
    '''
    p[0] = (p[1],p[2])   

def p_mp(p):
    '''
    mp : PLUS
       | MINUS
       | empty
    '''
    p[0] = p[1]
 
def p_estatuto(p):
    '''
    estatuto : asignacion
            | condicion
            | escritura
    '''
    p[0] = ('estatuto',p[1])

def p_asignacion(p):
    '''
    asignacion : ID EQUALS expresion SEMIC
    '''
    p[0] = ('asignacion',p[1],p[2],p[3],p[4] )

def p_expresion(p):
    '''
    expresion : exp ep
    '''
    p[0] = ('expresion',p[1],p[2])

def p_ep(p):
    '''
    ep : GT exp
       | LT exp
       | NOTEQ exp
       | empty
    '''
    if (len(p) == 3):
     p[0] = (p[1],p[2])
    else:
        p[0] = p[1] 

def p_exp(p):
    '''
    exp : termino xp
    '''
    p[0] = (p[1],p[2])

def p_xp(p):
    '''
    xp : PLUS exp
       | MINUS exp
       | empty
    '''
    if (len(p) == 3):
     p[0] = (p[1],p[2])
    else:
        p[0] = p[1] 

def p_termino(p):
    '''
    termino : factor tp
    '''
    p[0] = ('termino',p[1],p[2])

def p_tp(p):
    '''
    tp : TIMES termino
       | DIVIDE termino
       | empty
    '''
    if (len(p) == 3):
     p[0] = (p[1],p[2])
    else:
        p[0] = p[1] 

def p_varkte(p):
    '''
    varkte : ID
       | CTEL
       | CTEF
    '''
    p[0] = ('var_kte',p[1] )

def p_condicion(p):
    '''
    condicion : IF LPAREN expresion RPAREN bloque cp SEMIC
    '''
    p[0] = ('condicion',p[3],p[5],p[6],p[7])

def p_cp(p):
    '''
    cp : ELSE bloque
       | empty
    '''
    if (len(p) == 3):
     p[0] = (p[1],p[2])
    else:
        p[0] = p[1] 
def p_escritura(p):
    '''
    escritura : PRINT LPAREN pp RPAREN SEMIC
    '''
    p[0] = ('escritura',p[3])

def p_pp(p):
    '''
    pp : expresion p
       | CTESTRING p
    '''
    p[0] = (p[1],p[2])


def p_p(p):
    '''
    p : COMMA pp
       | empty
    '''
    if (len(p) == 3):
     p[0] = (p[1],p[2])
    else:
        p[0] = p[1] 


def p_error(p):
    print(f'Syntax error at {p.value!r}')

# Build the parser
parser = yacc()


# --accepted:
# program id ; { id = +ctel;}
# program id ; {}
# program id; { if(a > b) {id = ctef; }; } 
# --deberia ser error:
# program id ; { print(); }
# program id ; { if(4>5) {id = 22.3}; }
data = '''
program id; { if(a > b) {id = ctef; }; } 
'''
#lexer.input(data)

# Tokenize
#for tok in lexer:
#    print(tok)

#while True:
#   try:
#       s = input('input program > ')
#   except EOFError:
#       break
#   if not s: continue
#   result = parser.parse(s)
#   print(result)


text = open("pruebas.txt","r")
for x in text:
    lexer.input(x)
    # Tokenize
    for tok in lexer:
        print(tok)
    #parser.parse(x, debug=True)
    print(parser.parse(x))