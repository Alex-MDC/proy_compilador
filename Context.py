class Context:
    def __init__(self):
        self.current_type = ''
        self.vars = [{}]
        self.scope = []

        #for return type handling
        self.scope_type = None
        
        # For <call> diagram
        self.param_counter = 0
        self.param_list = []
    

    def setScopeType(self, curr):
        self.scope_type = curr
    
    def getScopeType(self):
        return self.scope_type

    def setCurrType(self, curr):
        self.current_type = curr
    
    def getCurrType(self):
        return self.current_type
    
    def addVars(self, var, var_type):
        dict = {}
        dict[var] = var_type
        self.vars.append(dict)
    
    def getVars(self):
        return self.vars
    
    def clearVars(self):
        self.vars.clear()

    def setScope(self, scope):
        self.scope.append(scope)

    def popScope(self):
        self.scope.pop()
    
    def getScope(self):
        return self.scope[-1]
    
    def getParamCounter(self):
        return self.param_counter

    def incrementParamCounter(self):
        self.param_counter += 1
    
    def resetParamCounter(self):
        self.param_counter = 0

    def setParamListCALL(self, param_list):
        self.param_list = param_list
    
    def getParamListCALL(self):
        return self.param_list
    
    def getSingleParamCALL(self, index):
        return self.param_list[index]