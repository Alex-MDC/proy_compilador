class Context:
    def __init__(self):
        # Variable's type
        self.current_type = ''
        self.scope = []
        
        # For <call> diagram
        self.param_counter = []
        self.param_list = []

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

    def setParamListCALL(self, param_list):
        self.param_list = param_list
    
    def getParamListCALL(self):
        return self.param_list
    
    def getSingleParamCALL(self, index):
        # Validate index is inbounds
        if index >= len(self.param_list):
            return None
        
        return self.param_list[index]