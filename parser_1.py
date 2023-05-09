import ply.yacc as yacc
from main import tokens

#---------------------------
# --- Parser

# Write functions for each grammar rule which is
# specified in the docstring.
#terminales en mayus. no term en minsuc

def p_program(p):
    '''
    program : dv df dc MAIN block
    '''
    # p is a sequence that represents rule contents.
    #
    # expression : term PLUS term
    #   p[0]     : p[1] p[2] p[3]
    # 
    p[0] = ('begin program', p[1], p[2], p[3],p[4],p[5])

def p_dv(p):
    '''
    dv : dec_vars dv
        | empty
    '''
    if (len(p) == 3):
     p[0] = (p[1],p[2])
    else:
        p[0] = p[1]

def p_df(p):
    '''
    df : function df
        | empty
    '''
    if (len(p) == 3):
     p[0] = (p[1],p[2])
    else:
        p[0] = p[1]

def p_dc(p):
    '''
    dc : class dc
        | empty
    '''
    if (len(p) == 3):
     p[0] = (p[1],p[2])
    else:
        p[0] = p[1]


def p_empty(p):
    'empty :'
    pass

def p_statement(p):
    '''
    statement : assignment
            | condition
            | writing
            | return
            | loop
            | input
            | call
            | arr_assign
    '''
    p[0] = ('statement',p[1])

def p_block(p):
    '''
    block : LCURL bp RCURL
    '''
    p[0]=('block',p[2])

def p_bp(p):
    '''
    bp : b
        | empty
    '''
    p[0]=('bp',p[1])

def p_b(p):
    '''
    b : statement bp
    '''
    p[0]=('b',p[1],p[2])

def p_dec_vars(p):
    '''
    dec_vars : VAR sp
             | VAR cp
    '''
    p[0]=('dec_vars',p[1],p[2])

def p_sp(p):
    '''
    sp : simple_type spp
    '''
    p[0]=('sp',p[1],p[2])

def p_spp(p):
    '''
    spp : ID da sppp
    '''
    p[0]=('spp',p[1],p[2],p[3])

def p_sppp(p):
    '''
    sppp : COMMA spp
        | empty
    '''
    if (len(p) == 3):
        p[0] = ('sppp',p[1],p[2])
    elif (len(p) == 2):
        p[0] = p[1]

def p_da(p):
    '''
    da : LBRACKET CTE_INT RBRACKET db
        | LBRACKET CTE_INT RBRACKET arr_init
        | assignment
        | empty
    '''
    if (len(p) == 5):
        p[0] = ('da',p[1],p[2],p[3],p[4])
    elif (len(p) == 2):
        p[0] = p[1]

def p_db(p):
    '''
    db : LBRACKET CTE_INT RBRACKET 
        | LBRACKET CTE_INT RBRACKET arr_init
        | empty
    '''
    if (len(p) == 5):
        p[0] = ('db',p[1],p[2],p[3],p[4])
    elif (len(p) == 4):
        p[0] = ('db',p[1],p[2],p[3])
    elif (len(p) == 2):
        p[0] = p[1]

def p_cp(p):
    '''
    cp : compound_type ID cpp
    '''
    p[0]=('cp',p[1],p[2],p[3])

def p_cpp(p):
    '''
    cpp : COMMA ID cpp
        | empty
    '''
    if (len(p) == 4):
        p[0] = ('cpp',p[1],p[2],p[3])
    elif (len(p) == 2):
        p[0] = p[1]

def p_factor(p):
    '''
    factor : LPAREN expression RPAREN
           | fp
           | variable
           | call
    '''
    if (len(p) == 4):
        p[0] = ('factor',p[1],p[2],p[3])
    else:
        p[0] = ('factor',p[1])

def p_fp(p):
    '''
    fp : mp var_cte
    '''
    p[0] = ('fp',p[1],p[2]) 

def p_mp(p):
    '''
    mp : PLUS
       | MINUS
       | empty
    '''
    p[0] = p[1]

def p_var_cte(p):
    '''
    var_cte : CTE_INT
       | CTE_FLOAT
       | CTE_CHAR
    '''
    p[0] = ('var_cte',p[1] )

def p_input(p):
    '''
    input : ID EQUALS INPUT LPAREN variable RPAREN SEMIC
    '''
    p[0] = ('input',p[1],p[2],p[3],p[4],p[5],p[6],p[7]) 

def p_call(p):
    '''
    call : ID callp
       | ID callpp
    '''
    p[0] = ('call',p[1],p[2] )

def p_callp(p):
    '''
    callp : LPAREN callppp RPAREN
    '''
    p[0] = ('callp',p[1],p[2],p[3] )

def p_callppp(p):
    '''
    callppp : exp callpppp
     | empty
    '''
    if (len(p) == 3):
        p[0] = ('callppp',p[1],p[2])
    else:
        p[0] = ('callppp',p[1])

def p_callpppp(p):
    '''
    callpppp : COMMA exp callpppp
     | empty
    '''
    if (len(p) == 4):
        p[0] = ('callpppp',p[1],p[2],p[3])
    else:
        p[0] = ('callpppp',p[1])

def p_callpp(p):
    '''
    callpp : DOT ID
        | DOT ID q
    '''
    if (len(p) == 3):
        p[0] = ('callpp',p[1],p[2])
    elif(len(p)== 4):
        p[0] = ('callpp',p[1],p[2],p[3])

def p_q(p):
    '''
    q : LPAREN qp RPAREN
    '''
    p[0] = ('q',p[1],p[2],p[3] )

def p_qp(p):
    '''
    qp : exp qpp
        | empty
    '''
    if (len(p) == 3):
        p[0] = ('qp',p[1],p[2])
    elif(len(p)== 2):
        p[0] = p[1]

def p_qpp(p):
    '''
    qpp : COMMA exp qpp
        | empty
    '''
    if (len(p) == 4):
        p[0] = ('qpp',p[1],p[2],p[4])
    elif(len(p)== 2):
        p[0] = p[1]

def p_assignment(p):
    '''
    assignment : assignmentp EQUALS expression SEMIC
    '''
    p[0] = ('assignment',p[1],p[2],p[3],p[4] )

def p_assignmentp(p):
    '''
    assignmentp : ID
        | empty
    '''
    p[0] = ('assignment',p[1])

def p_expression(p):
    '''
    expression : exp ep
    '''
    p[0] = ('expression',p[1],p[2])

def p_ep(p):
    '''
    ep : epp exp
       | empty
    '''
    if (len(p) == 3):
     p[0] = ('ep',p[1],p[2])
    else:
        p[0] = p[1] 

def p_epp(p):
    '''
    epp : GT
       | LT
       | NOTEQ
       | EQEQ
    '''
    p[0] = ('epp',p[1])

def p_exp(p):
    '''
    exp : term xp
    '''
    p[0] = ('exp',p[1],p[2])

def p_xp(p):
    '''
    xp : PLUS exp
       | MINUS exp
       | empty
    '''
    if (len(p) == 3):
     p[0] = ('xp',p[1],p[2])
    else:
        p[0] = p[1] 

def p_term(p):
    '''
    term : factor tp
    '''
    p[0] = ('term',p[1],p[2])

def p_tp(p):
    '''
    tp : TIMES term
       | DIVIDE term
       | empty
    '''
    if (len(p) == 3):
     p[0] = ('tp',p[1],p[2])
    else:
        p[0] = p[1] 

def p_condition(p):
    '''
    condition : IF LPAREN expression RPAREN block cp
    '''
    p[0] = ('condition',p[1],p[2],p[3],p[4],p[5],p[6])

def p_cp(p):
    '''
    cp : ELSE block
       | empty
    '''
    if (len(p) == 3):
     p[0] = ('cp',p[1],p[2])
    else:
        p[0] = p[1] 

def p_writing(p):
    '''
    writing : PRINT LPAREN expression RPAREN SEMIC
    '''
    p[0] = ('writing',p[1],p[2],p[3],p[4],p[5])

def p_variable(p):
    '''
    variable : ID ap
    '''
    p[0] = ('variable',p[1], p[2])

def p_ap(p):
    '''
    ap : LBRACKET exp RBRACKET bp
       | empty
    '''
    if (len(p) == 5):
     p[0] = ('ap',p[1],p[2],p[3],p[4])
    else:
        p[0] = p[1] 

def p_bp(p):
    '''
    bp : LBRACKET exp RBRACKET
       | empty
    '''
    if (len(p) == 4):
     p[0] = ('bp',p[1],p[2],p[3])
    else:
        p[0] = p[1] 

def p_compound_type(p):
    '''
    compound_type : ID 
    '''
    p[0] = ('compound_type',p[1])

def p_simple_type(p):
    '''
    simple_type : INT
        | FLOAT
        | CHAR
        | BOOL
    '''
    p[0]=('simple_type',p[1]) 

def p_loop(p):
    '''
    loop : FOR ID EQUALS exp TO exp DO statement SEMIC
    '''
    p[0] = ('loop',p[1],p[2],p[3],p[4],p[5],p[6],p[7],p[8],p[9])

def p_class(p):
    '''
    class : CLASS ID LCURL simple_type ID SEMIC lt function lf RCURL SEMIC
    '''
    p[0] = ('class',p[1],p[2],p[3],p[4],p[5],p[6],p[7],p[8],p[9],p[10],p[11])

def p_lt(p):
    '''
    lt : simple_type ID SEMIC lt
       | empty
    '''
    if (len(p) == 5):
     p[0] = ('lt',p[1],p[2],p[3],p[4])
    else:
        p[0] = p[1] 

def p_lf(p):
    '''
    lf : function lf
       | empty
    '''
    if (len(p) == 3):
     p[0] = ('lf',p[1],p[2])
    else:
        p[0] = p[1] 

def p_function(p):
    '''
    function : fs ID LPAREN fp RPAREN dec_vars block
    '''
    p[0] = ('function',p[1],p[2],p[3],p[4],p[5],p[6],p[7])

def p_fs(p):
    '''
    fs : simple_type
       | VOID
    '''
    p[0] = ('fs',p[1] )

def p_fp(p):
    '''
    fp : parameter
       | empty
    '''
    p[0] = ('fp',p[1] )

def p_parameter(p):
    '''
    parameter : simple_type ID pl
    '''
    p[0] = ('parameter',p[1],p[2],p[3])

def p_pl(p):
    '''
    pl : COMMA parameter
          | empty
    '''
    if (len(p) == 3):
        p[0] = ('pl',p[1],p[2])
    else:
        p[0] = p[1] 

def p_arr_init(p):
    '''
    arr_init : EQUALS LCURL aip RCURL
    '''
    p[0] = ('arr_init',p[1],p[2],p[3],p[4])

def p_aip(p):
    '''
    aip : var_cte aipp
          | LCURL var_cte aipp RCURL aippp
    '''
    if (len(p) == 3):
        p[0] = ('aip',p[1],p[2])
    else:
        p[0] = ('aip',p[1],p[2],p[3],p[4],p[5])

def p_aipp(p):
    '''
    aipp : COMMA var_cte aipp
          | empty
    '''
    if (len(p) == 4):
        p[0] = ('aipp',p[1],p[2],p[3])
    else:
        p[0] = ('aipp',p[1])

def p_aippp(p):
    '''
    aippp : COMMA LCURL var_cte aipp RCURL aippp
          | empty
    '''
    if (len(p) == 7):
        p[0] = ('aippp',p[1],p[2],p[3],p[4],p[5],p[6])
    else:
        p[0] = ('aippp',p[1])

def p_arr_assign(p):
    '''
    arr_assign : ID arr_assign1 EQUALS expression SEMIC
    '''
    p[0] = ('arr_assign',p[1],p[2],p[3],p[4],p[5])

def p_arr_assign1(p):
    '''
    arr_assign1: LBRACKET exp RBRACKET arr_assign2
    '''
    p[0] = ('arr_assign1',p[1],p[2],p[3],p[4])

def p_arr_assign2(p):
    '''
    arr_assign2: LBRACKET exp RBRACKET 
        | empty
    '''
    if (len(p) == 4):
        p[0] = ('arr_assign2',p[1],p[2],p[3])
    else:
        p[0] = ('arr_assign2',p[1])

def p_return(p):
    '''
    return : RETURN ID
          | RETURN expression
    '''
    p[0] = ('return',p[1],p[2])


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