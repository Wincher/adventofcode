p1, p2 = 8,9
times,die,s1,s2 = 0,0,0,0
sides = 100

while True:
    for _ in range(3):
        die = (die)%(sides)+1
        p1 = (p1+die-1)%10+1
        times+=1
    s1 += p1
    if s1>=1000:
        break
    for _ in range(3):
        die = (die)%(sides)+1
        p2 = (p2+die-1)%10+1
        times+=1
    s2 += p2
    if s2>=1000:
        break
print(f'part1: {min(s1,s2)*times}')

p1,p2 = 8,9
sides = [1,2,3]
cache = {}
def solve(p1, p2, s1, s2):
    # print(f'---------start sovle with p1 {p1}, p2 {p2}, s1 {s1}, s2 {s2}-----------')
    if s1 >= 21:
        return (1,0)
    if s2 >= 21:
        return (0,1)
    if (p1, p2, s1, s2) in cache:
        # print(f'in dp,key  {(p1,p2,s1,s2)}, value {cache[(p1, p2, s1, s2)]}, len:{l}, total:{ll}')
        return cache[(p1, p2, s1, s2)]
    count = (0,0)
    for x in sides:
        for y in sides:
            for z in sides:
                # print(f'in for loop x:{x}, y:{y}, z:{z}')
                p1_ = (p1+x+y+z-1)%10+1
                s1_ = s1 + p1_
                # print(f'invoke p2={p2}, p1_={p1_}, s2={s2}, s1_={s1_}')
                x_, y_ = solve(p2, p1_, s2, s1_)
                # print(f'invoke p2={p2}, p1_={p1_}, s2={s2}, s1_={s1_} return value x_={x_} y_={y_}')
                count = (count[0]+y_, count[1]+x_)
                # print(cache)
    cache[(p1, p2, s1, s2)] = count
    return count
print(f'part2: {max(solve(p1,p2,0,0))}')