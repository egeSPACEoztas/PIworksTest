def is_prime(x):
    if x > 1:
        for i in range(2, x):
            if (x % i) == 0:
                return False
        return True
    return False
#a simple func to tell if is prime or not

#create a pyramid node sytem so we can sort things easily
#only two branches either down or diagonal
class PyramidNode:
    def __init__(self, key=None, down=None, diagnoal=None):
        self.down = down
        self.diagnoal = diagnoal
        self.key = key

#from a list we make the pyramid object i is its first layer length k is second layer depth
def MakePyramid(i,k,  pyramidList):
    if ((i+1) == len(pyramidList)):
        return PyramidNode(key = pyramidList[i][k])
        #if there is no more pyramid left leave branches empty
    else:
        return PyramidNode(pyramidList[i][k], down=MakePyramid(i+1, k, pyramidList), diagnoal=MakePyramid(i+1, k+1, pyramidList ))
        #k is at most equal to i as nodes either go one down in same depth or go one deeper

def TraversePyramid(valueOfPyramidRoute, root):
    print("considered route val:", valueOfPyramidRoute)
    if (root.down != None and root.diagnoal != None): #if both of the branches exist recursively consider both of them
        if (is_prime(root.down.key)): #if a branch contains prime nummber we can not go there so we consider all possible paths from there as 0 and go no fuhrer
            downVal = 0
        else:
            downVal = TraversePyramid((valueOfPyramidRoute + root.key), root.down)
        if (is_prime(root.diagnoal.key)): #same here
            diagnoalVal = 0
        else:
            diagnoalVal = TraversePyramid((valueOfPyramidRoute + root.key), root.diagnoal)
        return max(downVal, diagnoalVal)

    elif (root.down != None): #just in case if the algorithm is given an uneven tree to sort and consider
        if (is_prime(root.down.key)):
            return 0
        return TraversePyramid((valueOfPyramidRoute + root.key), root.down)
    elif (root.diagnoal != None):
        if (is_prime(root.diagnoal.key)):
            return 0
        return TraversePyramid((valueOfPyramidRoute + root.key), root.diagnoal)
    else:
        return valueOfPyramidRoute #if no branches are left simply return the path value we have made this far


file_location = "demofile.txt"
f = open(file_location, "r")
InputAsList = []
for line in f:
    #print(line)
    int_list = [int(num) for num in line.split()]
    #print(int_list)
    InputAsList.append(int_list)
    #print(InputAsList)


PyramidRoot = MakePyramid(0, 0, InputAsList)
max_sum = TraversePyramid(0, PyramidRoot)
print(max_sum)