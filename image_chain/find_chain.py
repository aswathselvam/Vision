import numpy as np
import sys

# Increase this recursion limit if you encounter error
# or if you expand the arena size

# sys.setrecursionlimit(200000)

print("Current recursion limit is: ", sys.getrecursionlimit())

#10x10
grid=". . . . . . . . . ."\
     ". + + . . . . . . ."\
     ". . + + + . . . . ."\
     ". . . . + . . . . ."\
     ". . . . . . . . . ."\
     ". . . . . . . . . ."\
     ". . . . . . . . . ."\
     ". . . . . . . . . ."\
     ". . . . . . . . . ."\
     ". . . . . . . . . ."

rows = 10
cols = 10

arena = []
for j in range(10):
    arena.append([])
    for i in range(0,20,2):
        arena[j].append(grid[j*19+i])

path = {}

def findChain(r, c):
    global arena, rows, cols, path

    #Check boundary conditions
    if(r>rows or c>cols or r<0 or c<0):
        return False

    if(path.get((r,c))):
            return False

    if(arena[r][c]!='+'):
        return False      

    path[(r,c)]=True
    # print(r,c)
    path_available= False

    # UP
    if(findChain(r-1,c)):
        path_available=path_available or True

    # RIGHT
    if(findChain(r,c+1) and not path_available):
        path_available |= True

    # DOWN
    if(findChain(r+1,c) and not path_available):
        path_available |= True

    # LEFT
    if(findChain(r,c-1) and not path_available):
        path_available |= True

    return path_available


# Start the search from (3,4)
result = findChain(3,4)
print("Path found? ", result)
print("Found path is: ", list(path.keys()))