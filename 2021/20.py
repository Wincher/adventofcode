data = open('../puzzleInput/2021/20.in').read().strip()

alg, lines = data.split('\n\n')
alg = alg.strip()
print(len(alg))
isReversed = alg[0] == '#' and alg[-1] == '.'
print(isReversed)
assert(isReversed)


S = set()
for r,line in enumerate(lines.strip().split('\n')):
    for c,x in enumerate(line.strip()):
        if x=='#':
            S.add((r,c))

# on True means item in S stands for '#' or Flase '.'
def solve(S, on):
    S2 = set()
    r_min,r_max = min([r for r,_ in S]), max([r for r,_ in S])
    c_min,c_max = min([c for _,c in S]), max([c for _,c in S])
    for r in range(r_min-5, r_max+10):
        for c in range(c_min-5, c_max+10):
            result = 0
            bit = 8
            for dr in [-1, 0, 1]:
                for dc in [-1, 0, 1]:
                    if ((r+dr,c+dc) in S) if on == None else ((r+dr,c+dc) in S) == on:
                        result += 2**bit
                    bit -= 1
            if (alg[result]=='#') if on == None else (alg[result]=='#') != on:
                S2.add((r,c))
    return S2
def show(G):
    r_min = min([r for r,c in G])
    r_max = max([r for r,c in G])
    c_min = min([c for r,c in G])
    c_max = max([c for r,c in G])
    print(r_min, r_max, c_min, c_max)
  
    for r in range(r_min-1, r_max+2):
        row = ''
        for c in range(c_min-1, c_max+2):
            row += '#' if (r,c) in G else '.'
        print(row)
show(S) 
print(isReversed, 'isrever')
for i in range(50):
    S = solve(S,i%2==0 if isReversed else None)
    if (i+1)==2:
        print(f'part1: {len(S)}')
    if (i+1)==50:
        print(f'part2: {len(S)}')