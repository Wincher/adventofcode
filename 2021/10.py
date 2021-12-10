l = ['<', '(', '{', '[']
r = ['>', ')', '}', ']']
s = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137,
}

il = [] #incompleted lines
sum = 0
for line in open('10.in'):
    stack = []
    for x in (list(line.split())):
        interuppted = False
        for i in x:
            if interuppted:
                break
            if (i in l):
                stack.append(i)
            else:
                p = stack.pop()
                if p not in l or l[r.index(i)] != p:
                    sum+=s[i]
                    interuppted = True
        if not interuppted:
            il.append(x)
print(sum)

sc = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4,
}
SUM = []
sum = 0

for line in il:
    sum = 0
    stack = []
    for x in (list(line.split())):
        for i in x:
            if (i in l):
                stack.append(i)
            else:
                p = stack.pop()
    while(stack):
        c = r[l.index(stack.pop())]
        sum = sum * 5 +sc[c]
    SUM.append(sum)
print(sorted(SUM)[len(SUM)//2])