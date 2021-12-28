
filename = '../puzzleInput/2021/17.in'
a = open(filename).read().strip().split(':')[1].strip().split(',')
x,y = a
x = x.split('=')[1].split('..')
y = y.split('=')[1].split('..')
x_min, x_max = (int(x[0]), int(x[1]))
y_max, y_min = (int(y[0]), int(y[1]))
# print(x_min, x_max, y_min, y_max)

sum = 0
max_h = 0
magic_value = 250
for ii in range(1,x_max+1):
    for jj in range(y_max-1, magic_value):
        S = (0,0)
        i = ii
        j = jj
        probes = [S]
        missed = False
        while True:
            S = (S[0]+i, S[1]+j)  
            if S[0] > x_max or S[1] < y_max: 
                missed = True
                # print('missed target area')
                break
            if S[0] in range(x_min, x_max+1) and S[1] in range(y_max, y_min+1):
                # print('into target area', S)
                sum+=1
                break
            else:
                probes.append(S)
            i = 0 if i-1 < 0 else i-1
            j-=1
        if not missed:
            # print(S, i,j , f'max: {max(probes, key=itemgetter(1))}')
            max_h = max(max_h, max(probes, key=lambda item:item[1])[1])
print(f'part1: {max_h}')
print(f'part2: {sum}')