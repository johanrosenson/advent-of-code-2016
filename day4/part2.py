# https://adventofcode.com/2016/day/4
import re

rooms = open('input').read().splitlines()

def calc_checksum(name):
    chars = {}
    for char in sorted(name):
        if char == '-':
            continue
        if chars.get(char) == None:
            chars[char] = 0
        chars[char] += 1
    return ''.join(sorted(chars, key=chars.get, reverse=True)[:5])

def decrypt_name(name, offset = 2, charmap = 'abcdefghijklmnopqrstuvwxyz'):
    decrypted = ''
    for char in name:
        if char == '-':
            decrypted += ' '
            continue

        decrypted += charmap[(charmap.index(char)+offset) % len(charmap)]
    return decrypted

for room in rooms:
    [name, sector, checksum] = re.match(r'(.+)-(\d+)\[(.+)\]', room).groups()
    if calc_checksum(name) == checksum:
        decrypted_name = decrypt_name(name, int(sector))
        if 'north' in decrypted_name:
            print(decrypted_name, sector)
            exit()
