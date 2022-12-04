# Reading the file, and calculating the total calories
cal=[sum(map(int, p.split('\n'))) for p in open('Day 1/input.txt', 'r').read().strip().split('\n\n')]
# Printing position of the elf and the total number of calories
print(cal.index(sorted(cal)[-1]), sorted(cal)[-1])
### WON MY FIRST GOLD STAR WOOHOO !