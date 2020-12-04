# https://adventofcode.com/2016/day/4
import re

rooms = open('input').read().splitlines()

sector_sum = 0

def calc_checksum(name):
    chars = {}
    for char in sorted(name):
        if char == '-':
            continue
        if chars.get(char) == None:
            chars[char] = 0
        chars[char] += 1
    return ''.join(sorted(chars, key=chars.get, reverse=True)[:5])

for room in rooms:
    [name, sector, checksum] = re.match(r'(.+)-(\d+)\[(.+)\]', room).groups()
    if calc_checksum(name) == checksum:
        sector_sum += int(sector)

print('Sector sum: {}'.format(sector_sum))
