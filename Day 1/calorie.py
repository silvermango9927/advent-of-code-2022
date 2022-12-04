with open('Day 1/input.txt', 'r') as f:
    data = f.read()

cal=[]
for p in data.strip().split('\n\n'):
    cal.append(sum(map(int, p.split('\n'))))

print(cal.index(sorted(cal)[-1]), sorted(cal)[-1])



