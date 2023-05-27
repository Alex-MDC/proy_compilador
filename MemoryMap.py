class MemoryMap:
    def __init__(self, startDirInt, startDirFloat, startDirChar, startDirBool, startDirCompound,startDirPointers = None, isConstant = False):
        self.int = []
        self.float = []
        self.char = []
        self.bool = []
        self.compound = []
        self.pointers = []
        self.isConstant = isConstant

        self.startDirInt = startDirInt
        self.startDirFloat = startDirFloat
        self.startDirChar = startDirChar
        self.startDirBool = startDirBool
        self.startDirCompound = startDirCompound
        self.startDirPointers = startDirPointers
        #TODO adding of pointers

    def addVar(self, var_name, var_type):
        virtual_address = 0
        
        if var_type == 'int':
            self.int.append(var_name if self.isConstant else 0)
            virtual_address = (len(self.int) - 1) + self.startDirInt

            # Out of bounds error
            isInbounds = virtual_address >= self.startDirInt and virtual_address < self.startDirFloat
            if (isInbounds == False):
                return None

        elif var_type == 'float':
            self.float.append(var_name if self.isConstant else 0)
            virtual_address = (len(self.float) - 1) + self.startDirFloat

            # Out of bounds error
            isInbounds = virtual_address >= self.startDirFloat and virtual_address < self.startDirChar
            if (isInbounds == False):
                return None

        elif var_type == 'char':
            self.char.append(var_name if self.isConstant else 0)
            virtual_address = (len(self.char) - 1) + self.startDirChar
            
            # Out of bounds error
            isInbounds = virtual_address >= self.startDirChar and virtual_address < self.startDirBool
            if (isInbounds == False):
                return None
                
        elif var_type == 'id':
            self.compound.append(var_name if self.isConstant else 0)
            virtual_address = (len(self.compound) - 1) + self.startDirCompound

        elif var_type == 'bool':
            self.bool.append(var_name if self.isConstant else 0)
            virtual_address = (len(self.bool) - 1) + self.startDirBool
            # Out of bounds error
            isInbounds = virtual_address >= self.startDirBool and virtual_address < self.startDirCompound
            if (isInbounds == False):
                return None
            
        
        # Return virtual address
        return virtual_address

    def resetMemoryMap(self):
        self.int.clear()
        self.float.clear()
        self.char.clear()
        self.bool.clear()
        self.compound.clear()
        self.pointers.clear()

    def printMemoryMap(self):
        print(f"Int: {self.int}")
        print(f"Float: {self.float}")
        print(f"Char: {self.char}")
        print(f"Bool: {self.bool}")
        print(f"Compound: {self.compound}")
        print(f"Pointers: {self.pointers}")