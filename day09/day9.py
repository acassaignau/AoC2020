print('Part 1')

query=25
cond1=True
while cond1:
    with open('input.txt') as f:
        line = f.readlines()[query]
        isitasum=int(line.split('\n')[0])
        cond2=False
        i=query-25
        while not cond2 and i<query:
            j=i+1
            while not cond2 and j<query:
                with open('input.txt') as f:
                    line2 = f.readlines()[i]
                    i_num=int(line2.split('\n')[0])
                with open('input.txt') as f:
                    line3 = f.readlines()[j]
                    j_num=int(line3.split('\n')[0])

                if isitasum==(i_num+j_num):
                    cond2=True
                j=j+1
            i=i+1        
    cond1=cond2    
    query=query+1

print(isitasum)

print('Part 2')

def AddUpContiguous(i,num):   
    with open('input.txt') as f:
        line = f.readlines()[i]
        summed=int(line.split('\n')[0])
        list=[summed]
    while summed < num:
        with open('input.txt') as f:
            line = f.readlines()[i+1]
            addme=int(line.split('\n')[0])
            summed=summed+addme
            list.append(addme)
        i=i+1
    if summed==num:
        print(min(list)+max(list),"yo")
        return
    

count = len(open('input.txt').readlines(  ))
k=1
while k<count:
    AddUpContiguous(k,isitasum)
    k=k+1
    