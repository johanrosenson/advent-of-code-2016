# https://adventofcode.com/2016/day/3
import re

triangles = open('input').read().splitlines()

valid = 0

for triangle in triangles:
    [v1, v2, v3] = [int(v) for v in filter(None, re.split(r'\s+', triangle))]
    if v1+v2 > v3 and v2+v3 > v1 and v3+v1 > v2:
        valid += 1

print('Valid triangles: {}'.format(valid))
