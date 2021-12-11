
from typing import Counter
import re

vowels = ['a','e','i','o','u']
forbidden = ['ab','cd','pq','xy']
count = 0
for line in open('../puzzleInput/2015/5.in'):
    f_ok = False
    for f in forbidden:
        if f in line:
            f_ok = True 
            break
    if f_ok:
        continue
    c = Counter([ x for x in line.strip()])
    v_count = 0
    for v in vowels:
        v_count+=c[v]
    if v_count<3:
        continue
    if re.search(r'(\w)\1', line):
        count+=1
print(f'part1: {count}')

count = 0
for line in open('../puzzleInput/2015/5.in'):
    line = line.strip()
    ok = False
    for i in range(len(line)-2):
        if line[i]==line[i+2]:
            ok = True
            break
    if not ok:
        continue
    ww = {}
    for i in range(len(line)-1):
        if line[i:i+2] in ww.keys() and i-ww[line[i:i+2]]>1:
           count+=1 
           break
        else:
            ww[line[i:i+2]]=i
print(f'part2: {count}')