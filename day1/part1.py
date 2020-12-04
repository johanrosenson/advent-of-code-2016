# https://adventofcode.com/2016/day/1

instructions = open('input').read().split(', ')

# instructions = 'R2, R2, R2'.split(', ')

x = 0
y = 0

nexts = {
    'R': ['north', 'east', 'south', 'west'],
    'L': ['north', 'west', 'south', 'east'],
}

direction = 'north'

for instruction in instructions:
    [turn, steps] = [instruction[:1], instruction[1:]]
    direction = nexts[turn][(nexts[turn].index(direction) + 1) % 4]

    if direction in ['north', 'south']:
        x += (int(steps) * -1, int(steps))[direction == 'north']
    else:
        y += (int(steps) * -1, int(steps))[direction == 'east']

distance = abs(x) + abs(y)
print('Distance {}'.format(distance))
