A = []
for line in open('3.in'):
    line = line.strip()
    A.append(line)

width = len(A[0])
V = [[0 for _ in range(width)] for _ in range(2)]
print(A)
print(width)
print(V)
for x in A:
    print(list(enumerate(x)))
    for i, c in enumerate(x):
        print(f'{i}:' + c)
