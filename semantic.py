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

import pprint

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
