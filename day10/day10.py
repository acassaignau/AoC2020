print('Part 1')

list=[0]
for line in open('input.txt'):
    list.append(int(line.split('\n')[0]))
sortd=sorted(list)
i=0
counter1=1
counter3=1
while i<(len(sortd)-1):
    if sortd[i+1]-sortd[i]==1:
        counter1=counter1+1
    if sortd[i+1]-sortd[i]==3:
        counter3=counter3+1
    i=i+1

print(counter1*counter3)

print('Part 2')
# I added "195" to the list

count = len(open('input.txt').readlines(  ))

def FindNeighbours(i):
    index=sortd.index(i)
    #find neighbours in the list that are not part of the earlier numbers
    result=[]    
    j=index+1
    while j<count+1:
        k=sortd[j]
        #this finds the neighbours
        if not i==k and abs(i-k)<=3:
            result.append(str(k))
        j=j+1
    return result


possibilities={'0':1}
a=0
counter=0
finalcombo={}
while a<count:
    start={}
    for combo in possibilities:
        # last number, previous numbers and new possibilites to carry on the string
        lastnumber=combo.split(':')[-1]
        newletters = FindNeighbours(int(lastnumber))
        if not newletters==[]:
            if not newletters==['195']:
                for poss in newletters:
                    #if there are new items to append&we haven't reached the end, create a new start array
                    if combo.count(':')>5:
                        #no need to have stupidly long strings
                        shortercombo=':'.join(combo.split(':')[1:])
                        newcombo=shortercombo+':'+poss
                        if newcombo in start:
                            start[newcombo]=start[newcombo]+possibilities[combo]
                        else:
                            start[newcombo]=possibilities[combo]
                    else:
                        start[combo+':'+poss]=possibilities[combo]
            else:
                if combo in finalcombo:
                    finalcombo[combo]=finalcombo[combo]+possibilities[combo]
                else:
                    finalcombo[combo]=possibilities[combo]
    possibilities=start
    a=a+1
summed=0
for item in finalcombo:
    summed=summed+finalcombo[item]
print("Answer:",summed)

#print(sortd)
