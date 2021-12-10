from collections import Counter, defaultdict
A = Counter([int(x) for x in open('6.in').read().strip().split(',')])
S = dict(A)
for _ in range(80):
    T = defaultdict(int)
    for day,c in S.items():
        if (day == 0):
            T[6]+=c
            T[8]+=c
        else:
            T[day-1]+=c
    S = T
print(f'part1: {sum(S.values())}')

S = dict(A)
for _ in range(256):
    T = defaultdict(int)
    for day,c in S.items():
        if (day == 0):
            T[6]+=c
            T[8]+=c
        else:
            T[day-1]+=c
    S = T
print(f'part2: {sum(S.values())}')