print("Part 1")
counter=0
passport=1

searchfor={'byr:':False,'iyr:':False,'eyr:':False,'hgt:':False,'hcl:':False,'ecl:':False,'pid:':False}
for line in open('input.txt'):
    if line == '\n':
        passport=passport+1
        if searchfor['byr:'] and searchfor['iyr:'] and searchfor['eyr:'] and searchfor['hgt:'] and searchfor['hcl:'] and searchfor['ecl:'] and searchfor['pid:']:
                counter=counter+1
        for item in searchfor:
            searchfor[item]=False
        
    for item in searchfor:
#         print(item)
        if item in line:
#             print("yeah")
            searchfor[item]=True
        
    
print('Valid passports:',counter)         
print('Total passports:',passport)               


print("Part 2")
counter=0
passport=1

searchfor={'byr:':False,'iyr:':False,'eyr:':False,'hgt:':False,'hcl:':False,'ecl:':False,'pid:':False}
for line in open('input.txt'):
    if line == '\n':
        passport=passport+1
        if searchfor['byr:'] and searchfor['iyr:'] and searchfor['eyr:'] and searchfor['hgt:'] and searchfor['hcl:'] and searchfor['ecl:'] and searchfor['pid:']:
                counter=counter+1
        for item in searchfor:
                searchfor[item]=False
             
            
    a = line.split()
    for item in searchfor:
        matching = [s for s in a if item in s]
        if not matching ==[]:
            matching2 = (str(matching[0]).split(":")[1]) 
            
            if item == 'byr:':
                 if int(matching2) >=1920 and int(matching2) <=2002:
                        searchfor[item]=True
            if item == 'iyr:':
                 if int(matching2) >=2010 and int(matching2) <=2020:
                        searchfor[item]=True
            if item == 'eyr:':
                if int(matching2) >=2020 and int(matching2) <=2030:
                        searchfor[item]=True
            if item == 'hgt:':
                if matching2[-2:] == 'in':
                    if int(matching2[:-2]) >=59 and int(matching2[:-2]) <= 76:
                        searchfor[item]=True
                if matching2[-2:] == 'cm':
                    if int(matching2[:-2]) >=150 and int(matching2[:-2]) <= 193:   
                        searchfor[item]=True
            if item == 'hcl:':
                if matching2[0] == '#' and len(matching2) == 7:
                    searchfor[item]=True
                    i=1
                    allowed = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
                    while i<=6:
                        matching3 = [s for s in allowed if matching2[i] == s]
                        if matching3 == []:
                            searchfor[item]=False
                        i=i+1
            if item == 'ecl:':
                allowed2 = ['amb','blu','brn','gry','grn','hzl','oth']
                for s in allowed2:
                    if matching2 == s:
                        searchfor[item]=True
            if item == 'pid:':
                    if len(matching2) == 9:
                        searchfor[item]=matching2.isdigit()
        
print('Valid passports:',counter)         
print('Total passports:',passport)         


