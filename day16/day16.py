print('Part 1')
import collections
TicketItems=collections.namedtuple('TicketItems',['name','range1','range2'])

Ranges=[]
bloc1=True
i=0

#read bloc 1
while bloc1:
    with open('input.txt') as f:
        line = f.readlines()[i]
    if line=='\n':
        bloc1=False
    if bloc1: 
        range1=line.split(': ')[1].split(' or ')[0]
        range2=line.split(': ')[1].split(' or ')[1].split('\n')[0]
        Ranges.append(TicketItems(line.split(': ')[0],range1,range2))
    i=i+1
print(Ranges)

#read my ticket
i=i+1
with open('input.txt') as f:
    line = f.readlines()[i]
myticket=line.split(',')
print(myticket)
    
print('Part (1&)2')


CountFakes=0
GoodTicketsList=[]
i=i+3
#read bloc 3
bloc3=True
while bloc3:
    with open('input.txt') as f:
        line = f.readlines()[i]
    if line=='\n':
        bloc3=False
    if bloc3: 
        items=line.split('\n')[0].split(',')
        istheticketok=True
        for each in items:
            itisok=False
            for ticketitems in Ranges:
                if int(each) >= int(ticketitems.range1.split('-')[0]) and int(each) <= int(ticketitems.range1.split('-')[1]):
                    itisok=True
                if int(each) >= int(ticketitems.range2.split('-')[0]) and int(each) <= int(ticketitems.range2.split('-')[1]):
                    itisok=True
            if not itisok:
                CountFakes=CountFakes+int(each)
                istheticketok=False
        if istheticketok:
            GoodTicketsList.append(items)                
    i=i+1

print('sum from fakes',CountFakes)    
#print(GoodTicketsList)

Exclusions={}
for i in GoodTicketsList:
    j=-1
    for each in i:
        j=j+1
        for ticketitems in Ranges:
            if (int(each) < int(ticketitems.range1.split('-')[0]) or int(each) > int(ticketitems.range1.split('-')[1])) and (int(each) < int(ticketitems.range2.split('-')[0]) or int(each) > int(ticketitems.range2.split('-')[1])):
                if ticketitems.name in Exclusions:
                    Exclusions[ticketitems.name].append(j)
                else:
                    Exclusions[ticketitems.name]=[j]

print(Exclusions)

def Diff(li1, li2):
    return (list(list(set(li1)-set(li2)) + list(set(li2)-set(li1))))

b=list(range(0,20))
Solutions={}

notalldone=True
while notalldone: 
    cond=True
    for key, value in Exclusions.items():
        a=Diff(value,b)      
        if len(a)==1 and cond:
            Solutions[key]=a[0]
            c=key
            toremove=a
            cond=False
    if not cond:
        Exclusions.pop(c)
        for key2, value2 in Exclusions.items():
            Exclusions[key2]=Exclusions[key2]+toremove
    if Exclusions=={}:
        notalldone=False
print(Solutions)

Answer=1
for key,value in Solutions.items():
    if 'departure' in key:
        index=value
        Answer=Answer*int(myticket[index])      
print(Answer)



    

        