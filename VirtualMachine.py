from MemoryMap import *

class VirtualMachine:
    def __init__(self, quadruples, memConstants, functionTable, memGlobal, classTable):
        self.quadruples = quadruples
        self.functionTable = functionTable
        self.memGlobal = memGlobal
        self.memConstants = memConstants
        self.classTable = classTable
        self.executedQuads =[]

        # Stack of memories (temporal and local)
        self.memTemp = []
        self.currMem = []
        self.global_stack = []
        self.isBetweenEraGosub = False

        self.initMainMem()
        self.executeVM()
        #self.printExecutedQuads()
    
    def initMainMem(self):
        self.global_stack.append(MemoryMap(1000, 2000, 3000, 4000, 5000))
        self.memTemp.append(MemoryMap(20000, 21000, 22000, 23000, 24000))
        resources = self.functionTable.get_resources_in_function('main')
        
        for i in range(len(resources)):
            if i == 0:
                for x in range(resources[i]):
                    self.global_stack[-1].addVar('defaultName', 'int')
            elif i == 1:
                for x in range(resources[i]):
                    self.global_stack[-1].addVar('defaultName', 'float')
            elif i == 2:
                for x in range(resources[i]):
                    self.global_stack[-1].addVar('defaultName', 'bool')
            elif i == 3:
                for x in range(resources[i]):
                    self.global_stack[-1].addVar('defaultName', 'char')
            elif i == 4:
                for x in range(resources[i]):
                    self.memTemp[-1].addVar('defaultName','int')
            elif i == 5:
                for x in range(resources[i]):
                    self.memTemp[-1].addVar('defaultName','float')
            elif i == 6:
                for x in range(resources[i]):
                    self.memTemp[-1].addVar('defaultName','bool')
            elif i == 7:
                for x in range(resources[i]):
                    self.memTemp[-1].addVar('defaultName','char')


    def printExecutedQuads(self):
        print("-------------------START QUADRUPLE EXECUTION ORDER------------------")
        for index, quad in enumerate(self.executedQuads):
            print(quad)
        print("-------------------END QUADRUPLE EXECUTION ORDER------------------")
            
    def executeVM(self):
        instruction_pointer = 0
        stack_migajas = []
        seenReturn = False

        while instruction_pointer < len(self.quadruples) - 1:
            #save the order of executed quads
            self.executedQuads.append(self.quadruples[instruction_pointer])
            op_code = self.quadruples[instruction_pointer][0]
            left_op_dir = self.quadruples[instruction_pointer][1]
            right_op_dir = self.quadruples[instruction_pointer][2]
            store_in_dir = self.quadruples[instruction_pointer][3]

            # print(op_code)

            if seenReturn and op_code != 'ENDFUNC':
                instruction_pointer += 1
                continue

            if op_code == 'PRINT':
                if store_in_dir == 'endl':
                    print('')
                elif isinstance(store_in_dir, str) and not store_in_dir.startswith("(") and not store_in_dir.endswith(")"):
                    print(store_in_dir, end=' ')
                else:
                    result = self.getValueInMemory(store_in_dir)
                    print(result, end=' ')
                instruction_pointer += 1

            elif op_code == '=':
                left_op = self.getValueInMemory(left_op_dir)
                self.assignValue(store_in_dir, left_op)

                instruction_pointer += 1

            elif op_code =='input':
                newVal = input("-->")
                self.assignValue(left_op_dir, newVal)

                instruction_pointer += 1

            elif op_code == '+':
                left_op = self.getValueInMemory(left_op_dir)
                right_op = self.getValueInMemory(right_op_dir)
                result = left_op + right_op
                self.assignValue(store_in_dir, result)

                instruction_pointer += 1

            elif op_code == '*':
                left_op = self.getValueInMemory(left_op_dir)
                right_op = self.getValueInMemory(right_op_dir)
                result = left_op * right_op
                self.assignValue(store_in_dir, result)

                instruction_pointer += 1

            elif op_code == '-':
                left_op = self.getValueInMemory(left_op_dir)
                right_op = self.getValueInMemory(right_op_dir)
                result = left_op - right_op
                self.assignValue(store_in_dir, result)

                instruction_pointer += 1

            elif op_code == '/':
                left_op = self.getValueInMemory(left_op_dir)
                right_op = self.getValueInMemory(right_op_dir)
                result = left_op / right_op
                self.assignValue(store_in_dir, result)

                instruction_pointer += 1

            elif op_code == '>':
                left_op = self.getValueInMemory(left_op_dir)
                right_op = self.getValueInMemory(right_op_dir)
                self.assignValue(store_in_dir, left_op > right_op)

                instruction_pointer += 1

            elif op_code == '<':
                left_op = self.getValueInMemory(left_op_dir)
                right_op = self.getValueInMemory(right_op_dir)
                self.assignValue(store_in_dir, left_op < right_op)

                instruction_pointer += 1

            elif op_code == '>=':
                left_op = self.getValueInMemory(left_op_dir)
                right_op = self.getValueInMemory(right_op_dir)
                self.assignValue(store_in_dir, left_op >= right_op)

                instruction_pointer += 1

            elif op_code == '<=':
                left_op = self.getValueInMemory(left_op_dir)
                right_op = self.getValueInMemory(right_op_dir)
                self.assignValue(store_in_dir, left_op <= right_op)

                instruction_pointer += 1

            elif op_code == '==':
                left_op = self.getValueInMemory(left_op_dir)
                right_op = self.getValueInMemory(right_op_dir)
                self.assignValue(store_in_dir, left_op == right_op)

                instruction_pointer += 1

            elif op_code == '<>':
                left_op = self.getValueInMemory(left_op_dir)
                right_op = self.getValueInMemory(right_op_dir)
                self.assignValue(store_in_dir, left_op != right_op)

                instruction_pointer += 1

            elif op_code == 'and':
                left_op = self.getValueInMemory(left_op_dir)
                right_op = self.getValueInMemory(right_op_dir)
                self.assignValue(store_in_dir, left_op and right_op)

                instruction_pointer += 1

            elif op_code == 'or':
                left_op = self.getValueInMemory(left_op_dir)
                right_op = self.getValueInMemory(right_op_dir)
                self.assignValue(store_in_dir, left_op or right_op)

                instruction_pointer += 1

            elif op_code == 'GOTO':
                instruction_pointer = store_in_dir
            
            elif op_code == 'GOTOF':
                left_op = self.getValueInMemory(left_op_dir)
                if left_op == False:
                    instruction_pointer = store_in_dir
                else:
                    instruction_pointer += 1

            elif op_code == 'GOSUB':
                stack_migajas.append(instruction_pointer + 1)
                
                if right_op_dir == '':
                    # Quadruple number where function being called starts
                    quad_no = self.functionTable.get_dirVir(store_in_dir)
                else:
                    quad_no = self.classTable.get_dirVir_in_function(right_op_dir, store_in_dir)

                instruction_pointer = quad_no
                self.isBetweenEraGosub = False

            elif op_code == 'ENDFUNC':
                '''
                Function ends and we want to check that a return was seen if function's type is not void
                IP is set to migaja (quadruple where we left off)
                '''
                # We finished executing this function, return to the breadcrumb now
                if right_op_dir == '':
                    function_type = self.functionTable.get_returnType_of_function(store_in_dir)
                    instruction_pointer = stack_migajas.pop()
                else:
                    function_type = self.classTable.get_returnType_of_function(right_op_dir, store_in_dir)
                    instruction_pointer = stack_migajas.pop()

                # if function_type != 'void': TODO add back with validation for functions in classes
                #     # Virtual address of var with same name as function
                #     dirvir = self.functionTable.get_var_dirVir_in_function('main', store_in_dir)
                #     dirvir_value = self.getValueInMemory(dirvir)

                #     # Check that a return was seen => var with same name as function is not 0
                #     if dirvir_value == None: # TODO NONE assignment
                #         raise KeyError("Function needs a return statement")
                    
                # We must delete the current working memory to use the previous one in the stack! This helps control the flow of
                # active memory and passive memory
                self.memTemp.pop()
                self.currMem.pop()

                seenReturn = False
            
            elif op_code == 'RETURN':
                '''
                Return sets the variable (with same name as function's) equal to the value being returned
                '''
                # Virtual address of var with same name as function
                dirvir = self.functionTable.get_var_dirVir_in_function('main', left_op_dir)

                # Value that needs to be assigned to var above
                store_dir_value = self.getValueInMemory(store_in_dir)

                self.assignValue(dirvir, store_dir_value)

                instruction_pointer += 1

                seenReturn = True

            elif op_code == "ERA":
                '''
                Creates memory by pushing an instance of "current" working memory and a temporal instance as well.
                The stacking of these resolves the active memory and "sleeping" memory
                '''
                self.memTemp.append(MemoryMap(20000, 21000, 22000, 23000,24000))
                self.currMem.append(MemoryMap(15000,16000,17000,18000,19000))

                if right_op_dir == '':
                    # Find the function and allocate memory based on resources
                    resources = self.functionTable.get_resources_in_function(store_in_dir)
                else:
                    resources = self.classTable.get_resources_of_function_in_class(right_op_dir, store_in_dir)
                
                for i in range(len(resources)):
                    if i == 0:
                        for x in range(resources[i]):
                            self.currMem[-1].addVar('defaultName','int')
                    elif i == 1:
                        for x in range(resources[i]):
                            self.currMem[-1].addVar('defaultName','float')
                    elif i == 2:
                        for x in range(resources[i]):
                            self.currMem[-1].addVar('defaultName','bool')
                    elif i == 3:
                        for x in range(resources[i]):
                            self.currMem[-1].addVar('defaultName','char')
                    elif i == 4:
                        for x in range(resources[i]):
                            self.memTemp[-1].addVar('defaultName','int')
                    elif i == 5:
                        for x in range(resources[i]):
                            self.memTemp[-1].addVar('defaultName','float')
                    elif i == 6:
                        for x in range(resources[i]):
                            self.memTemp[-1].addVar('defaultName','bool')
                    elif i == 7:
                        for x in range(resources[i]):
                            self.memTemp[-1].addVar('defaultName','char')

                self.isBetweenEraGosub = True
                instruction_pointer +=1
            
            elif op_code == 'PARAM':
                '''
                Set PARAM equal to the expression sent
                '''
                left_op = self.getValueInMemory(left_op_dir)

                self.isBetweenEraGosub = False
                self.assignValue(store_in_dir, left_op)
                self.isBetweenEraGosub = True
                
                instruction_pointer += 1

            elif op_code == 'VERIFY':
                left_op = self.getValueInMemory(left_op_dir)
                
                if left_op < right_op_dir or left_op > store_in_dir:
                    raise KeyError("Index out of bounds!")
                
                instruction_pointer += 1
            
            elif op_code == 'ERACLASS':
                memory = self.functionTable.get_resources_of_var_in_function('main', store_in_dir)
                self.global_stack.append(memory)

                self.memTemp.append(MemoryMap(20000, 21000, 22000, 23000,24000))
                resources = self.classTable.get_resources_in_class(right_op_dir)
                
                for i in range(len(resources)):
                    if i == 4:
                        for x in range(resources[i]):
                            self.memTemp[-1].addVar('defaultName','int')
                    elif i == 5:
                        for x in range(resources[i]):
                            self.memTemp[-1].addVar('defaultName','float')
                    elif i == 6:
                        for x in range(resources[i]):
                            self.memTemp[-1].addVar('defaultName','bool')
                    elif i == 7:
                        for x in range(resources[i]):
                            self.memTemp[-1].addVar('defaultName','char')

                instruction_pointer += 1
            
            elif op_code == 'ENDCLASS':
                self.global_stack.pop()
                self.memTemp.pop()
                instruction_pointer += 1

            else:
                instruction_pointer += 1

    
    def getValueInMemory(self, dir):
        index = -2 if self.isBetweenEraGosub else -1

        # Check if the direction has parentheses around it
        if isinstance(dir, str) and dir.startswith("(") and dir.endswith(")"):
            # Remove the parentheses and get the inner direction
            inner_dir = int(dir[1:-1])

            # Perform additional lookups in the memory
            value = self.getValueInMemory(inner_dir)
            value = self.getValueInMemory(value)

            return value

        # Global memory map
        if dir >= 1000 and dir < 2000:
            return int(self.global_stack[-1].int[dir - 1000])
        elif dir >= 2000 and dir < 3000:
            return float(self.global_stack[-1].float[dir - 2000])
        elif dir >= 3000 and dir < 4000:
            return self.global_stack[-1].char[dir - 3000]
        elif dir >= 4000 and dir < 5000:
            return self.global_stack[-1].bool[dir - 4000]
        elif dir >= 5000 and dir < 6000:
            return self.global_stack[-1].compound[dir - 5000]
        
        #Temporal memory map 
        elif dir >= 20000 and dir < 21000:
            return int(self.memTemp[index].int[dir - 20000])
        elif dir >= 21000 and dir < 22000:
            return float(self.memTemp[index].float[dir - 21000])
        elif dir >= 22000 and dir < 23000:
            return self.memTemp[index].char[dir - 22000]
        elif dir >= 23000 and dir < 24000:
            return self.memTemp[index].bool[dir - 23000]
        elif dir >= 24000 and dir < 25000:
            return self.memTemp[index].compound[dir - 24000]

        # Constant's memory map
        elif dir >= 25000 and dir < 26000:
            return int(self.memConstants.int[dir - 25000])
        elif dir >= 26000 and dir < 27000:
            return float(self.memConstants.float[dir - 26000])
        elif dir >= 27000 and dir < 28000:
            return self.memConstants.char[dir - 27000]
        elif dir >= 28000 and dir < 29000:
            return self.memConstants.bool[dir - 28000]

        # Local memory map 
        elif dir >= 15000 and dir < 16000:
            return int(self.currMem[index].int[dir - 15000])
        elif dir >= 16000 and dir < 17000:
            return float(self.currMem[index].float[dir - 16000])
        elif dir >= 17000 and dir < 18000:
            return self.currMem[index].char[dir - 17000]
        elif dir >= 18000 and dir < 19000:
            return self.currMem[index].bool[dir - 18000]
        elif dir >= 19000 and dir < 20000:
            return self.currMem[index].compound[dir - 19000]


    def assignValue(self, dir, new_val):
        index = -2 if self.isBetweenEraGosub else -1

        if isinstance(dir, str) and dir.startswith("(") and dir.endswith(")"):
            # Remove the parentheses and get the inner direction
            dir = int(dir[1:-1])
            dir = self.getValueInMemory(dir)

        # Global memory map
        if dir >= 1000 and dir < 2000:
            self.global_stack[-1].int[dir - 1000] = new_val
        elif dir >= 2000 and dir < 3000:
            self.global_stack[-1].float[dir - 2000] = new_val
        elif dir >= 3000 and dir < 4000:
            self.global_stack[-1].char[dir - 3000] = new_val
        elif dir >= 4000 and dir < 5000:
            self.global_stack[-1].bool[dir - 4000] = new_val
        
        # Constant's memory map
        elif dir >= 25000 and dir < 26000:
            self.memConstants.int[dir - 25000] = new_val
        elif dir >= 26000 and dir < 27000:
            self.memConstants.float[dir - 26000] = new_val
        elif dir >= 27000 and dir < 28000:
            self.memConstants.char[dir - 27000] = new_val
        elif dir >= 28000 and dir < 29000:
            self.memConstants.bool[dir - 28000] = new_val

        #Temporal memory map 
        elif dir >= 20000 and dir < 21000:
            self.memTemp[index].int[dir - 20000] = new_val
        elif dir >= 21000 and dir < 22000:
            self.memTemp[index].float[dir - 21000] = new_val
        elif dir >= 22000 and dir < 23000:
            self.memTemp[index].char[dir - 22000] = new_val
        elif dir >= 23000 and dir < 24000:
            self.memTemp[index].bool[dir - 23000] = new_val
        elif dir >= 24000 and dir < 25000:
            self.memTemp[index].compound[dir - 24000] = new_val

        # Local memory map 
        elif dir >= 15000 and dir < 16000:
            self.currMem[index].int[dir - 15000] = new_val
        elif dir >= 16000 and dir < 17000:
            self.currMem[index].float[dir - 16000] = new_val
        elif dir >= 17000 and dir < 18000:
            self.currMem[index].char[dir - 17000] = new_val
        elif dir >= 18000 and dir < 19000:
            self.currMem[index].bool[dir - 18000] = new_val
        elif dir >= 19000 and dir < 20000:
            self.currMem[index].compound[dir - 19000] = new_val