
from typing import DefaultDict

A = DefaultDict(list)
for line in open ('../puzzleInput/2021/12.in'):
    f,t = line.strip().split('-')
    # print(f,t)
    A[f].append(t)
    A[t].append(f)
start = 'start'
end = 'end'
# print(A)
def count(p, visited = set()):
    if p == end:
        return 1
    c = 0
    visited = set(visited)
    if (p.lower()==p):
        visited.add(p)
    for next in A[p]:
        if next in visited:
            continue
        c += count(next, visited)
    return c
print(f'part1: {count(start)}')

def count2(p, visited = set(), twice=False):
    if p == end:
        return 1
    c = 0
    visited = set(visited)
    if (p.lower()==p):
        visited.add(p)
    for next in A[p]:
        if next == start or (next in visited and twice):
                continue
        if next in visited:
           c += count2(next, visited, True) 
        else:
           c += count2(next, visited, twice)
    return c
print(f'part2: {count2(start)}')
