
from typing import Counter

A = ''
lines = []
for line in open('../puzzleInput/2021/14.in'):
        if not A:
            # A = [x for x in line.strip()]
            A = line
        else:
            if not line.strip(): continue
            lines.append(line.strip())
c = Counter()
for i in range(len(A)-2):
    c[A[i:i+2]]+=1
for i in range(40):
    c_temp = Counter()
    for line in lines:
        # print(line)
        s, t = line.strip().split(' -> ')
        for item in c:
            if item==s:
               c_temp[s[0]+t] += c[s]
               c_temp[t+s[1]] += c[s]
               c_temp[s] += -c[s]
            #    print(c_temp, s)
    c+=c_temp
# print(c)
count = Counter()
for item in c:
    count[item[0]]+=c[item]
count[A.strip()[-1]]+=1
print(max(count.values())-min(count.values()))
    
# too slow
# for i in range(40):
#     insert = []
#     for line in lines:
#         for ii in range(len(A)-1):
#             if not line.strip(): continue
#             s, t = line.strip().split(' -> ')
#             s1,s2 = [aa for aa in s]
#             u=s1+t+s2
#             a = A[ii:ii+2]
#             if a==s:
#                 insert.append((ii,t))
#     AA = [c for c in A.strip()]
#     AAA = []
#     insert = dict(insert)
#     # print(insert, AA)
#     inc = 0
#     for iii in range(len(AA)):
#         AAA.append(AA[iii])
#         if iii in insert:
#             AAA.append(insert[iii])
#     A = ''.join(AAA)
#     # print(A, i+1)
# counter = Counter(A)
# print(counter)