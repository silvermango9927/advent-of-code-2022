cal=[sum(map(int, p.split('\n'))) for p in open('Day 1/input.txt', 'r').read().strip().split('\n\n')]
print(cal.index(sorted(cal)[-1]), sorted(cal)[-1])