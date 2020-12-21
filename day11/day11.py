print('Part 1')
import numpy as np

def split(word): 
    return list(word)

#read in data as array (92x95)
with open('input.txt') as f:
    line = f.readlines()[0]
    onearray=np.array(split(line[:-1]))
i=1
while i<92:
    with open('input.txt') as f:
        line = f.readlines()[i]
        twoarray=np.array(split(line[:-1]))
        Array=np.hstack((onearray,twoarray))
        onearray=Array
    i=i+1
# print(Array)
# print(Array.shape)
FinalArray=Array.reshape(92,95)
print(FinalArray)
# print(FinalArray.shape)



# #go through array and find amount of neighbours
# i=0
# j=0
# NewArray=np.copy(FinalArray)

# cond=False
# while not cond:
#     OldArray=np.copy(NewArray)
#     i=0
#     j=0
#     while i<len(NewArray[:,1]):
#         while j<len(NewArray[1,:]):
#             # slicing numpy arrays: result includes the start index, but excludes the end index!!
#             if i==0: k=0
#             else: k=i-1
#             if i==len(NewArray[:,1]): l=NewArray[:,1]
#             else:l=i+2
#             if j==0: m=0
#             else: m=j-1
#             if j==len(NewArray[1,:]): n=NewArray[1,:]
#             else:n=j+2
#             partialArray=OldArray[k:l,m:n]
#             if OldArray[i,j]=='L':
#                 count=np.count_nonzero(partialArray == '#')
#                 if count==0:
#                     NewArray[i,j]='#'
#             if OldArray[i,j]=='#':
#                 count=np.count_nonzero(partialArray == '#')-1
#                 #print(partialArray,count)
#                 if count>=4:
#                     NewArray[i,j]='L'
#             j=j+1
#         j=0
#         i=i+1
#     cond= np.array_equal(OldArray,NewArray)
#     #print(cond)
#     np.set_printoptions(edgeitems=8)
#     #print(NewArray)

# print(np.count_nonzero(NewArray == '#'))
# print(np.count_nonzero(OldArray == '#'))

# np.set_printoptions(edgeitems=8)
# print(NewArray)
# print(OldArray)

print('Part 2')

cond=False
NewArray=np.copy(FinalArray)

while not cond:
    OldArray=np.copy(NewArray)
    i=0
    j=0
    while i<len(OldArray[:,1]):
        while j<len(OldArray[1,:]):
            counter=0
            
            #HORIZONTAL
            #search to the right ####################
            if not i==len(OldArray[:,1]):
                #right
                k=i+1
                keepsearching=True
                while k<len(OldArray[:,1]) and keepsearching:
                    if OldArray[k,j]=='L':
                        keepsearching=False
                    if OldArray[k,j]=='#':
                        counter=counter+1
                        keepsearching=False
                    k=k+1
                #down right
                if not j==len(OldArray[1,:]):
                    k=i+1
                    l=j+1
                    keepsearching=True
                    while k<len(OldArray[:,1]) and l<len(OldArray[1,:]) and keepsearching:
                        if OldArray[k,l]=='L':
                            keepsearching=False
                        if OldArray[k,l]=='#':
                            counter=counter+1
                            keepsearching=False
                        k=k+1
                        l=l+1
                #up right
                if not j==0:
                    k=i+1
                    l=j-1
                    keepsearching=True
                    while k<len(OldArray[:,1]) and l>=0 and keepsearching:
                        if OldArray[k,l]=='L':
                            keepsearching=False
                        if OldArray[k,l]=='#':
                            counter=counter+1
                            keepsearching=False
                        k=k+1
                        l=l-1
                
            #search to the left ###############################       
            if not i==0:
                k=i-1
                keepsearching=True
                while k>=0 and keepsearching:
                    if OldArray[k,j]=='L':
                        keepsearching=False
                    if OldArray[k,j]=='#':
                        counter=counter+1
                        keepsearching=False
                    k=k-1
                    
                #down left
                if not j==len(OldArray[1,:]):
                    k=i-1
                    l=j+1
                    keepsearching=True
                    while k>=0 and l<len(OldArray[1,:]) and keepsearching:
                        if OldArray[k,l]=='L':
                            keepsearching=False
                        if OldArray[k,l]=='#':
                            counter=counter+1
                            keepsearching=False
                        k=k-1
                        l=l+1
                #up left
                if not j==0:
                    k=i-1
                    l=j-1
                    keepsearching=True
                    while k>=0 and l>=0 and keepsearching:
                        if OldArray[k,l]=='L':
                            keepsearching=False
                        if OldArray[k,l]=='#':
                            counter=counter+1
                            keepsearching=False
                        k=k-1
                        l=l-1
                    
            #VERTICAL  ###########################################      
            #search down
            if not j==len(OldArray[1,:]):
                k=j+1
                keepsearching=True
                while k<len(OldArray[1,:]) and keepsearching:
                    if OldArray[i,k]=='L':
                        keepsearching=False
                    if OldArray[i,k]=='#':
                        counter=counter+1
                        keepsearching=False
                    k=k+1
            #search up
            if not j==0:
                k=j-1
                keepsearching=True
                while k>=0 and keepsearching:
                    if OldArray[i,k]=='L':
                        keepsearching=False
                    if OldArray[i,k]=='#':
                        counter=counter+1
                        keepsearching=False
                    k=k-1

            #change the array according to the counter
            if OldArray[i,j]=='L':
                if counter==0:
                    NewArray[i,j]='#'
            if OldArray[i,j]=='#':
                if counter>=5:
                    NewArray[i,j]='L'
            j=j+1
        j=0
        i=i+1
    cond= np.array_equal(OldArray,NewArray)
    print(cond)
    np.set_printoptions(edgeitems=8)
    print(NewArray)


print(np.count_nonzero(NewArray == '#'))
print(np.count_nonzero(OldArray == '#'))

np.set_printoptions(edgeitems=8)
print(NewArray)
print(OldArray)


