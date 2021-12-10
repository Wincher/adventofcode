sum = 0
ribbon = 0
for x in open('2.in'):
    n = list(map(int, x.strip().split('x')))
    n.sort()
    x,y,z = n
    ribbon += 2*(x+y)+x*y*z
    sum += (x*y+y*z+z*x)*2+x*y
print(f'part1: {sum}')
print(f'part2: {ribbon}')
