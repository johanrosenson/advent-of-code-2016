# https://adventofcode.com/2016/day/5
from hashlib import md5

seed = open('input').read()

def get_hash(seed, n):
    return md5('{}{}'.format(seed, n).encode('utf-8')).hexdigest()

def find_next_letter(seed, n):
    while get_hash(seed, n)[:5] != '00000':
        n += 1
    return [n+1, get_hash(seed, n)[5:6]]

def find_password(seed, iterations, n = 0):
    password = ''
    for i in range(iterations):
        [n, letter] = find_next_letter(seed, n)
        password += letter
    return password

password = find_password(seed, 8)

print('Password: {}'.format(password))
