
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


