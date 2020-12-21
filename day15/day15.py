print('Part 1')
#part2: 2020th number spoken?
inputfile=[16,1,0,18,12,14,19]
#inputfile=[0,3,6]
           
# i=len(inputfile)-1
# while i<2019:
#     j=i-1
#     cond1=False
#     cond2=False
#     a=-1
#     b=-1    
#     while j>=0 and not cond1 and not cond2:
#         if not cond1 and inputfile[j]==inputfile[i]:
#             a=j
#             cond1=True
#         else:
#             if not cond2 and inputfile[j]==inputfile[i]:
#                 b=j
#                 cond2=True
#         j=j-1
#     if b==-1:
#         if a==-1:
#             inputfile.append(0)
#         else:
#             inputfile.append(int(i-a))
#     else:
#         inputfile.append(a-b)
#     i=i+1
# print(inputfile)

print('Part 1 again: this is not good enough')
#part2: 30000000th number spoken?
import collections

Memory=collections.namedtuple('Memory',['number','position'])

#inputfile=[0,3,6]
MemoryList=[]
# inputfile=[16,1,0,18,12,14,19]
# i=0
# for element in inputfile:
#     MemoryList.append(Memory(element,i))
#     i=i+1
# print(MemoryList)
    
# i=len(inputfile)-1
# CurrentValue=inputfile[len(inputfile)-1]
# while i<2019:
#     FoundIt=False
#     for j in MemoryList:
#         if not FoundIt:
#             if j.number==CurrentValue:
#                 CurrentValue=i-j.position
#                 a=j.number
#                 MemoryList.remove(j)
#                 MemoryList.append(Memory(a,i))
#                 FoundIt=True
#     if not FoundIt:
#         MemoryList.append(Memory(CurrentValue,i))
#         CurrentValue=0
#     i=i+1

# print(CurrentValue)
# #print(MemoryList)

print('Part 2')
#part2: 30000000th number spoken?

import numpy as np

Memry=np.full((30000000,1),-1)

inputfile=[16,1,0,18,12,14]
i=0
for element in inputfile:
    Memry[element]=i
    i=i+1
    
i=len(inputfile)
CurrentValue=19
while i<29999999:
    if int(Memry[CurrentValue])==-1:
        NewValue=0
    else:
        NewValue=i-int(Memry[CurrentValue])
    Memry[CurrentValue]=i
    CurrentValue=NewValue
    i=i+1

print(CurrentValue)
#print(MemoryList)
