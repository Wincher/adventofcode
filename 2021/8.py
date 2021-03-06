t = 0
for line in open('../puzzleInput/2021/8.in'):
    a,b = line.split(' | ')
    for x in b.split():
        if len(x) in [2,3,4,7]:
            t+=1
print('part1:', t)

sum = 0
digits = [x for x in 'abcdefg']
for line in open('../puzzleInput/2021/8.in'):
    a,b = line.split(' | ') 
    A={}
    i = 0
    aa = a.split()
    for x in aa:
        if len(x) == 2:
            A[1] = x
            aa.remove(x)
            break
    for x in aa:
        if len(x) == 4:
            A[4] = x
            aa.remove(x)
            break
    for x in aa:
        if len(x) == 3:
            A[7] = x
            aa.remove(x)
            break
    for x in aa:
        if len(x) == 7:
            A[8] = x
            aa.remove(x)
            break
    for x in aa:
        if len(x) == 5:
            diff_letter = [d for d in digits if d not in x]
            if len([d for d in A[1] if d not in x]) == 0:
                A[3] = x
                aa.remove(x)
                break
    for x in aa:
        if len(x) == 6:
            diff_letter = [d for d in digits if d not in x][0]
            if diff_letter not in A[3]:
                A[9] = x
                aa.remove(x)
                break; 
    for x in aa:
        if len(x) == 6:
            diff_letter = [d for d in digits if d not in x][0]
            if diff_letter not in A[1]:
                A[0] = x
                aa.remove(x)
                break
    for x in aa:
        if len(x) == 6:
                A[6] = x
                aa.remove(x)
                break
    for x in aa:
        if len(x) == 5:
            diff_letter = [d for d in digits if d not in x][0]
            if len([d for d in A[6] if d not in x]) == 2:
                A[2] = x
            else:
                A[5] = x
    text = '';    
    for w in b.split():
        for k, v in A.items():
            if (sorted(w) == sorted(v)):
                text += str(k)
    sum += int(text)
print('part2:', sum)
                

#another way for part2 slow but fast in coding
from itertools import *

t = 0
for line in open('../puzzleInput/2021/8.in'):
    b, a = line.strip().split(' | ')
    b = b.split()
    a = a.split()
    origin = ["abcefg", "cf", "acdeg", "acdfg", "bcdf", "abdfg", "abdefg", "acf", "abcdefg", "abcdfg"]
    tr = set(origin)
    for x in permutations('abcdefg'):
        m = {i:j for i, j in zip(x, 'abcdefg')}   
        c = { ''.join(sorted(map(m.get, s))) for s in b}
        if c == tr:
            d = [ ''.join(sorted(map(m.get, s))) for s in a]
            d = ''.join(str(origin.index(st)) for st in d)
            t += int(d)
print('part2:', t)
