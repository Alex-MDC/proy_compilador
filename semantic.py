import pprint

#this file contains the semantic components
#such as the semantic cube, procedure directory
#------------------------------
# Operations and their index
# 0. +
# 1. -
# 2. *
# 3. /
# 4. >
# 5. <
# 6. >=
# 7. <=
# 8. ==
# 9. <>
# Operator Types
# 0. int
# 1. float
# 2. char
# 3. bool
# Error codes
# -1 type_mismatch
#-----------------------



#global components -------
#type and scope is given by memory direction
#TODO dir funciones  ---- dir vars --> list of dictionaries
#function signature: return type, name, params, 
# funDict =[{"functionID":2,"type":"void","params":{}, "varTable":???}] TODO define all structures
funDict =[]
globalVars =[]
#constants structure
# [{"memoryDir":25001, "value":5},{"memoryDir":27000, "value":7.9}]
constants =[]

tempVars=[]
tempFunDict=[]

#memory direction gives both type and scope
#TODO add memdir ranges explanation
current_memDir=None
cteInt_counter = 0
cteFloat_counter = 0
cteChar_counter = 0
#-------------------------

def addConstant(constantVal):
    global constants
    memTypeCounter = None
    # check for duped values, will only add if new value is unique
    if not any(d['value'] == constantVal for d in constants):
        #TODO handle counter types
        #find val in constant table, get range and do math to get type then
        #increase appropiate counter based on type.
        # for cte in constants:
        #     if (cte["memoryDir"] - 2 )

        # lastDir=memoryDir[-1]["memoryDir"] TODO: add to memory
        # memoryDir.append("memoryDir":lastDir+1,"value":constantVal)

        newCte = {"memoryDir":memTypeCounter,"value":constantVal}
        constants.append(newCte.copy())






#semantic cube follows this order of indexes:
# semanticCube[operation][leftOperator type][right operator type]
#example:  int * float --> semanticCube [2] [0][1] = 1 
#which means that the type of the multiplication of an int with a float is a float 
#cube dimensions: 10x4x4
def createSemanticCube():
    global semanticCube
    semanticCube = [
        [[0,1,-1,-1],
         [1,1,-1,-1],
         [-1,-1,-1,-1],
         [-1,-1,-1,-1]],   #0
        [[0,1,-1,-1],
         [1,1,-1,-1],
         [-1,-1,-1,-1],
         [-1,-1,-1,-1]],   #1
        [[0,1,-1,-1],
         [1,1,-1,-1],
         [-1,-1,-1,-1],
         [-1,-1,-1,-1]],   #2
        [[0,1,-1,-1],
         [1,1,-1,-1],
         [-1,-1,-1,-1],
         [-1,-1,-1,-1]],   #3
        [[3,3,-1,-1],
         [3,3,-1,-1],
         [-1,-1,-1,-1],
         [-1,-1,-1,-1]],   #4
        [[3,3,-1,-1],
         [3,3,-1,-1],
         [-1,-1,-1,-1],
         [-1,-1,-1,-1]],   #5
        [[3,3,-1,-1],
         [3,3,-1,-1],
         [-1,-1,-1,-1],
         [-1,-1,-1,-1]],   #6
        [[3,3,-1,-1],
         [3,3,-1,-1],
         [-1,-1,-1,-1],
         [-1,-1,-1,-1]],   #7
        [[3,3,-1,-1],
         [3,3,-1,-1],
         [-1,-1,3,-1],
         [-1,-1,-1,3]],    #8
        [[3,3,-1,-1],
         [3,3,-1,-1],
         [-1,-1,3,-1],
         [-1,-1,-1,3]]     #9
 
    ]
    #pprint.pprint(semanticCube)
    # print("------------------------------")
    # print(semanticCube[2][0][1])

    def delSemanticCube():
        global semanticCube
        del semanticCube
