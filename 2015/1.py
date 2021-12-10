floor = 0
count = 0
found = False
for i in open('1.in').read():
    floor+=1 if i == '(' else -1
    if not found:
        count+=1
        if -1==floor:
            found = True
            print(f'part2: {count}')        
print(f'part1: {floor}')


