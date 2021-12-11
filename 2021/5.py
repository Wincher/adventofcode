from collections import defaultdict
from typing import defaultdict

M = defaultdict(int)
M2 = defaultdict(int)
for line in open('../puzzleInput/2021/5.in'):
    str1,str2 = line.split('->')
    x1,y1 = str1.strip().split(',')
    x2,y2 = str2.strip().split(',')
    x1 = int(x1)
    y1 = int(y1)
    x2 = int(x2)
    y2 = int(y2)
    # print(f'{x1}, {y1} -> {x2}, {y2}')
    if x1 == x2 or y1 == y2 or abs(x1-x2) == abs(y1-y2):
        if (x1 == x2):
            for i in range(min(y1, y2), max(y1, y2)+1):
                M[(x1,i)] += 1
                M2[(x1,i)] += 1
        elif (y1 == y2):
            for i in range(min(x1, x2), max(x1, x2)+1):
                M[(i,y1)] += 1
                M2[(i,y1)] += 1
        else:
            # print('GOT')
            for i in range(abs(x1-x2)):
                l =  True if x1-x2 < 0 else False
                t =  True if y1-y2 < 0 else False
                xx = x1 + (i if l else -i)
                yy = y1 + (i if t else -i)
                # print(l, t, xx, yy, i)
                M2[(xx,yy)] += 1
print('part1:', len([x for x in M if M[x] > 1]))
print('part2:', len([x for x in M2 if M2[x] > 1]))
