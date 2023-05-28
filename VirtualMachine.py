from MemoryMap import *

class VirtualMachine:
    def __init__(self, quadruples, memConstants, functionTable, memGlobal):
        self.quadruples = quadruples
        self.functionTable = functionTable
        self.memGlobal = memGlobal
        self.memConstants = memConstants
        self.memTemp = []
        self.currMem = []
        self.initMainMem()
        self.executeVM()
    
    def initMainMem(self):
        self.currMem.append(MemoryMap(15000,16000,17000,18000,19000))
        self.memTemp.append(MemoryMap(20000, 21000, 22000, 23000,24000,29000))
        resources = self.functionTable.get_resources_in_function('main')
        
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
            elif i == 0:
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

            
                
    def executeVM(self):
        instruction_pointer = 0
        migaja = 0

        while instruction_pointer < len(self.quadruples) - 1:
            # print("CURRENT QUAD")
            # print(self.quadruples[instruction_pointer])
            op_code = self.quadruples[instruction_pointer][0]
            left_op_dir = self.quadruples[instruction_pointer][1]
            right_op_dir = self.quadruples[instruction_pointer][2]
            store_in_dir = self.quadruples[instruction_pointer][3]

            if op_code == 'PRINT':
                if isinstance(store_in_dir, str):
                    print(store_in_dir)
                else:
                    result = self.getValueInMemory(store_in_dir)
                    print(result)
                instruction_pointer += 1

            elif op_code == '=':
                left_op = self.getValueInMemory(left_op_dir)
                # print(self.memTemp)
                self.assignValue(store_in_dir, left_op)

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
                migaja = instruction_pointer + 1
                
                # Quadruple number where function being called starts
                quad_no = self.functionTable.get_dirVir(store_in_dir)
                instruction_pointer = quad_no

            elif op_code == 'ENDFUNC':
                '''
                Function ends and we want to check that a return was seen if function's type is not void
                IP is set to migaja (quadruple where we left off)
                '''
                #nothing should execute after ENDFUNC, we return to the breadcrumb now
                instruction_pointer = migaja

                function_type = self.functionTable.get_returnType_of_function(store_in_dir)

                if function_type != 'void':
                    # Virtual address of var with same name as function
                    dirvir = self.functionTable.get_var_dirVir_in_function('main', store_in_dir)
                    dirvir_value = self.getValueInMemory(dirvir)

                    # Check that a return was seen => var with same name as function is not 0
                    if dirvir_value == 0:
                        raise KeyError("Function needs a return statement")
                #We must delete the current working memory to use the next one in the stack! This helps control the flow of
                # active memory and passive memory
                self.memTemp.pop()
                self.currMem.pop()
            
            elif op_code == 'RETURN':
                '''
                Return sets the variable (with same name as function's) equal to the value being returned
                '''
                # Virtual address of var with same name as function
                dirvir = self.functionTable.get_var_dirVir_in_function('main', left_op_dir)

                # Value that needs to be assigned to var above
                store_dir_value = self.getValueInMemory(store_in_dir)

                self.assignValue(dirvir, store_dir_value)

                # Once a return was seen, the ENDFUNC should follow so nothing else executes. raise IP
                instruction_pointer += 1

            elif op_code == "ERA":
                '''
                Creates memory by pushing an instance of "current" working memory and a temporal instance as well.
                The stacking of these resolves the active memory and "sleeping" memory
                '''
                self.memTemp.append(MemoryMap(20000, 21000, 22000, 23000,24000,29000))
                self.currMem.append(MemoryMap(15000,16000,17000,18000,19000))
                #find the function and allocate memory based on resources
                resources = self.functionTable.get_resources_in_function(store_in_dir)
                
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
                    elif i == 0:
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
                
                #self.currMem[-1].printMemoryMap()

                instruction_pointer +=1
            
                
            else:
                instruction_pointer += 1

    
    def getValueInMemory(self, dir):
        # Global memory map
        if dir >= 1000 and dir < 2000:
            return int(self.memGlobal.int[dir - 1000])
        elif dir >= 2000 and dir < 3000:
            return float(self.memGlobal.float[dir - 2000])
        elif dir >= 3000 and dir < 4000:
            return self.memGlobal.char[dir - 3000]
        elif dir >= 4000 and dir < 5000:
            return self.memGlobal.bool[dir - 4000]
        elif dir >= 5000 and dir < 6000:
            return self.memGlobal.compound[dir - 5000]
        
        #Temporal memory map 
        elif dir >= 20000 and dir < 21000:
            return int(self.memTemp[-1].int[dir - 20000])
        elif dir >= 21000 and dir < 22000:
            return float(self.memTemp[-1].float[dir - 21000])
        elif dir >= 22000 and dir < 23000:
            return self.memTemp[-1].char[dir - 22000]
        elif dir >= 23000 and dir < 24000:
            return self.memTemp[-1].bool[dir - 23000]
        elif dir >= 24000 and dir < 25000:
            return self.memTemp[-1].compound[dir - 24000]
        elif dir >= 29000 and dir < 30000:
            return self.memTemp[-1].pointers[dir - 29000]

        # Constant's memory map
        elif dir >= 25000 and dir < 26000:
            return int(self.memConstants.int[dir - 25000])
        elif dir >= 26000 and dir < 27000:
            return float(self.memConstants.float[dir - 26000])
        elif dir >= 27000 and dir < 28000:
            return self.memConstants.char[dir - 27000]
        # elif dir >= 30000 and dir < 31000:
        #     return self.memConstants.bool[dir - 30000]


    def assignValue(self, dir, new_val):
        # Global memory map
        if dir >= 1000 and dir < 2000:
            self.memGlobal.int[dir - 1000] = new_val
        elif dir >= 2000 and dir < 3000:
            self.memGlobal.float[dir - 2000] = new_val
        elif dir >= 3000 and dir < 4000:
            self.memGlobal.char[dir - 3000] = new_val
        elif dir >= 4000 and dir < 5000:
            self.memGlobal.bool[dir - 4000] = new_val
        
        # Constant's memory map
        elif dir >= 25000 and dir < 26000:
            self.memConstants.int[dir - 25000] = new_val
        elif dir >= 26000 and dir < 27000:
            self.memConstants.float[dir - 26000] = new_val
        elif dir >= 27000 and dir < 28000:
            self.memConstants.char[dir - 27000] = new_val
        # elif dir >= 30000 and dir < 31000:
        #     self.memConstants.bool[dir - 30000] = left_op_dir

        #Temporal memory map 
        elif dir >= 20000 and dir < 21000:
            self.memTemp[-1].int[dir - 20000] = new_val
        elif dir >= 21000 and dir < 22000:
            self.memTemp[-1].float[dir - 21000] = new_val
        elif dir >= 22000 and dir < 23000:
            self.memTemp[-1].char[dir - 22000] = new_val
        elif dir >= 23000 and dir < 24000:
            self.memTemp[-1].bool[dir - 23000] = new_val
        elif dir >= 24000 and dir < 25000:
            self.memTemp[-1].compound[dir - 24000] = new_val
        elif dir >= 29000 and dir < 30000:
            self.memTemp[-1].pointers[dir - 29000] = new_val