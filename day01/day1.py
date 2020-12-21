#find 2 numbers adding to 2020

print("Part 1")
foundit=False
for line in open('input.txt'):
    a = int(line)
    for line in open('input.txt'):
        b = int(line)
        if a+b ==2020:
            print("hurray,",a,"+",b,"=2020",sep="")
            c = a*b
            print("And ",a,"*",b,"=",c,sep="")
            foundit=True
            break
    if foundit: break
        
print("Part 2")
foundit=False
for line in open('input.txt'):
        a = int(line)
        for line in open('input.txt'):
            b = int(line)
            for line in open('input.txt'):
                c = int(line)
                if a+b+c==2020:
                    print("hurray,",a,"+",b,"+",c,"=2020",sep="")
                    d=a*b*c
                    print("And ",a,"*",b,"*",c,"=",d,sep="")
                    foundit=True
            if foundit: break
        if foundit: break
        
