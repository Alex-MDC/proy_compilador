class VirtualMachine:
    def __init__(self, quadruples, memConstants, functionTable, memGlobal):
        self.quadruples = quadruples
        self.functionTable = functionTable
        self.memGlobal = memGlobal
        self.memConstants = memConstants

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
                left_op_dir = self.getValueInMemory(left_op_dir)
                self.assignValue(store_in_dir, left_op_dir)
    

    def getValueInMemory(self, dir):
        # Global memory map
        if dir >= 1000 and dir < 2000:
            return self.memGlobal.int[dir - 1000]
        elif dir >= 2000 and dir < 3000:
            return self.memGlobal.float[dir - 2000]
        elif dir >= 3000 and dir < 4000:
            return self.memGlobal.char[dir - 3000]
        elif dir >= 4000 and dir < 5000:
            return self.memGlobal.bool[dir - 4000]
        elif dir >= 5000 and dir < 6000:
            return self.memGlobal.compound[dir - 5000]
        
        
        # Constant's memory map
        elif dir >= 25000 and dir < 26000:
            return self.memConstants.int[dir - 25000]
        elif dir >= 26000 and dir < 27000:
            return self.memConstants.float[dir - 26000]
        elif dir >= 27000 and dir < 28000:
            return self.memConstants.char[dir - 27000]
        # elif dir >= 30000 and dir < 31000:
        #     return self.memConstants.bool[dir - 30000]


    def assignValue(self, dir, left_op_dir):
        # Global memory map
        if dir >= 1000 and dir < 2000:
            self.memGlobal.int[dir - 1000] = left_op_dir
        elif dir >= 2000 and dir < 3000:
            self.memGlobal.float[dir - 2000] = left_op_dir
        elif dir >= 3000 and dir < 4000:
            self.memGlobal.char[dir - 3000] = left_op_dir
        elif dir >= 4000 and dir < 5000:
            self.memGlobal.bool[dir - 4000] = left_op_dir
        
        # Constant's memory map
        elif dir >= 25000 and dir < 26000:
            self.memConstants.int[dir - 25000] = left_op_dir
        elif dir >= 26000 and dir < 27000:
            self.memConstants.float[dir - 26000] = left_op_dir
        elif dir >= 27000 and dir < 28000:
            self.memConstants.char[dir - 27000] = left_op_dir
        # elif dir >= 30000 and dir < 31000:
        #     self.memConstants.bool[dir - 30000] = left_op_dir