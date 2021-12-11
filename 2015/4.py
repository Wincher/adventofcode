import hashlib
secret = 'iwrupvqb'
i = 0
while True:
    a = hashlib.md5((secret + str(i)).encode())
    if str(a.hexdigest()).startswith('00000'):
        print(f'part1: {i}')
        break
    i += 1
while True:
    a = hashlib.md5((secret + str(i)).encode())
    if str(a.hexdigest()).startswith('000000'):
        print(f'part2: {i}')
        break
    i += 1