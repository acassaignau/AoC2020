print("Part 1")
import collections
BagContents=collections.namedtuple('BagContents',['colour','number'])

Bags={}
for line in open('input.txt'):
    container=line.split('bags contain')[0][:-1]
    contents=line.split('bags contain')[1].split('.')[0][1:].split(', ')
    Bags[container]=[]
    for item in contents: 
        if item == 'no other bags':
            Bags[container].append(BagContents('no other bags',0))
        else:
            bagnumber=item.split(' ')[0]
            bagcolour=item.split('bag')[0][2:][:-1]
            Bags[container].append(BagContents(bagcolour,bagnumber))
            
    #print(Bags)

def SearchForShinyGold(i):
    for newbags in Bags[i]:          
        if newbags.colour == 'shiny gold':
            return True
        if not newbags.colour == 'no other bags':
            new_i=newbags.colour
#             print('under this',new_i)
            if SearchForShinyGold(new_i):
                return True
    return False
            
counter=0    
# print(Bags)
for bag in Bags:
#     print(bag)
    if not bag == 'shiny gold':
         if SearchForShinyGold(bag):
            counter=counter+1

    #print(SearchForShinyGold(bag))
    #print(counter)
        
        
print(counter)
        
            
print("Part 2")

def HowManyBags(i):
    counter=0
    for newbags in Bags[i]:
        print(i)
        counter=counter+int(newbags.number)
        if not newbags.colour == 'no other bags':
            new_i=newbags.colour
            print('under this',new_i)
            counter=counter+int(newbags.number)*(HowManyBags(new_i))
    return counter

        
print(HowManyBags('shiny gold'))        