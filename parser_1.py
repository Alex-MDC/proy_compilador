import ply.yacc as yacc
from main import tokens
from semantic import *

#---------------------------
# --- Parser

# Write functions for each grammar rule which is
# specified in the docstring.
#terminales en mayus. no term en minsuc

def p_program(p):
    '''
    program : dv df dc MAIN block
    '''
    
    p[0] = ('begin program', p[1], p[2], p[3],p[4],p[5])

def p_dv(p):
    '''
    dv : dec_vars
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

def p_block(p):
    '''
    block : LCURL block2 RCURL
    '''
    p[0]=('block',p[1],p[2],p[3])

def p_block2(p):
    '''
    block2 : block3
           | empty
    '''
    p[0]=('block2',p[1])

def p_block3(p):
    '''
    block3 : statement block2
    '''
    p[0]=('block3',p[1])

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

def p_dec_vars(p):
    '''
    dec_vars : VAR dec_vars2
             | VAR dec_vars3
    '''
    p[0]=('dec_vars',p[1],p[2])

def p_dec_vars2(p):
    '''
    dec_vars2 : simple_type dec_vars4
    '''
    p[0]=('dec_vars2',p[1],p[2])

def p_dec_vars4(p):
    '''
    dec_vars4 : ID dec_vars6 dec_vars5
    '''
    p[0]=('dec_vars4',p[1],p[2],p[3])

def p_dec_vars5(p):
    '''
    dec_vars5 : COMMA dec_vars4
        | empty
    '''
    if (len(p) == 3):
        p[0] = ('dec_vars5',p[1],p[2])
    elif (len(p) == 2):
        p[0] = p[1]

def p_dec_vars6(p):
    '''
    dec_vars6 : LBRACKET CTE_INT RBRACKET dec_vars7
        | LBRACKET CTE_INT RBRACKET arr_init
        | assignment
        | empty
    '''
    if (len(p) == 5):
        p[0] = ('dec_vars6',p[1],p[2],p[3],p[4])
    elif (len(p) == 2):
        p[0] = p[1]

def p_dec_vars7(p):
    '''
    dec_vars7 : LBRACKET CTE_INT RBRACKET 
        | LBRACKET CTE_INT RBRACKET arr_init
        | empty
    '''
    if (len(p) == 5):
        p[0] = ('dec_vars7',p[1],p[2],p[3],p[4])
    elif (len(p) == 4):
        p[0] = ('dec_vars7',p[1],p[2],p[3])
    elif (len(p) == 2):
        p[0] = p[1]

def p_dec_vars3(p):
    '''
    dec_vars3 : compound_type ID dec_vars8
    '''
    p[0]=('dec_vars3',p[1],p[2],p[3])

def p_dec_vars8(p):
    '''
    dec_vars8 : COMMA ID dec_vars8
        | empty
    '''
    if (len(p) == 4):
        p[0] = ('dec_vars8',p[1],p[2],p[3])
    elif (len(p) == 2):
        p[0] = p[1]

def p_function(p):
    '''
    function : function2 ID LPAREN function3 RPAREN dec_vars block
    '''
    p[0] = ('function',p[1],p[2],p[3],p[4],p[5],p[6],p[7])

def p_function2(p):
    '''
    function2 : simple_type
              | VOID
    '''
    p[0] = ('function2',p[1] )

def p_function3(p):
    '''
    function3 : parameter
              | empty
    '''
    p[0] = ('function3',p[1] )

def p_class(p):
    '''
    class : CLASS ID LCURL simple_type ID SEMIC class2 function class3 RCURL SEMIC
    '''
    p[0] = ('class',p[1],p[2],p[3],p[4],p[5],p[6],p[7],p[8],p[9],p[10],p[11])

def p_class2(p):
    '''
    class2 : simple_type ID SEMIC class2
           | empty
    '''
    if (len(p) == 5):
     p[0] = ('class2',p[1],p[2],p[3],p[4])
    else:
        p[0] = p[1] 

def p_class3(p):
    '''
    class3 : function class3
           | empty
    '''
    if (len(p) == 3):
     p[0] = ('class3',p[1],p[2])
    else:
        p[0] = p[1] 

def p_arr_init(p):
    '''
    arr_init : EQUALS LCURL arr_init2 RCURL
    '''
    p[0] = ('arr_init',p[1],p[2],p[3],p[4])

def p_arr_init2(p):
    '''
    arr_init2 : var_cte arr_init3
              | LCURL var_cte arr_init3 RCURL arr_init4
    '''
    if (len(p) == 3):
        p[0] = ('arr_init2',p[1],p[2])
    else:
        p[0] = ('arr_init2',p[1],p[2],p[3],p[4],p[5])

def p_arr_init3(p):
    '''
    arr_init3 : COMMA var_cte arr_init3
              | empty
    '''
    if (len(p) == 4):
        p[0] = ('arr_init3',p[1],p[2],p[3])
    else:
        p[0] = ('arr_init3',p[1])

def p_arr_init4(p):
    '''
    arr_init4   : COMMA LCURL var_cte arr_init3 RCURL arr_init4
                | empty
    '''
    if (len(p) == 7):
        p[0] = ('arr_init4',p[1],p[2],p[3],p[4],p[5],p[6])
    else:
        p[0] = ('arr_init4',p[1])

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

def p_parameter(p):
    '''
    parameter : simple_type ID parameter2
    '''
    p[0] = ('parameter',p[1],p[2],p[3])

def p_parameter2(p):
    '''
    parameter2 : COMMA parameter
          | empty
    '''
    if (len(p) == 3):
        p[0] = ('parameter2',p[1],p[2])
    else:
        p[0] = p[1] 

def p_var_cte(p):
    '''
    var_cte : CTE_INT 
       | CTE_FLOAT
       | CTE_CHAR
    '''
    p[0] = ('var_cte',p[1] )
    #TODO call addconstant
    



def p_expression(p):
    '''
    expression : exp expression2
    '''
    p[0] = ('expression',p[1],p[2])

def p_expression2(p):
    '''
    expression2 : expression3 exp
       | empty
    '''
    if (len(p) == 3):
     p[0] = ('expression2',p[1],p[2])
    else:
        p[0] = p[1] 

def p_expression3(p):
    '''
    expression3 : GT
       | LT
       | NOTEQ
       | EQEQ
    '''
    p[0] = ('expression3',p[1])

def p_exp(p):
    '''
    exp : term exp2
    '''
    p[0] = ('exp',p[1],p[2])

def p_exp2(p):
    '''
    exp2 : PLUS exp
       | MINUS exp
       | empty
    '''
    if (len(p) == 3):
     p[0] = ('exp2',p[1],p[2])
    else:
        p[0] = p[1] 

def p_term(p):
    '''
    term : factor term2
    '''
    p[0] = ('term',p[1],p[2])

def p_term2(p):
    '''
    term2 : TIMES term
       | DIVIDE term
       | empty
    '''
    if (len(p) == 3):
     p[0] = ('term2',p[1],p[2])
    else:
        p[0] = p[1] 

def p_factor(p):
    '''
    factor : LPAREN expression RPAREN
           | factor2
           | variable
           | call
    '''
    if (len(p) == 4):
        p[0] = ('factor',p[1],p[2],p[3])
    else:
        p[0] = ('factor',p[1])

def p_factor2(p):
    '''
    factor2 : factor3 var_cte
    '''
    p[0] = ('factor2',p[1],p[2]) 

def p_factor3(p):
    '''
    factor3 : PLUS
       | MINUS
       | empty
    '''
    p[0] = p[1]

def p_variable(p):
    '''
    variable : ID variable2
    '''
    #   TODO verify ID exists in current function
    p[0] = ('variable',p[1], p[2])
    

def p_variable2(p):
    '''
    variable2 : LBRACKET exp RBRACKET variable3
       | empty
    '''
    if (len(p) == 5):
     #TODO verify type of p[2] exp is int

     p[0] = ('variable2',p[1],p[2],p[3],p[4])
    else:
        p[0] = p[1] 

def p_variable3(p):
    '''
    variable3 : LBRACKET exp RBRACKET
       | empty
    '''
    if (len(p) == 4):
     p[0] = ('variable3',p[1],p[2],p[3])
    else:
        p[0] = p[1] 

def p_call(p):
    '''
    call : ID call2
       | ID call3
    '''
    p[0] = ('call',p[1],p[2] )

def p_call2(p):
    '''
    call2 : LPAREN call4 RPAREN
    '''
    p[0] = ('call2',p[1],p[2],p[3] )

def p_call4(p):
    '''
    call4 : exp call5
     | empty
    '''
    if (len(p) == 3):
        p[0] = ('call4',p[1],p[2])
    else:
        p[0] = ('call4',p[1])

def p_call5(p):
    '''
    call5 : COMMA exp call5
     | empty
    '''
    if (len(p) == 4):
        p[0] = ('call5',p[1],p[2],p[3])
    else:
        p[0] = ('call5',p[1])

def p_call3(p):
    '''
    call3 : DOT ID
        | DOT ID call6
    '''
    if (len(p) == 3):
        p[0] = ('call3',p[1],p[2])
    elif(len(p)== 4):
        p[0] = ('call3',p[1],p[2],p[3])

def p_call6(p):
    '''
    call6 : LPAREN call7 RPAREN
    '''
    p[0] = ('call6',p[1],p[2],p[3] )

def p_call7(p):
    '''
    call7 : exp call8
        | empty
    '''
    if (len(p) == 3):
        p[0] = ('call7',p[1],p[2])
    elif(len(p)== 2):
        p[0] = p[1]

def p_call8(p):
    '''
    call8 : COMMA exp call8
        | empty
    '''
    if (len(p) == 4):
        p[0] = ('call8',p[1],p[2],p[4])
    elif(len(p)== 2):
        p[0] = p[1]

def p_condition(p):
    '''
    condition : IF LPAREN expression RPAREN block condition2
    '''
    p[0] = ('condition',p[1],p[2],p[3],p[4],p[5],p[6])

def p_condition2(p):
    '''
    condition2 : ELSE block
       | empty
    '''
    if (len(p) == 3):
     p[0] = ('condition2',p[1],p[2])
    else:
        p[0] = p[1] 

def p_writing(p):
    '''
    writing : PRINT LPAREN expression RPAREN SEMIC
    '''
    p[0] = ('writing',p[1],p[2],p[3],p[4],p[5])

def p_return(p):
    '''
    return : RETURN ID
          | RETURN expression
    '''
    p[0] = ('return',p[1],p[2])

def p_loop(p):
    '''
    loop : FOR ID EQUALS exp TO exp DO statement SEMIC
    '''
    p[0] = ('loop',p[1],p[2],p[3],p[4],p[5],p[6],p[7],p[8],p[9])

def p_input(p):
    '''
    input : ID EQUALS INPUT LPAREN variable RPAREN SEMIC
    '''
    p[0] = ('input',p[1],p[2],p[3],p[4],p[5],p[6],p[7]) 

def p_arr_assign(p):
    '''
    arr_assign : ID arr_assign1 EQUALS expression SEMIC
    '''
    p[0] = ('arr_assign',p[1],p[2],p[3],p[4],p[5])

def p_arr_assign1(p):
    '''
    arr_assign1 : LBRACKET exp RBRACKET arr_assign2
    '''
    p[0] = ('arr_assign1',p[1],p[2],p[3],p[4])

def p_arr_assign2(p):
    '''
    arr_assign2 : LBRACKET exp RBRACKET 
        | empty
    '''
    if (len(p) == 4):
        p[0] = ('arr_assign2',p[1],p[2],p[3])
    else:
        p[0] = ('arr_assign2',p[1])

def p_empty(p):
    'empty :'
    pass


def p_error(p):
    print(f'Syntax error in {p.value}')

# Build the parser
parser = yacc.yacc()

data = '''
program id; { if(a > b) {id = ctef; }; } 
'''

while True:
  try:
      s = input('input program > ')
  except EOFError:
      break
  if not s: continue
  #result contains the AST tree
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