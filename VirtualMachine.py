class VirtualMachine:
    def __init__(self, quadruples, memConstants, functionTable, memGlobal,memTemp):
        self.quadruples = quadruples
        self.functionTable = functionTable
        self.memGlobal = memGlobal
        self.memConstants = memConstants
        self.memTemp = memTemp

        self.executeVM()
    
    def executeVM(self):
        for i, quad in enumerate(self.quadruples):
            op_code = quad[0]
            left_op_dir = quad[1]
            right_op_dir = quad[2]
            store_in_dir = quad[3]

            if op_code == 'PRINT':
                if isinstance(store_in_dir, str):
                    print(store_in_dir)
                else:
                    result = self.getValueInMemory(store_in_dir)
                    print(result)

            elif op_code == '=':
                left_op = self.getValueInMemory(left_op_dir)
                self.assignValue(store_in_dir, left_op)

            elif op_code == '+':
                left_op = self.getValueInMemory(left_op_dir)
                right_op = self.getValueInMemory(right_op_dir)
                result = left_op + right_op
                self.assignValue(store_in_dir,result)

            elif op_code == '*':
                left_op = self.getValueInMemory(left_op_dir)
                right_op = self.getValueInMemory(right_op_dir)
                result = left_op * right_op
                self.assignValue(store_in_dir,result)

            elif op_code == '-':
                left_op = self.getValueInMemory(left_op_dir)
                right_op = self.getValueInMemory(right_op_dir)
                result = left_op - right_op
                self.assignValue(store_in_dir,result)

            elif op_code == '/':
                left_op = self.getValueInMemory(left_op_dir)
                right_op = self.getValueInMemory(right_op_dir)
                result = left_op / right_op
                self.assignValue(store_in_dir,result)

            elif op_code == '>':
                left_op = self.getValueInMemory(left_op_dir)
                right_op = self.getValueInMemory(right_op_dir)
                self.assignValue(store_in_dir,left_op > right_op)

            elif op_code == '<':
                left_op = self.getValueInMemory(left_op_dir)
                right_op = self.getValueInMemory(right_op_dir)
                self.assignValue(store_in_dir,left_op < right_op)

            elif op_code == '>=':
                left_op = self.getValueInMemory(left_op_dir)
                right_op = self.getValueInMemory(right_op_dir)
                self.assignValue(store_in_dir,left_op >= right_op)

            elif op_code == '<=':
                left_op = self.getValueInMemory(left_op_dir)
                right_op = self.getValueInMemory(right_op_dir)
                self.assignValue(store_in_dir,left_op <= right_op)

            elif op_code == '==':
                left_op = self.getValueInMemory(left_op_dir)
                right_op = self.getValueInMemory(right_op_dir)
                self.assignValue(store_in_dir,left_op == right_op)

            elif op_code == '<>':
                left_op = self.getValueInMemory(left_op_dir)
                right_op = self.getValueInMemory(right_op_dir)
                self.assignValue(store_in_dir,left_op != right_op)

            elif op_code == 'and':
                left_op = self.getValueInMemory(left_op_dir)
                right_op = self.getValueInMemory(right_op_dir)
                self.assignValue(store_in_dir,left_op and right_op)

            elif op_code == 'or':
                left_op = self.getValueInMemory(left_op_dir)
                right_op = self.getValueInMemory(right_op_dir)
                self.assignValue(store_in_dir,left_op or right_op)
                
    

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
            return int(self.memTemp.int[dir - 20000])
        elif dir >= 21000 and dir < 22000:
            return float(self.memTemp.float[dir - 21000])
        elif dir >= 22000 and dir < 23000:
            return self.memTemp.char[dir - 22000]
        elif dir >= 23000 and dir < 24000:
            return self.memTemp.bool[dir - 23000]
        elif dir >= 24000 and dir < 25000:
            return self.memTemp.compound[dir - 24000]
        elif dir >= 29000 and dir < 30000:
            return self.memTemp.pointers[dir - 29000]

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
            self.memTemp.int[dir - 20000] = new_val
        elif dir >= 21000 and dir < 22000:
            self.memTemp.float[dir - 21000] = new_val
        elif dir >= 22000 and dir < 23000:
            self.memTemp.char[dir - 22000] = new_val
        elif dir >= 23000 and dir < 24000:
            self.memTemp.bool[dir - 23000] = new_val
        elif dir >= 24000 and dir < 25000:
            self.memTemp.compound[dir - 24000] = new_val
        elif dir >= 29000 and dir < 30000:
            self.memTemp.pointers[dir - 29000] = new_val

        