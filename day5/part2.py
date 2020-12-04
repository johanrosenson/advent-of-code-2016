# https://adventofcode.com/2016/day/5
from hashlib import md5

seed = open('input').read()

def get_hash(seed, n):
    return md5('{}{}'.format(seed, n).encode('utf-8')).hexdigest()

def find_next_candidate(seed, n):
    h = get_hash(seed, n)
    while h[:5] != '00000':
        n += 1
        h = get_hash(seed, n)
    return [n+1, h[5:6], h[6:7]]

def find_password(seed, iterations, n = 0):
    password = [None] * 8
    while None in password:
        [n, position, letter] = find_next_candidate(seed, n)
        if position in ['0', '1', '2', '3', '4', '5', '6', '7']:
            position = int(position)
            if password[position] == None:
                password[position] = letter
    return ''.join(password)

password = find_password(seed, 8)

print('Password: {}'.format(password))
