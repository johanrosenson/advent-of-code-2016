# https://adventofcode.com/2016/day/3
import re

lines = open('input').read().splitlines()

valid = 0

def triangles(lines):
    triangles = []

    stack = [];

    for line in lines:
        [v1, v2, v3] = [int(v) for v in filter(None, re.split(r'\s+', line))]
        stack.append([v1, v2, v3])
        if len(stack) == 3:
            for i in range(3):
                triangles.append('{} {} {}'.format(stack[0][i], stack[1][i], stack[2][i]))
            stack = []

    return triangles

for triangle in triangles(lines):
    [v1, v2, v3] = [int(v) for v in filter(None, re.split(r'\s+', triangle))]
    if v1+v2 > v3 and v2+v3 > v1 and v3+v1 > v2:
        valid += 1

print('Valid triangles: {}'.format(valid))
