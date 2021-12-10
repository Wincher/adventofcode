import heapq
from collections import deque
BOARD = []
for line in open('9.in'):
    BOARD.append([int(x) for x in list(line.strip())])
len = len(BOARD)
sum = 0
for i in range(len):
    for j in range(len):
        c = BOARD[i][j]
        if i+1 in range(len):
            if BOARD[i+1][j] <= c:
                continue
        if i-1 in range(len):
            if BOARD[i-1][j] <= c:
                continue
        if j+1 in range(len):
            if BOARD[i][j+1] <= c:
                continue
        if j-1 in range(len):
            if BOARD[i][j-1] <= c:
                continue
        c+=1
        sum+=c
print('part1:', sum)

CALED = set()
SUM = []
for i in range(len):
    for j in range(len):
        if (i,j) not in CALED and BOARD[i][j] < 9:
            a = [(i,j)]
            sum = 0
            while(a):
                (ii, jj) = a[0]
                a.remove(a[0])
                if (ii,jj) in CALED:
                    continue
                CALED.add((ii,jj))
                sum += 1
                if ii+1 in range(len):
                    if BOARD[ii+1][jj] < 9:
                        a.append((ii+1, jj))
                if ii-1 in range(len):
                    if BOARD[ii-1][jj] < 9:
                        a.append((ii-1, jj)) 
                if jj+1 in range(len):
                    if BOARD[ii][jj+1] < 9:
                        a.append((ii, jj+1))
                if jj-1 in range(len):
                    if BOARD[ii][jj-1] < 9:
                        a.append((ii, jj-1))
                # print(a)
            SUM.append(sum)
c = 1
for i in heapq.nlargest(3,SUM):
    c*=i
print('part2', c)