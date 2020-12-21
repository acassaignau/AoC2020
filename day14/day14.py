print('Part 1')
import collections
AddressSpace=collections.namedtuple('AddressSpace',['address','value'])

list1=[]
for line in open('input.txt'):
    instructiontype = line.split(' = ')[0]
    #grab the instructions / masks
    if instructiontype == 'mask':
        mask=line.split(' = ')[1].split('\n')[0][::-1]
    else:
        myaddress=line.split(' = ')[0].split('[')[1].split(']')[0]
        #gets the binary number in reverse (::-1)
        tobemasked=str(bin(int(line.split(' = ')[1]))).split('b')[1][::-1]
        i=0
        result=''
        while i<len(mask):
            if mask[i]=='0'or mask[i]=='1':
                result=result+mask[i]
            else:
                if i<len(tobemasked):
                    if tobemasked[i]=='1':
                        result=result+'1'
                    else:
                        result=result+'0'
                else:
                    result=result+'0'
            i=i+1            
        for a in list1:
            if a.address==myaddress:
                list1.remove(a)
        list1.append(AddressSpace(myaddress,result[::-1]))
        #print(int(0b00111))

total=0
for a in list1:
    total=total+int('0b'+a.value,2)    
print(total)


print('Part 2')

    
def UnPack(Code):
    unpacked=[Code]
    while any('X' in a for a in unpacked):    
        cond=False
        i=0
        for element in unpacked:
            while not cond and i<len(element):
                if element[i]=='X':
                    cond=True
                    if i==0:
                        one='1'+element[1:]
                        two='0'+element[1:]
                    else:
                        if i==len(element)-1:
                            one=element[:-1]+'1'
                            two=element[:-1]+'0'
                        else:
                            one=element[:i]+'1'+element[i+1:]
                            two=element[:i]+'0'+element[i+1:]
                    unpacked.append(one)
                    unpacked.append(two)
                    if element in unpacked:
                        unpacked.remove(element)                
                i=i+1
    return unpacked

def MaskAway(Mask,ToMask):
    i=0
    result=''
    while i<len(Mask):
        if Mask[i]=='1' or Mask[i]=='X':
            result=result+mask[i]
        else:
            if i<len(ToMask):
                result=result+ToMask[i]
            else:
                result=result+Mask[i]
        i=i+1
        
    

list1=[]
for line in open('input.txt'):
    instructiontype = line.split(' = ')[0]
    #grab the instructions / masks
    if instructiontype == 'mask':
        mask=line.split(' = ')[1].split('\n')[0][::-1]
    else:
        SetTo=line.split(' = ')[1].split('\n')[0]
        tobemasked=str(bin(int(line.split(' = ')[0].split('[')[1].split(']')[0]))).split('b')[1][::-1]
        print(tobemasked,SetTo)
        
        
        i=0
        result=''
        while i<len(mask):
            if mask[i]=='X'or mask[i]=='1':
                result=result+mask[i]
            else:
                if i<len(tobemasked):
                    if tobemasked[i]=='1':
                        result=result+'1'
                    else:
                        result=result+'0'
                else:
                    result=result+'0'
            i=i+1    
        UnPackMe=result[::-1]
        ListOfDestinations=UnPack(UnPackMe)
        
        for EveryDestination in ListOfDestinations:
            goeshere=str(int('0b'+EveryDestination,2))
            for a in list1:
                if a.address==goeshere:
                    list1.remove(a)            
            list1.append(AddressSpace(goeshere,SetTo))
        #print(list1)

#print(UnPack('1XXX0'))        
        
#     for a in list1:
#         if a.address==myaddress:
#             list1.remove(a)
#     list1.append(AddressSpace(myaddress,result[::-1]))



total=0
for a in list1:
    total=total+int(a.value)
print(total)

