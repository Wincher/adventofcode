l = ['<', '(', '{', '[']
r = ['>', ')', '}', ']']
s = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137,
}
sc = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4,
}
SUM = []
sum = 0

il = [] #incompleted lines
sum = 0
for line in open('../puzzleInput/2021/10.in'):
    sum2 = 0
    stack = []
    interuppted = False
    for x in line.strip():
        if interuppted:
            break
        if (x in l):
            stack.append(x)
        else:
            p = stack.pop()
            if p not in l or l[r.index(x)] != p:
                sum+=s[x]
                interuppted = True
    if not interuppted:
        while(stack):
            c = r[l.index(stack.pop())]
            sum2 = sum2 * 5 +sc[c]
        SUM.append(sum2)
print(f'part1: {sum}')
print(f'part2: {sorted(SUM)[len(SUM)//2]}')