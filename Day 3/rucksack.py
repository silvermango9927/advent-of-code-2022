sum=0
for line in open('Day 3/input.txt', 'r').readlines():
        sum+= ord((set(line.strip()[:len(line)//2]).intersection(set(line.strip()[len(line)//2:]))).pop())-65+27 if (set(line.strip()[:len(line)//2]).intersection(set(line.strip()[len(line)//2:]))).pop().isupper() else ord((set(line.strip()[:len(line)//2]).intersection(set(line.strip()[len(line)//2:]))).pop())-97+1
        print(sum)