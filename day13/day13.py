print('Part 1')

with open('input.txt') as f:
    IArrive = f.readlines()[0].split('\n')[0]
with open('input.txt') as f:
    timez = f.readlines()[1].split('\n')[0].split(',')

Buses={}    
for bus in timez:
    if not bus=='x':
        lateness=int(bus)-(int(IArrive)%int(bus))
        Buses[bus]=lateness

print(Buses)

SmallestWait=int(min(Buses, key = lambda k: Buses[k]))
BusWithSmallestWait=int(Buses[min(Buses, key = lambda k: Buses[k])])
print('The answer is',SmallestWait*BusWithSmallestWait)

print('Part 2')
#only now I saw that these are all primes. yay

def is_prime(n):
    for i in range(3, n):
        if n % i == 0:
            return False
    return True
for bus in Buses:
    print(is_prime(int(bus)))    
    
def FindFirstIncidence(A,a,B,b):
    foundit=False
    i=A-a
    while not foundit:
        i=i+A
        if (i+b)%B==0:
            return i
         
Buses2={}   
counter=0
for bus in timez:
    counter=counter+1
    if not bus=='x':
        Buses2[bus]=counter-1
print(Buses2)
Buses2InAList=sorted(Buses2, reverse=True)

MeetMe=[int(Buses2InAList[0]),Buses2[Buses2InAList[0]] ]
for bus in Buses2InAList[1:]:
    A=MeetMe[0]*int(bus)    
    a=FindFirstIncidence(MeetMe[0],MeetMe[1],int(bus),Buses2[bus])
    print(MeetMe[0],MeetMe[1],int(bus),Buses2[bus])
    
    MeetMe=[A,A-a]
    print(MeetMe)
    
print('The Answer Is'a)