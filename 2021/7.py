A = [ int(x) for x in open('7.in').read().split(',')]
print(A)
SUM = []

for i in range(min(A), max(A)):
    t = 0
    for x in A:
        t += abs(x-i)
    SUM.append(t)
print('part1:', min(SUM))

SUM = []
def count(d):
    return d*(d+1)/2
for i in range(min(A), max(A)):
    t = 0
    for x in A:
        #t += sum(range(abs(i-x)))
        t += int(count(abs(x-i)))
    SUM.append(t)
print('part2:', min(SUM))