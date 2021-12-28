import heapq

n = 5
_R = [list(map(int, line.strip())) for line in open('../puzzleInput/2021/15.in')]
R = [[ 0 for _ in range(len(_R[0]*n))] for _ in range(len(_R)*n)]
r = len(_R)
c = len(_R[0])
# print(R,r,c)
for i in range(len(R)):
    for j in range(len(R[0])):
        R[i][j]=(_R[i%r][j%c]+i//c+j//r-1)%9+1
visited = [[ 0 for _ in range(len(R[0]))] for _ in range(len(R))]
heap = [(0,0,0)]

# while True:
#     rf, x, y = heapq.heappop(heap)
#     if visited[x][y]: continue
#     if (x, y) == (len(R) - 1, len(R[x]) - 1):
#         print(rf)
#         exit(0)
#     visited[x][y] = 1
#     for nx, ny in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
#         if not len(R) > nx >= 0 <= ny < len(R[0]): continue
#         if visited[nx][ny]: continue
#         heapq.heappush(heap, (rf + R[nx][ny], nx, ny))

while True:
    risk, x, y = heapq.heappop(heap)
    # print(risk,(x,y),heap)
    if visited[x][y]: continue
    if x==len(R)-1 and y == len(R[0])-1:
        print('result:', risk)
        exit()
    visited[x][y]=True
    if x+1 in range(len(R)):
        if not visited[x+1][y]: 
            heapq.heappush(heap, (risk+R[x+1][y],x+1,y))
    if y+1 in range(len(R[0])):
        if not visited[x][y+1]: 
            heapq.heappush(heap, (risk+R[x][y+1],x,y+1))
    if x-1 in range(len(R)):
        if not visited[x-1][y]:
            heapq.heappush(heap, (risk+R[x-1][y],x-1,y))
    if y-1 in range(len(R[0])):
        if not visited[x][y-1]: 
            heapq.heappush(heap, (risk+R[x][y-1],x,y-1))

# result = []
# def slow_solve(p=(0,0),t=0):
#     print(t, p, r, c)
#     xx,yy = p 
#     if p != (0,0):
#         print(t, 'before')
#         t += R[xx][yy]
#         print(t, 'after')
#     if xx==r-1 and yy == c-1:
#         print('GOT', t, p)
#         result.append(t)
#         return
#     if xx+1 in range(r):
#         slow_solve((xx+1,yy), t)
#     if yy+1 in range(c):
#         slow_solve((xx,yy+1), t)

# slow_solve(p=(0,0), t=0)
# print(min(result), 'a')
