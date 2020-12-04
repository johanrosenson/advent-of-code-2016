# https://adventofcode.com/2016/day/2
from designs import classic as design
from functions import crack

code = crack(open('input').read().splitlines(), design)

print(code)
