class Context:
    def __init__(self):
        self.current_type = ''
        self.vars = [{}]
        self.params = []
        self.scope = []
    
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

    def addParams(self, param_type):
        '''
        Params is a list that only contains the type of the parameters in order
        '''
        self.params.append(param_type)

    def getParams(self):
        return self.params

    def clearParams(self):
        self.params.clear()

    def setScope(self, scope):
        self.scope.append(scope)

    def popScope(self):
        self.scope.pop()
    
    def getScope(self):
        return self.scope[-1]