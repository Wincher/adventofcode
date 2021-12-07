A = [int(x)for x in open('1.in')]
increase_count = 0
for i in range(1, len(A)):
    if A[i-1] < A[i]:
        increase_count += 1
print(f'part1: {increase_count}')

increase_count = 0
for i in range(3, len(A)):
    if A[i-3] < A[i]:
        increase_count += 1
print(f'part2: {increase_count}')