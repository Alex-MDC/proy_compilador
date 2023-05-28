import ply.yacc as yacc
from main import tokens
from Context import Context
from FunctionTable import FunctionTable
from Quadruples import Quadruples 
from VariableTable import VariableTable
from SemanticCube import SemanticCube
from MemoryMap import MemoryMap
from VirtualMachine import VirtualMachine
# --- Parser

# Write functions for each grammar rule which is specified in the docstring.
# Terminales en mayus. no term en minsuc

curr = Context()
functionTable = FunctionTable()
quadruples = Quadruples()
constantsTable = VariableTable()
semanticCube = SemanticCube()

# Memory maps
memGlobal = MemoryMap(1000, 2000, 3000, 4000,5000)
memLocal = MemoryMap(15000,16000,17000,18000,19000)
memTemporal = MemoryMap(20000, 21000, 22000, 23000,24000,29000)
memConstants = MemoryMap(25000, 26000, 27000, 500,600,None, True)
#Pointers = 29,000 ... 30,000

# TODO
# Convert 'signos' into numerical codes 
# Delete function's vars table whenever we are out of that scope

def p_program(p):
    '''
    program : set_global_scope dv df dc MAIN solve_pending_jump_main block
    '''
    # Add quadruple for end of program
    quad = ['ENDPROG', '', '', '']
    quadruples.quadruples.append(quad)

    
    # Execute code in virtual machine
    VirtualMachine(quadruples.quadruples, memConstants, functionTable, memGlobal)

    functionTable.print_function_table()
    functionTable.delete_function_table()
    quadruples.print_stacks()

    print("Global memory map: ")
    memGlobal.printMemoryMap()

    print("Local memory map: ")
    memLocal.printMemoryMap()

    print("Temporal's memory map: ")
    memTemporal.printMemoryMap()

    print("Constants' memory map: ")
    memConstants.printMemoryMap()

    print("Constant's table: ")
    constantsTable.print_var_table()

    # We are out of the current scope
    curr.popScope()

    p[0] = ('begin program', p[1], p[2], p[3],p[4],p[5])

def p_set_global_scope(p):
    "set_global_scope :"
    # Set current scope
    curr.setScope('main')

    # Add to function table
    functionTable.add_function('main', 'int')

    # Add quadruple for jump to main
    quad = ['GOTO', 'main', '', '']
    quadruples.quadruples.append(quad)

    # Add to jump's stack to solve later
    quadruples.stack_jumps.append(len(quadruples.quadruples) - 1)

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

def p_dv_func(p):
    '''
    dv_func : dec_vars dv_func
        | empty
    '''
    if (len(p) == 3):
        p[0] = (p[1],p[2])
    else:
        p[0] = p[1]

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
    dec_vars4 : ID add_var dec_vars6 dec_vars5
    '''
    p[0]=('dec_vars4',p[1],p[2],p[3])

def p_add_var(p):
    "add_var :"
    # Add var to memory map
    virtual_address = 0
    if (curr.getScope() == 'main'):
        virtual_address = memGlobal.addVar(p[-1], curr.getCurrType())
    else:
        virtual_address = memLocal.addVar(p[-1], curr.getCurrType())
    
    # Check if virtual address is in valid range
    if virtual_address is None:
        raise yacc.YaccError(f"Stack overflow!")

    # Add var and check if variable is not already declared within current function (scope)
    if (functionTable.add_var_to_function(curr.getScope(), p[-1], curr.getCurrType(), virtual_address) is None):
        raise yacc.YaccError(f"Variable {p[-1]} already declared")

    # Update function's resources
    functionTable.set_resources_to_function(curr.getScope(), 'var ' + curr.getCurrType())


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
        | empty
    '''
    if (len(p) == 5):
        p[0] = ('dec_vars6',p[1],p[2],p[3],p[4])
    elif (len(p) == 2):
        p[0] = p[1]

def p_dec_vars7(p):
    '''
    dec_vars7 : LBRACKET CTE_INT RBRACKET
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
    function : function2 ID set_scope LPAREN function3 RPAREN dv_func block
    '''
    # Add quad ENDFUNC
    function_name = curr.getScope()
    quad = ['ENDFUNC', '', '', function_name]
    quadruples.quadruples.append(quad)

    # We are out of the current scope
    curr.popScope()

    p[0] = ('function',p[1],p[2],p[3],p[4],p[5],p[6],p[7])

def p_function2(p):
    '''
    function2 : simple_type 
              | VOID
    '''
    p[0] = p[1]


def p_function3(p):
    '''
    function3 : parameter
              | empty
    '''
    p[0] = ('function3',p[1] )

def p_set_scope(p):
    "set_scope :"
    
    #save potential return type if function is not void
    if(p[-2] != "void"):
        ret_type = p[-2]
        varName = p[-1]

        # Add var to memory map
        virtual_address = memGlobal.addVar(varName, ret_type)

        # Check if virtual address is in valid range
        if virtual_address is None:
            raise yacc.YaccError(f"Stack overflow!")

        #save return type as a duplicate var with the name of the function
        if (functionTable.add_var_to_function("main", varName, ret_type, virtual_address) is None):
            raise yacc.YaccError(f"Variable {p[-1]} already declared")
        
    # Set current scope
    curr.setScope(p[-1])

    # Each time we enter a new scope we can reuse temporals from before
    quadruples.reset_temporal_counter()

    # Reset memory map
    memTemporal.resetMemoryMap()

    # Add function to function table
    if (functionTable.add_function(p[-1], p[-2]) is None):
        raise yacc.YaccError(f"Function {p[-1]} already declared")

    # Save dirVir to be equal to quad where function starts
    functionTable.set_dirVir(curr.getScope(), len(quadruples.quadruples))

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
    curr.setCurrType(p[1])
    
    p[0]=p[1]

def p_assignment(p):
    '''
    assignment : ID EQUALS super_expression SEMIC
    '''
    # Verify id exists in current scope or global scope
    if ((functionTable.get_var_type_in_function(curr.getScope(), p[1]) is None) and (functionTable.get_var_type_in_function('main', p[1]) is None)):
        raise yacc.YaccError(f"Variable {p[1]} is not declared")
    
    elif (functionTable.get_var_type_in_function(curr.getScope(), p[1]) != None):
        assignee_operand = functionTable.get_var_dirVir_in_function(curr.getScope(), p[1])
        type = functionTable.get_var_type_in_function(curr.getScope(), p[1])

    elif(functionTable.get_var_type_in_function('main', p[1]) != None):
        assignee_operand = functionTable.get_var_dirVir_in_function('main', p[1])
        type = functionTable.get_var_type_in_function('main', p[1])

    # Generate quad
    operator = p[2]
    left_operand = quadruples.stack_operands.pop()

    # Verify types are same
    if(type == quadruples.stack_types.pop()):
        quad = [operator, left_operand, '', assignee_operand]
        # By now, these two pops have erased the latest remaining operand and type
        quadruples.quadruples.append(quad)
    else:
        raise yacc.YaccError(f"Type mismatch on assignment!")

    p[0] = ('assignment',p[1],p[2],p[3],p[4] )

def p_parameter(p):
    '''
    parameter : simple_type ID add_parameter parameter2
    '''
    # Add var to memory map
    virtual_address = memLocal.addVar(p[2], p[1])

    # Check if virtual address is in valid range
    if virtual_address is None:
        raise yacc.YaccError(f"Stack overflow!")
    
    # Add param as var and check if param is not already declared within function
    if (functionTable.add_var_to_function(curr.getScope(), p[2], p[1], virtual_address) is None):
        raise yacc.YaccError(f"Variable {p[2]} already declared")

    # Update function's resources
    functionTable.set_resources_to_function(curr.getScope(), 'var ' + p[1])
    
    p[0] = ('parameter',p[1],p[2],p[3])

def p_add_parameter(p):
    "add_parameter :"
    functionTable.add_param_types_to_function(curr.getScope(), p[-2])

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
    var_cte : PLUS CTE_INT add_constant_int
       | PLUS CTE_FLOAT add_constant_float
       | MINUS CTE_INT add_neg_constant_int
       | MINUS CTE_FLOAT add_neg_constant_float
       | CTE_INT add_constant_int
       | CTE_FLOAT add_constant_float
       | CTE_CHAR add_constant_char
    '''
    if (len(p) == 3):
        p[0] = p[1] 

def p_add_constant_int(p):
    "add_constant_int :"
    #check if constant already declared
    if (constantsTable.get_var_type(p[-1]) == None):
        # Add to constants' memory map 
        virtual_address = memConstants.addVar(p[-1], 'int')

        # Check if virtual address is in valid range
        if virtual_address is None:
            raise yacc.YaccError(f"Stack overflow!")
    
        constantsTable.add_var(p[-1], 'int', virtual_address)

        quadruples.stack_operands.append(virtual_address)
        quadruples.stack_types.append('int')
    else:
        quadruples.stack_operands.append(constantsTable.get_var_dirVir(p[-1]))
        quadruples.stack_types.append('int')

def p_add_constant_float(p):
    "add_constant_float :"
    # Add to constants' memory map 
    virtual_address = memConstants.addVar(p[-1], 'float')

    # Check if virtual address is in valid range
    if virtual_address is None:
        raise yacc.YaccError(f"Stack overflow!")
    
    constantsTable.add_var(p[-1], 'float', virtual_address)

    quadruples.stack_operands.append(virtual_address)
    quadruples.stack_types.append('float')

def p_add_neg_constant_int(p):
    "add_neg_constant_int :"
    # Add to constants' memory map 
    virtual_address = memConstants.addVar(str(int(p[-1])*-1), 'int')

    # Check if virtual address is in valid range
    if virtual_address is None:
        raise yacc.YaccError(f"Stack overflow!")
    
    constantsTable.add_var(str(int(p[-1])*-1), 'int', virtual_address)

    quadruples.stack_operands.append(virtual_address)
    quadruples.stack_types.append('int')
    p[0] = str(int(p[-1])*-1)

def p_add_neg_constant_float(p):
    "add_neg_constant_float :"
    # Add to constants' memory map 
    virtual_address = memConstants.addVar(str(float(p[-1])*-1), 'float')

    # Check if virtual address is in valid range
    if virtual_address is None:
        raise yacc.YaccError(f"Stack overflow!")
    
    constantsTable.add_var(str(float(p[-1])*-1), 'float', virtual_address)

    quadruples.stack_operands.append(virtual_address)
    quadruples.stack_types.append('float')
    p[0] = str(float(p[-1])*-1)

def p_add_constant_char(p):
    "add_constant_char :"
    # Add to constants' memory map 
    virtual_address = memConstants.addVar(p[-1], 'char')

    # Check if virtual address is in valid range
    if virtual_address is None:
        raise yacc.YaccError(f"Stack overflow!")
    
    constantsTable.add_var(p[-1], 'char', virtual_address)

    quadruples.stack_operands.append(virtual_address)
    quadruples.stack_types.append('char')

def p_super_expression(p):
    '''
    super_expression : expression super_expression2
    '''
    p[0] = ('super_expression',p[1],p[2])

def p_super_expression2(p):
    '''
    super_expression2 : super_expression3 push_operator expression check_for_boolean_op
       | empty
    '''
    if (len(p) == 3):
     p[0] = ('super_expression2',p[1],p[2])
    else:
        p[0] = p[1] 

def p_super_expression3(p):
    '''
    super_expression3 : AND
       | OR
    '''
    p[0] = p[1]

def p_check_for_boolean_op(p):
    "check_for_boolean_op :"
    # Check that fake bottom (-1) does not exist
    if (len(quadruples.stack_operators) > 0 and quadruples.stack_operators[-1] != '-1'):
        # If i have a boolean operator pending
        if (quadruples.stack_operators[-1] == 'and' or quadruples.stack_operators[-1] == 'or'):
            right_operand = quadruples.stack_operands.pop()
            right_type = quadruples.stack_types.pop()

            left_operand = quadruples.stack_operands.pop()
            left_type = quadruples.stack_types.pop()

            operator = quadruples.stack_operators.pop()

            result_type = semanticCube.get_result_type(operator, left_type, right_type)

            if (result_type is None):
                raise yacc.YaccError(f"Type mismatch!")
            else:
                # Generate quad
                temporal = 't' + str(quadruples.get_temporal_counter())

                # Add temporal to memory map
                virtual_address = memTemporal.addVar(temporal, result_type)

                # Check if is in range
                if virtual_address is None:
                    raise yacc.YaccError(f"Stack overflow!")

                quad = [operator, left_operand, right_operand, virtual_address]
                quadruples.quadruples.append(quad)

                quadruples.stack_operands.append(virtual_address)
                quadruples.stack_types.append(result_type)
                quadruples.increment_counter()

                # Update function's resources
                functionTable.set_resources_to_function(curr.getScope(), 'temp ' + result_type)

def p_expression(p):
    '''
    expression : exp expression2
    '''
    p[0] = ('expression',p[1],p[2])

def p_expression2(p):
    '''
    expression2 : expression3 push_operator exp check_for_relational_op
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
    p[0] = p[1]

def p_exp(p):
    '''
    exp : term check_for_sum_rest exp2
    '''
    p[0] = ('exp',p[1],p[2])

def p_check_for_relational_op(p):
    "check_for_relational_op :"
    # Check that fake bottom (-1) does not exist
    if (len(quadruples.stack_operators) > 0 and quadruples.stack_operators[-1] != '-1'):
        # If i have a relational operator pending
        if (quadruples.stack_operators[-1] == '<' or quadruples.stack_operators[-1] == '>'
            or quadruples.stack_operators[-1] == '<>' or quadruples.stack_operators[-1] == '=='):

            right_operand = quadruples.stack_operands.pop()
            right_type = quadruples.stack_types.pop()

            left_operand = quadruples.stack_operands.pop()
            left_type = quadruples.stack_types.pop()

            operator = quadruples.stack_operators.pop()

            result_type = semanticCube.get_result_type(operator, left_type, right_type)

            if (result_type is None):
                raise yacc.YaccError(f"Type mismatch!")
            else:
                # Generate quad
                temporal = 't' + str(quadruples.get_temporal_counter())

                # Add temporal to memory map
                virtual_address = memTemporal.addVar(temporal, result_type)

                # Check if is in range
                if virtual_address is None:
                    raise yacc.YaccError(f"Stack overflow!")
                
                quad = [operator, left_operand, right_operand, virtual_address]
                quadruples.quadruples.append(quad)

                quadruples.stack_operands.append(virtual_address)
                quadruples.stack_types.append(result_type)
                quadruples.increment_counter()

                # Update function's resources
                functionTable.set_resources_to_function(curr.getScope(), 'temp ' + result_type)

def p_check_for_sum_rest(p):
    "check_for_sum_rest :"
    # Check that fake bottom (-1) does not exist
    if (len(quadruples.stack_operators) > 0 and quadruples.stack_operators[-1] != '-1'):
        # If i have a sum or substraction pending
        if ((quadruples.stack_operators[-1] == '+' or quadruples.stack_operators[-1] == '-')):

            right_operand = quadruples.stack_operands.pop()
            right_type = quadruples.stack_types.pop()

            left_operand = quadruples.stack_operands.pop()
            left_type = quadruples.stack_types.pop()

            operator = quadruples.stack_operators.pop()

            result_type = semanticCube.get_result_type(operator, left_type, right_type)

            if (result_type is None):
                raise yacc.YaccError(f"Type mismatch!")
            else:
                # Generate quad
                temporal = 't' + str(quadruples.get_temporal_counter())

                # Add temporal to memory map
                virtual_address = memTemporal.addVar(temporal, result_type)

                # Check if is in range
                if virtual_address is None:
                    raise yacc.YaccError(f"Stack overflow!")
                
                quad = [operator, left_operand, right_operand, virtual_address]
                quadruples.quadruples.append(quad)

                quadruples.stack_operands.append(virtual_address)
                quadruples.stack_types.append(result_type)
                quadruples.increment_counter()
            
                # Update function's resources
                functionTable.set_resources_to_function(curr.getScope(), 'temp ' + result_type)

def p_exp2(p):
    '''
    exp2 : PLUS push_operator exp
       | MINUS push_operator exp
       | empty
    '''
    if (len(p) == 3):
     p[0] = ('exp2',p[1],p[2])
    else:
        p[0] = p[1] 

def p_term(p):
    '''
    term : factor check_for_mult_div term2
    '''
    p[0] = ('term',p[1],p[2])

def p_check_for_mult_div(p):
    "check_for_mult_div :"
    # Check that fake bottom (-1) does not exist
    if (len(quadruples.stack_operators) > 0 and quadruples.stack_operators[-1] != '-1'):
        # If i have a multiplication or division pending
        if ((quadruples.stack_operators[-1] == '*' or quadruples.stack_operators[-1] == '/')):

            right_operand = quadruples.stack_operands.pop()
            right_type = quadruples.stack_types.pop()

            left_operand = quadruples.stack_operands.pop()
            left_type = quadruples.stack_types.pop()

            operator = quadruples.stack_operators.pop()

            result_type = semanticCube.get_result_type(operator, left_type, right_type)

            if (result_type is None):
                raise yacc.YaccError(f"Type mismatch!")
            else:
                # Generate quad
                temporal = 't' + str(quadruples.get_temporal_counter())

                # Add temporal to memory map
                virtual_address = memTemporal.addVar(temporal, result_type)

                # Check if is in range
                if virtual_address is None:
                    raise yacc.YaccError(f"Stack overflow!")
                
                quad = [operator, left_operand, right_operand, virtual_address]
                quadruples.quadruples.append(quad)

                quadruples.stack_operands.append(virtual_address)
                quadruples.stack_types.append(result_type)
                quadruples.increment_counter()

                # Update function's resources
                functionTable.set_resources_to_function(curr.getScope(), 'temp ' + result_type)

def p_term2(p):
    '''
    term2 : TIMES push_operator term
       | DIVIDE push_operator term
       | empty
    '''
    if (len(p) == 3):
     p[0] = ('term2',p[1],p[2])
    else:
        p[0] = p[1] 

def p_push_operator(p):
    "push_operator :"
    quadruples.stack_operators.append(p[-1])

def p_factor(p):
    '''
    factor : LPAREN add_fake_bottom super_expression RPAREN remove_fake_bottom
           | var_cte 
           | variable push_operand
           | call
    '''
    if (len(p) == 4):
        p[0] = ('factor',p[1],p[2],p[3])
    else:
        p[0] = ('factor',p[1])

def p_add_fake_bottom(p):
    "add_fake_bottom :"
    quadruples.stack_operators.append('-1')

def p_remove_fake_bottom(p):
    "remove_fake_bottom :"
    quadruples.stack_operators.pop()

def p_push_operand(p):
    "push_operand :"

    # Check var is declared locally to push it, if not, check global. if not either, error undeclared var
    if (functionTable.get_var_type_in_function(curr.getScope(), p[-1]) != None):
        dirVir = functionTable.get_var_dirVir_in_function(curr.getScope(), p[-1])
        type = functionTable.get_var_type_in_function(curr.getScope(), p[-1])

        quadruples.stack_operands.append(dirVir)
        quadruples.stack_types.append(type)

    elif (functionTable.get_var_type_in_function('main', p[-1]) != None):
        dirVir = functionTable.get_var_dirVir_in_function('main', p[-1])
        type = functionTable.get_var_type_in_function('main', p[-1])

        quadruples.stack_operands.append(dirVir)
        quadruples.stack_types.append(type)

    else :
        raise yacc.YaccError(f"Variable {p[-1]} is not declared locally nor globally")


def p_variable(p):
    '''
    variable : ID variable2
    '''
    p[0] = p[1]
    # Verify id exists in current scope or global scope
    if ((functionTable.get_var_type_in_function(curr.getScope(), p[1]) is None) and (functionTable.get_var_type_in_function('main', p[1]) is None)):
        raise yacc.YaccError(f"Variable {p[1]} is not declared")
    

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
    call : ID verify_function_exists call2 add_gosub
       | ID call3
    '''
    # Pop paramCounter from stack since we have finished with all args of curr call
    curr.resetParamCounter()

    p[0] = ('call',p[1],p[2] )

def p_verify_function_exists(p):
    "verify_function_exists :"

    # Verify that function exists in function table
    if (functionTable.get_function(p[-1]) is None):
        raise yacc.YaccError(f"Function {p[-1]} not declared")

    # Get params' table of function being called
    curr.setParamTypesList(functionTable.get_params_types_of_function(p[-1]))
    
    # Generate ERA quad
    quad = ['ERA', '', '', p[-1]]
    quadruples.quadruples.append(quad)

    # Push to stack new paramCounter equal to 0
    curr.addParamCounter()

def p_call2(p):
    '''
    call2 : LPAREN call4 RPAREN
    '''
    # Verify parameter counter matches the parameter list's size
    param_list = curr.getParamTypesList()
    if (curr.getParamCounter() != len(param_list)):
        raise yacc.YaccError('Arguments number do not match')

    p[0] = ('call2',p[1],p[2],p[3] )

def p_call4(p):
    '''
    call4 : exp verify_argument call5
     | empty
    '''
    if (len(p) == 3):
        p[0] = ('call4',p[1],p[2])
    else:
        p[0] = ('call4',p[1])

def p_verify_argument(p):
    "verify_argument :"
    expr_type = quadruples.stack_types.pop()
    expression = quadruples.stack_operands.pop()

    # Verify argument type against parameter K in parameter table
    expected_arg_type = curr.getParamTypeInIndex(curr.getParamCounter())
    
    if (expected_arg_type is None):
        raise yacc.YaccError('Too many arguments')
    
    if (expected_arg_type != expr_type):
            raise yacc.YaccError('Argument type do not match')

    # Add PARAM quad
    quad = ['PARAM', expression, '', curr.getParamCounter()]
    quadruples.quadruples.append(quad)

    # Increment parameter counter
    curr.incrementParamCounter()        

def p_call5(p):
    '''
    call5 : COMMA call4
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

def p_add_gosub(p):
    "add_gosub :"

    # Generate GOSUB quadruple
    quad = ['GOSUB', '', '', p[-3]]
    quadruples.quadruples.append(quad)

    temporal = 't' + str(quadruples.get_temporal_counter())
    result_type = functionTable.get_returnType_of_function(p[-3])

    # Add temporal to memory map
    virtual_address_temporal = memTemporal.addVar(temporal, result_type)

    # Check if is in range
    if virtual_address_temporal is None:
        raise yacc.YaccError(f"Stack overflow!")

    # Virtual address of var with same name as function
    virtual_address_of_var = functionTable.get_var_dirVir_in_function('main', p[-3])
    
    # Parche de recursion / Snapshot
    if result_type != 'void':
        quad = ['=', virtual_address_of_var, '', virtual_address_temporal]
        quadruples.quadruples.append(quad)

    quadruples.stack_types.append(result_type)
    quadruples.stack_operands.append(virtual_address_temporal)

    # Increment temporal counter
    quadruples.increment_counter()
    
    # Update function's resources
    functionTable.set_resources_to_function(curr.getScope(), 'temp ' + result_type)

def p_condition(p):
    '''
    condition : IF LPAREN super_expression RPAREN add_gotof block condition2 solve_pending_jump
    '''
    p[0] = ('condition',p[1],p[2],p[3],p[4],p[5],p[6])

def p_condition2(p):
    '''
    condition2 : ELSE add_goto block
       | empty
    '''
    if (len(p) == 3):
     p[0] = ('condition2',p[1],p[2])
    else:
        p[0] = p[1] 

def p_add_gotof(p):
    "add_gotof :"
    expr_type = quadruples.stack_types.pop()
    expression = quadruples.stack_operands.pop()

    if expr_type != 'bool':
        raise yacc.YaccError(f"If requires a boolean expression!")
    else:
        # Generate quadruple
        quad = ['GOTOF', expression, '', '']
        quadruples.quadruples.append(quad)
        quadruples.stack_jumps.append(len(quadruples.quadruples) - 1)

def p_add_goto(p):
    "add_goto :"
    pending_jump = quadruples.stack_jumps.pop()

    # Generate quadruple
    quad = ['GOTO', '', '', '']
    quadruples.quadruples.append(quad)

    # I do not know where that GOTO needs to go, so in the mean time push it to jump' stack
    quadruples.stack_jumps.append(len(quadruples.quadruples) - 1)

    # Solve pending jump
    quadruples.quadruples[pending_jump][3] = len(quadruples.quadruples)

def p_solve_pending_jump_main(p):
    "solve_pending_jump_main :"
    pending_jump = quadruples.stack_jumps.pop()

    # Solve pending jump
    quadruples.quadruples[pending_jump][3] = len(quadruples.quadruples)

    # Reset temporal counter so another function can use them
    quadruples.reset_temporal_counter()

    # Reset memory map
    memTemporal.resetMemoryMap()

def p_solve_pending_jump(p):
    "solve_pending_jump :"
    pending_jump = quadruples.stack_jumps.pop()

    # Solve pending jump
    quadruples.quadruples[pending_jump][3] = len(quadruples.quadruples)

def p_writing(p):
    '''
    writing : PRINT LPAREN writing2 RPAREN SEMIC
    '''
    p[0] = ('writing',p[1],p[2],p[3],p[4],p[5])

def p_writing2(p):
    '''
    writing2 : CTE_STR push_str_operand generate_quad writing3
            | super_expression generate_quad writing3
    '''
    p[0] = ('writing2',p[1])

def p_writing3(p):
    '''
    writing3 : COMMA writing2
            | empty
    '''
    p[0] = ('writing3',p[1])

def p_push_str_operand(p):
    "push_str_operand :"

    # Push str operand (id and type)
    quadruples.stack_operands.append(p[-1])
    quadruples.stack_types.append("string")

def p_generate_quad(p):
    "generate_quad :"

    # Generate quadruple
    result = quadruples.stack_operands.pop()
    quad = ['PRINT', '', '', result]
    quadruples.quadruples.append(quad)

    quadruples.stack_types.pop()

def p_return(p):
    '''
    return : RETURN super_expression ret_ver_supexp
    '''
    #redundancy check ,if we are in a void func and validate NOT TO RETURN anything
    if(functionTable.get_var_type_in_function('main',curr.getScope() )=="void"):
        raise yacc.YaccError("Error, void function should not have a return statement")
    

    p[0] = ('return',p[1],p[2])
    
def p_ret_ver_supexp(p):
    "ret_ver_supexp :"
    expected_return_type = functionTable.get_var_type_in_function('main',curr.getScope() ) 
    #print(expected_return_type)
    if( expected_return_type == None):
        raise yacc.YaccError("Error, void function should not have a return statement")
    
    # Verify super expression type against scope type
    if ( quadruples.stack_types.pop() != expected_return_type):
        raise yacc.YaccError("return-type mismatch")
    
    func_name = curr.getScope()
    quad = ["RETURN", func_name, '', quadruples.stack_operands.pop()]
    quadruples.quadruples.append(quad)

#-----loop
def p_loop(p):
    '''
    loop : WHILE while_breadcrumb LPAREN super_expression RPAREN while_gotof block while_pending_jump
    '''
    p[0] = ('loop',p[1],p[2],p[3],p[4],p[5])

def p_while_breadcrumb(p):
    "while_breadcrumb :"
    quadruples.stack_jumps.append(len(quadruples.quadruples))

def p_while_gotof(p):
    "while_gotof :"
    expr_type = quadruples.stack_types.pop()
    expression = quadruples.stack_operands.pop()

    if expr_type != 'bool':
        raise yacc.YaccError(f"While requires a boolean expression!")
    else:
        # Generate quadruple
        quad = ['GOTOF', expression, '', '']
        quadruples.quadruples.append(quad)
        #breadcrunb to fill gotoF later
        quadruples.stack_jumps.append(len(quadruples.quadruples) - 1)

def p_while_pending_jump(p):
    "while_pending_jump :"
    end = quadruples.stack_jumps.pop()
    return_to_while = quadruples.stack_jumps.pop()
    # Generate GOTO quadruple
    quad = ['GOTO', '', '', return_to_while]
    quadruples.quadruples.append(quad)
    # Solve pending jump; what comes after the while
    quadruples.quadruples[end][3] = len(quadruples.quadruples)

#-----loop
def p_input(p):
    '''
    input : INPUT LPAREN variable RPAREN SEMIC
    '''
    # dynamic semantic on variable
    #generate quad
    instruction = p[1]
    input_var = p[3]
    quad = [instruction, input_var, ' ',' ']
    quadruples.quadruples.append(quad)
    quadruples.increment_counter()

    p[0] = ('input',p[1],p[2],p[3],p[4],p[5]) 

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
    if p:
        print(f'Syntax error in {p.value}')
    raise SyntaxError('Syntax Error')

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