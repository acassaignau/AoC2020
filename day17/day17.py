print('Part 1')
import numpy as np
import math

#read in slice
donnée=''
for line in open('input2.txt'):
    donnée=donnée+line.split('\n')[0]
print(donnée)
j=math.sqrt(len(donnée))
print(j)
i=0

List=[]
while i<int(j):
    List.append(list(donnée[i*int(j):(i+1)*int(j)]))
    i=i+1

myarray=np.array(List)
print(myarray)

def FindNeighbourValues(array):
    

# #make new slice
# def ExpandCube(old):
#     cube=j
#     cycle=1
#     while cycle<=6:
#         cycle=cycle+1
        