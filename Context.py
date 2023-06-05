class Context:
    def __init__(self):
        # Variable's type
        self.current_type = ''
        self.scope = []
        
        # For <call> diagram
        self.param_counter = []
        self.param_types_list = []
        self.param_names_list = []
        self.function_name = ''

        self.current_class = None
        self.current_object = None

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
    
    # Param's names
    def setParamNamesList(self, param_names_list):
        self.param_names_list = param_names_list
    
    def getParamNamesList(self):
        return self.param_names_list
    
    def getParamNameInIndex(self, index):
        # Validate index is inbounds
        if index >= len(self.param_names_list):
            return None
        
        return self.param_names_list[index]
    
    # Function name
    def setFunctionName(self, func_name):
        self.function_name = func_name

    def getFuncionName(self):
        return self.function_name
    
    # Class name
    def setCurrentClass(self, name):
        self.current_class = name

    def getCurrentClass(self):
        return self.current_class
    
    def clearCurrentClass(self):
        self.current_class = None

    # Object name
    def setCurrentObject(self, name):
        self.current_object = name
    
    def getCurrentObject(self):
        return self.current_object
    
    def clearCurrentObject(self):
        self.current_object = None

    def clear(self):
        self.current_type = ''
        self.scope.clear()

        self.param_counter.clear()
        self.param_types_list.clear()
        self.param_names_list.clear()
        self.function_name = ''