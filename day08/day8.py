print('Part 1')

accumulator=0
myline=0
memory=[]
condition=True

while condition:
    with open('input.txt') as f:
        line = f.readlines()[myline]
        instruction1=line.split(' ')[0]
        instruction2=line.split(' ')[1]    
    if instruction1=='nop':
        myline=myline+1
    if instruction1=='acc':
        accumulator=accumulator+int(instruction2)
        myline=myline+1
    if instruction1=='jmp':
        myline=myline+int(instruction2)
    if myline in memory:
        condition=False
    else:
        memory.append(myline)

print(accumulator)

print('Part 2')

count = len(open('input.txt').readlines(  ))

def RunProgram(i):
    accumulator=0
    myline=0
    memory=[]
    condition=True
    while condition:
        with open('input.txt') as f:
            line = f.readlines()[myline]
            instruction1=line.split(' ')[0]
            instruction2=line.split(' ')[1]    
        if instruction1=='nop':
            if myline==i:
                myline=myline+int(instruction2)
            else:
                myline=myline+1
        if instruction1=='acc':
            accumulator=accumulator+int(instruction2)
            myline=myline+1
        if instruction1=='jmp':
            if myline==i:
                myline=myline+1
            else:
                myline=myline+int(instruction2)
        if myline in memory:
            condition=False
        else:
            memory.append(myline)
        if myline >= count:
            return accumulator
    return False

j=1
while j<count:
    if not RunProgram(j) == False:
        print(RunProgram(j))
    j=j+1
    
