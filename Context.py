class Context:
    def __init__(self):
        self.current_type = ''
        self.vars = [{}]
    
    def setCurrType(self, curr):
        self.current_type = curr
    
    def getCurrType(self):
        return self.current_type
    
    def setVars(self, var, var_type):
        dict = {}
        dict[var] = var_type
        self.vars.append(dict)
    
    def getVars(self):
        return self.vars
    
    def clearVars(self):
        self.vars.clear()