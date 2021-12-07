length = 0
depth = 0

for line in open('2.in'):
    o, x = line.split()
    x = int(x)
    if ('forward' == o):
        length += x
    elif ('up' == o):
        depth -= x
    elif ('down' == o):
        depth += x
    else :
        print('error')
print(f'part1: {length*depth}')

total = 0
depth = 0
current_depth = 0
for line in open('2.in'):
    o, x = line.split()
    x = int(x)
    if ('forward' == o):
        total += x
        depth += x*current_depth
    elif ('up' == o):
        current_depth -= x
    elif ('down' == o):
        current_depth += x
    else :
        print('error')
print(f'part2: {total*depth}')