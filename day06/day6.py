print("Part 1")
questions={'a':0,'b':0,'c':0,'d':0,'e':0,'f':0,'g':0,'h':0,'i':0,'j':0,'k':0,'l':0,'m':0,'n':0,'o':0,'p':0,'q':0,'r':0,'s':0,'t':0,'u':0,'v':0,'w':0,'x':0,'y':0,'z':0}

group=1
counter=[]
for line in open('input.txt'):
    if line == '\n':
        group=group+1
        counter.append(0)
        for q in questions:
            if questions[q] > 0:
                counter[group-2]=counter[group-2]+1
        for q in questions:
            questions[q]=0
    else:
        for q in questions:
            i=0
            while i<len(line):
                if q == line[i]:
                    questions[q]=questions[q]+1
                i=i+1
                
print(counter)
sum=0    
for i in counter:
    sum=sum+i
print(sum)

print("Part 2")
questions={'a':0,'b':0,'c':0,'d':0,'e':0,'f':0,'g':0,'h':0,'i':0,'j':0,'k':0,'l':0,'m':0,'n':0,'o':0,'p':0,'q':0,'r':0,'s':0,'t':0,'u':0,'v':0,'w':0,'x':0,'y':0,'z':0}

group=1
counter=[]
linecounter=0
for line in open('input.txt'):
    if line == '\n':
        group=group+1
        counter.append(0)
        for q in questions:
            if questions[q] == linecounter:
                counter[group-2]=counter[group-2]+1
        for q in questions:
            questions[q]=0
        linecounter=0
    else:
        linecounter=linecounter+1
        for q in questions:
            i=0
            while i<len(line):
                if q == line[i]:
                    questions[q]=questions[q]+1
                i=i+1
                
print(counter)
sum=0    
for i in counter:
    sum=sum+i
print(sum)