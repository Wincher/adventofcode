A = [line.strip() for line in open('3.in')]
width = len(A[0])
M = [0 for _ in range(width)]
for x in A:
    for i, c in enumerate(x):
        M[i] += int(1 if '1' == c else -1)
gamma = ''
epsilon = ''
for x in M:
    gamma += '1' if x > 0 else '0'
    epsilon += '0' if x > 0 else '1'
print('part1:', int(gamma, 2)*int(epsilon,2))

OX = A
CO2 = A
for i in range(width):
    if len(OX) > 1:
        c0 = len([x for x in OX if x[i] == '0']) 
        c1 = len([x for x in OX if x[i] == '1']) 
        if c1>=c0:
           OX = [x for x in OX if x[i] == '1']
        else:
           OX = [x for x in OX if x[i] == '0']
    if len(CO2) > 1:
        c0 = len([x for x in CO2 if x[i] == '0']) 
        c1 = len([x for x in CO2 if x[i] == '1']) 
        if c1>=c0:
           CO2 = [x for x in CO2 if x[i] == '0']
        else:
           CO2 = [x for x in CO2 if x[i] == '1']
print('part2:', int(OX[0],2)*int(CO2[0],2))
