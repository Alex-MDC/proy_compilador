class Context:
    def __init__(self):
        self.current_type = ''
        self.vars = [{}]
        #aux types for expression comparisons
        self.leftExpType =''
        self.rightExpType =''
        self.relationOp = None
    
    def setCurrType(self, curr):
        self.current_type = curr

    def setLeftType(self,type):
        self.leftExpType = type

    def setRightType(self,type):
        self.rightExpType = type

    def setRelationOp(self,op):
        self.relationOp = op
    
    def getCurrType(self):
        return self.current_type
    
    def getLeftType(self):
        return self.leftExpType
    
    def getRightType(self):
        return self.rightExpType
    
    def getRelationOp(self):
        return self.relationOp
    
    def setVars(self, var, var_type):
        dict = {}
        dict[var] = var_type
        self.vars.append(dict)
    
    def getVars(self):
        return self.vars
    
    def clearVars(self):
        self.vars.clear()