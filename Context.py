class Context:
    def __init__(self):
        # Variable's type
        self.current_type = ''
        self.scope = []
        
        # For <call> diagram
        self.param_counter = []
        self.param_types_list = []

        # Operational codes
        self.op_codes = {
            '+' : 0,
            '-' : 1,
            '*' : 2,
            '/' : 3,
            '>' : 4,
            '<' : 5,
            '>=' : 6,
            '<=' : 7,
            '==' : 8,
            '<>' : 9,
            'ENDFUNC' : 10,
            'ENDPROG' : 11,
            'GOTO' : 12,
            'GOTOF' : 13,
            'ERA' : 14,
            'PARAM' : 15,
            'GOSUB' : 16,
            'PRINT' : 17,
            'RETURN' : 18,
            'INPUT' : 19
        }

    def setCurrType(self, curr):
        self.current_type = curr
    
    def getCurrType(self):
        return self.current_type

    def setScope(self, scope):
        self.scope.append(scope)

    def popScope(self):
        self.scope.pop()
    
    def getScope(self):
        return self.scope[-1]

    def addParamCounter(self):
        self.param_counter.append(0)
    
    def getParamCounter(self):
        return self.param_counter[-1]

    def incrementParamCounter(self):
        self.param_counter[-1] += 1
    
    def resetParamCounter(self):
        self.param_counter.pop()

    # Param's types
    def setParamTypesList(self, param_types_list):
        self.param_types_list = param_types_list
    
    def getParamTypesList(self):
        return self.param_types_list
    
    def getParamTypeInIndex(self, index):
        # Validate index is inbounds
        if index >= len(self.param_types_list):
            return None
        
        return self.param_types_list[index]