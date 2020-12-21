print('Part 1')


# North +
# South -
# East -j
# West j

# Change of direction:
# 180deg: multiply by -
# 90deg: multiply by -j
# 270deg: multiply by j


ship=(0+0j)
print(type(ship))
print(ship)
direction=-1j
print(type(direction))

for line in open('input.txt'):
    where=line[0]
    howmuch=int(line[1:])
    #print(where,howmuch)
    if where == 'N':
        ship=ship+howmuch
    if where == 'E':
        ship=ship-1j*howmuch
    if where == 'S':
        ship=ship-howmuch
    if where == 'W':
        ship=ship+1j*howmuch
    if where == 'R':
        if howmuch==90:
            direction=direction*(-1j)
        if howmuch==180:
            direction=direction*(-1)
        if howmuch==270:
            direction=direction*(1j)
    if where == 'L':
        if howmuch==270:
            direction=direction*(-1j)
        if howmuch==180:
            direction=direction*(-1)
        if howmuch==90:
            direction=direction*(1j)

    if where == 'F':
        ship=ship+direction*howmuch
# print(ship)
# print(ship.real,ship.imag)
# print(abs(ship.real)+abs(ship.imag))

    
print('Part 2')

#A waypoint is an intermediate point or place on a route or line of travel, a stopping point or point at which course is changed, the first use of the term tracing to 1880. Wikipedia

ship=(0-0j)
waypoint=(1-10j)
direction=-1j

for line in open('input.txt'):
    where=line[0]
    howmuch=int(line[1:])
    print(where,howmuch)

    if where == 'N':
        waypoint=waypoint+howmuch
    if where == 'E':
        waypoint=waypoint-1j*howmuch
    if where == 'S':
        waypoint=waypoint-howmuch
    if where == 'W':
        waypoint=waypoint+1j*howmuch
    if where == 'R':
        if howmuch==90:
            waypoint=waypoint*(-1j)
        if howmuch==180:
            waypoint=waypoint*(-1)
        if howmuch==270:
            waypoint=waypoint*(1j)
    if where == 'L':
        if howmuch==270:
            waypoint=waypoint*(-1j)
        if howmuch==180:
            waypoint=waypoint*(-1)
        if howmuch==90:
            waypoint=waypoint*(1j)

    if where == 'F':
        ship=ship+waypoint*howmuch

    
print(ship)
print(ship.real,ship.imag)
print(abs(ship.real)+abs(ship.imag))

