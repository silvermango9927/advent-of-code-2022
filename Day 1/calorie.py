# Reading the file, and calculating the total calories
cal=[sum(map(int, p.split('\n'))) for p in open('Day 1/input.txt', 'r').read().strip().split('\n\n')]
# Printing position of the elf and the total number of calories (part 1)
print(cal.index(sorted(cal)[-1]), sorted(cal)[-1])
# Part 2
print(sum(sorted(cal)[-3:]))

