print("Part 1")

seatIDs=[]
for line in open('input.txt'):
    row=line[:-4]
    column=line[-4:-1]
    r=0
    Row=[0,127]
    while r < len(row):
        if row[r] == 'F':
            Row[1]=(Row[0]+Row[1])//2
        else:
            Row[0]=(Row[0]+Row[1])//2 + 1
        r = r+1
#     print(Row[0])
    c=0
    Column=[0,7]
    while c < len(column):
        if column[c] == 'L':
            Column[1]=(Column[0]+Column[1])//2
        else:
            Column[0]=(Column[0]+Column[1])//2 + 1
        c = c+1
#     print(Column[0])
    ID=8*Row[0]+Column[0]
    seatIDs.append(ID)
    
    
print(sorted(seatIDs))
print(max(seatIDs))

print("Part 2")

#seats between 13-880:
#AllSeats=list(range(13,881))
#print(AllSeats)
i=13
while i<=880:
    index = seatIDs.index(i)
    i=i+1

    

