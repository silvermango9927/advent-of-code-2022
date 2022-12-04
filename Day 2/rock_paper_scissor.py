# Part 1
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

# Part 2
points=0
map_input = {'A': 'Rock', 'B': 'Paper', 'C': 'Scissors', 'X': 'Lose', 'Y': 'Draw', 'Z': 'Win'}
points_per_shape = {'Rock': 1, 'Paper': 2, 'Scissors': 3}
points_per_outcome = {'Lose': 0, 'Draw': 3, 'Win': 6}

for line in open("Day 2/input.txt", "r").read().splitlines():
    opponent_shape = map_input[line[0]]
    our_goal = map_input[line[2]]

    if (opponent_shape, our_goal) in [('Rock', 'Draw'), ('Paper', 'Lose'), ('Scissors', 'Win')]:
        points+= points_per_outcome[our_goal] + points_per_shape['Rock']
    elif (opponent_shape, our_goal) in [('Rock', 'Win'), ('Paper', 'Draw'), ('Scissors', 'Lose')]:
        points+= points_per_outcome[our_goal] + points_per_shape['Paper']
    else:
        points+= points_per_outcome[our_goal] + points_per_shape['Scissors']
print(points)