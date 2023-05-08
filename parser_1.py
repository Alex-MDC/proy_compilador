import ply.yacc as yacc
from main import tokens

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
parser = yacc.yacc()


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

while True:
  try:
      s = input('input program > ')
  except EOFError:
      break
  if not s: continue
  result = parser.parse(s)
  print(result)


# text = open("pruebas.txt","r")
# for x in text:
#     lexer.input(x)
#     # Tokenize
#     for tok in lexer:
#         print(tok)
#     #parser.parse(x, debug=True)
#     print(parser.parse(x))