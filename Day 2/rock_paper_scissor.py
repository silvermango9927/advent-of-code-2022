points=0
for line in open("Day 2/input.txt", "r").read().splitlines():
    line=line.replace('X', 'A').replace('Y', 'B').replace('Z', 'C').split(' ')
    if line[0]==line[1]:
        points+=3
    elif (line[0]=='A' and line[1]=='B') or (line[0]=='B' and line[1]=='C') or (line[0]=='C' and line[1]=='A'):
        points+=6
    if line[1]=='A':
            points+=1
    elif line[1]=='B':
            points+=2
    elif line[1]=='C':
            points+=3
print(points)