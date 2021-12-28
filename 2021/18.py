import ast
filename = '../puzzleInput/2021/18.in'
snailfishes = [ast.literal_eval(line.strip()) for line in open(filename)]

result = None
def add(result, sf):
    return reduce([result, sf])

def reduce(sf):
    changed, sf = explod(sf)
    if changed:
        return reduce(sf)
    else:
        changed, sf = splits(sf)
        if changed:
            return reduce(sf)
        else:
            return sf

def explod(sf):
    sfsl = []
    sf_str = str(sf)
    i = 0
    while i < len(sf_str):
        if sf_str[i].isdigit():
            j=i+1
            while j < len(sf_str) and sf_str[j].isdigit():
                j+=1
            sfsl.append(sf_str[i:j])
            i=j
        else:
            sfsl.append(sf_str[i])
            i+=1
    depth = 0
    for i, c in enumerate(sfsl):
        if c=='[':
            depth+=1
            if depth > 4: 
                r_index = i+4
                l, r = sfsl[i+1], sfsl[r_index]
                assert l.isdigit()
                assert r.isdigit()
                for j in reversed(range(i)):
                    if sfsl[j].isdigit():
                        sfsl[j] = str(int(sfsl[j])+int(l))
                        break
                for j in range(r_index+1, len(sfsl)):
                    if sfsl[j].isdigit():
                        sfsl[j] = str(int(sfsl[j])+int(r))
                        break
                for j in range(i, r_index+2):
                    sfsl[j] = ''
                sfsl[i] = '0'
                return True, ast.literal_eval(''.join(sfsl))
        elif c==']':
            depth-=1
            pass
        elif c.isdigit():
            pass
        elif c==',':
            pass
        elif c==' ':
            pass
        else:
            assert False
    return False, sf

def splits(sf):
    sfsl = list(str(sf))
    for i, c in enumerate(sfsl):
        if c=='[':
            pass
        elif c==']':
            pass
        elif c.isdigit():
            if sfsl[i+1].isdigit():
                n = int(''.join(sfsl[i:i+2]))
                sfsl[i] = f'[{n//2},{(n+1)//2}]'
                sfsl[i+1]=''
                return True, ast.literal_eval(''.join(sfsl))
        elif c==',':
            pass
        elif c==' ':
            pass
        else:
            assert False
    return False, sf

def magnitude(res):
    if isinstance(res, list):
        return 3*magnitude(res[0])+2*magnitude(res[1])
    else:
        assert isinstance(res, int)
        return res
    
for snailfish in snailfishes:
    if not result:
        result = snailfish
        continue
    result = add(result, snailfish)

sum = 0
for x in snailfishes:
    for y in snailfishes:
        if x is y:
            continue
        sum = max(sum, magnitude(add(x,y)))

print(f'part1: {magnitude(result)}')
print(f'part2: {sum}')