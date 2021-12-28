import numpy
bits = ''.join(bin(int(x, 16))[2:].zfill(4) for  x in open('../puzzleInput/2021/16.in').read().strip())
print(bits, len(bits))
ver_sum = 0
# packets = []
def deal_result(version, results):
    val = 0
    if version==0:
        return sum(results)
    elif version==1:
        return numpy.prod(results)
    elif version==2:
        return min(results)
    elif version==3:
        return max(results)
    elif version==5:
        assert len(results) == 2
        return 1 if results[0] > results[1] else 0
    elif version==6:
        assert len(results) == 2
        return 1 if results[0] < results[1] else 0
    elif version==7:
        assert len(results) == 2
        return 1 if results[0] == results[1] else 0
    elif version == 4:
        return val
    else:
        1/0
    # print(f'return value: {version}, {results},{val}')
def parse(index):
    global ver_sum
    v = int(bits[index:index+3],2)
    ver_sum+=v
    type = int(bits[index+3:index+6],2)
    # print(f'=======enter with index: {index}, version={v},type={type}')
    if type==4:
        # print('--------------type4 enter----------------')
        pos = index+6
        val = ''
        end = False
        while not end:
            segment = bits[pos:pos+5]
            # print(segment)
            if segment.startswith('0'): end=True
            val+=segment[1:]
            # print(f'segment={segment}, val = {val}')
            pos+=5
            # print(f'pos={pos}, val={val}, segement={segment}')
        # packets.append((v, type, int(val, 2)))
        # print(f'val={int(val,2)}, packets={packets}, pos={pos}, end%={(pos-index)%4}')
        # assert len(bits) - pos < 4
        # print('--------type 4 cal value end--------')
        return pos, int(val,2)
    else:
        if bits[index+6]=='0':
            # print('operator 0 + position + 15')
            l = int(bits[index+7:index+22],2)
            # print(f'bin={bits[index+7:index+22]}, l={int(bits[index+7:index+22],2)}, origin_p = {index+22}')
            origin_p = index+22
            p = index+22
            val = []
            while origin_p+l > p:
                p, v_result = parse(p)
                val.append(v_result)
            # print('for I(0)', l, origin_p+l,bits[origin_p+l:])
            # print('--------exit operator 0--------')
            return origin_p+l, deal_result(type, val)
        else:
            # print('operator 1 + position + 11')
            assert int(bits[index+6])==1
            # print(f'bin={bits[index+7:index+18]}, int={int(bits[index+7:index+18],2)}')
            n = int(bits[index+7:index+18], 2)
            start = index+18
            origin_start = index+18
            # print(start,n)
        
            val = []
            for i in range(n):
                # print(f'---------------enter {i+1} times ------------------')
                p, v_result = parse(start)
                val.append(v_result)
                # print(f'i: {i+1}, p:{p}, parsed area, {bits[start:p]}')
                start = p
            if type == 6:
                print(n)
            # print(bits[start:], 'end')
            # print('----------exit operator 1------')
            return start, deal_result(type, val)
print(f'part2: {parse(0)}')
print(f'part1: {ver_sum}')