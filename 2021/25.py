G = [line.strip() for line in open('../puzzleInput/2021/25.in').readlines()]

R = len(G)
C = len(G[0])
res = 0
while True:
    res += 1
    moved = False
    G1 = [[G[r][c] for c in range(C)] for r in range(R)]
    for i in range(R):
        for j in range(C):
            if G[i][j] == '>':
                if G[i][(j+1)%C] == '.':
                    moved = True
                    G1[i][(j+1)%C] = '>'
                    G1[i][j] = '.'
    G2 = [[G1[r][c] for c in range(C)] for r in range(R)]
    for i in range(R):
        for j in range(C):
            if G1[i][j] == 'v' and G1[(i+1)%R][j] == '.':
                moved = True
                G2[(i+1)%R][j] = 'v'
                G2[i][j] = '.'
    if not moved:
        print(res)
        exit(0)
    G = G2