print("Part 1")
counter=0
position=0
with open('input.txt') as f:
    first_line = f.readline()
    width=len(first_line)-1 #why on earth is length wrong
for line in open('input.txt'):
    if line[position]=='#':
        counter=counter+1
    position=position+3
    if position>(width-1):
        position=position-(width)
    
print(counter,"trees encountered")


print("Part 2")

counter={'R1D1':0,'R3D1':0,'R5D1':0,'R7D1':0,'R1D2':0}
position={'R1D1':0,'R3D1':0,'R5D1':0,'R7D1':0,'R1D2':0}

with open('input.txt') as f:
    first_line = f.readline()
    width=len(first_line)-1

linecounter=1
for line in open('input.txt'):
#     if line[position['R1D1']]=='#':
#             position['R1D1'] = position['R1D1'] +1
    for key in position:
        #print(line[position[key]])
        if line[position[key]]=='#':
            counter[key] = counter[key] +1
            if key == 'R1D2' and linecounter % 2 == 0: 
                counter['R1D2'] = counter['R1D2'] -1
    
    position['R1D1'] = position['R1D1'] +1
    position['R3D1'] = position['R3D1'] +3
    position['R5D1'] = position['R5D1'] +5
    position['R7D1'] = position['R7D1'] +7
    if not linecounter % 2 == 0: 
        position['R1D2'] = position['R1D2'] +1

    for key in position:
        if position[key]>(width-1):
                position[key]=position[key]-width    
    linecounter=linecounter+1
          
    
print(counter,"trees encountered")
print("Answer is",counter['R1D1']*counter['R3D1']*counter['R5D1']*counter['R7D1']*counter['R1D2'])



