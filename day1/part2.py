# https://adventofcode.com/2016/day/1
from collections import defaultdict

instructions = open('input').read().split(', ')

coord = {'x': 0, 'y': 0}
visits = defaultdict(int)

nexts = {
    'R': ['north', 'east', 'south', 'west'],
    'L': ['north', 'west', 'south', 'east'],
}

direction = 'north'

for instruction in instructions:
    [turn, steps] = [instruction[:1], instruction[1:]]
    direction = nexts[turn][(nexts[turn].index(direction) + 1) % 4]

    if direction in ['north', 'south']:
        axis = 'x'
    else:
        axis = 'y'

    axis_direction = (-1, 1)[direction in ['north', 'east']]

    for n in range(int(steps)):
        coord[axis] += axis_direction
        coord_key = '{}x{}'.format(coord['x'], coord['y'])
        visits[coord_key] += 1
        if visits[coord_key] > 1:
            break

    if visits[coord_key] > 1:
            break

distance = abs(coord['x']) + abs(coord['y'])
print('Distance {}'.format(distance))
