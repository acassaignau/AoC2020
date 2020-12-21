print("Part 1")
counter=0
for line in open('input.txt'):
    a = line.split()[0].split("-")
    character=line.split()[1]
    if line.split()[2].count(character[0]) >= int(a[0]) and line.split()[2].count(character[0]) <= int(a[1]):
        counter=counter+1
    #print(a[0],a[1],character[0],line.split()[2].count(character[0]))
        
print(counter)

print("Part 2")
counter=0
for line in open('input.txt'):
    a = line.split()[0].split("-")
    character=line.split()[1]
    #print(character[0],line.split()[2],line.split()[2][int(a[0])],line.split()[2][int(a[1])],a[0],a[1])
    if line.split()[2][int(a[0])-1] == character[0] and not line.split()[2][int(a[1])-1] == character[0]:
        counter=counter+1
    if not line.split()[2][int(a[0])-1] == character[0] and line.split()[2][int(a[1])-1] == character[0]:
        counter=counter+1      
    
print(counter)