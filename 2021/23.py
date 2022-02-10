#############
#...........#
###C#A#B#D###
  #D#C#B#A#
  #D#B#A#C#
  #C#A#D#B#
  #########
import heapq
data = '''
CDDC
ACBA
BBAD
DACB
'''

costs = {'A':1, 'B':10, 'C':100, 'D':1000,}
rooms = [*map(list, data.split())]
depth = len(rooms[0])
start = (0, ['.']*11, rooms)
end = [[x]*depth for x in 'ABCD']

def steps(state):
    res = []
    # move out from rooms
    for x, (i, room) in zip([2,4,6,8], enumerate(state[2])):
        # print(x,i, room, 'x i room')
        if not room:
            continue
        q = []
        for nx in range(x, 11):
            if state[1][nx]!='.':
                break
            q.append(nx)
        for nx in range(x-1, -1, -1):
            if state[1][nx]!='.':
                break
            q.append(nx)
        for j in q:
            if j in [2,4,6,8]:
                continue
            ns = state[1][:]
            ns[j] = room[0]
            nr = [ r[:] for r in state[2]]
            nr[i].pop(0)
            cost = state[0]+costs[room[0]]*(depth+1-len(room))+costs[room[0]]*abs(j-x)
            res.append([cost, ns, nr])
        # print(res, 'res', q, 'q')
    # move in rooms
    for i in range(11):
        if state[1][i]=='.': 
            continue
        q = []
        for nx in range(i+1, 11):
            if state[1][nx]!='.':
                break
            q.append(nx)
        for nx in range(i-1, -1, -1):
            if state[1][nx]!='.':
                break
            q.append(nx)
        for j in q:
            if j in [2,4,6,8]:
                ind = 'ABCD'.find(state[1][i])
                if (ind+1)*2==j:
                    if all(x==state[1][i] for x in state[2][ind]):
                        ns = state[1][:]
                        ns[i] = '.'
                        nr = [r[:] for r in state[2]]
                        nr[ind].insert(0, state[1][i])
                        cost = state[0]+costs[state[1][i]]*(depth+1+abs(i-j)-len(nr[ind]))
                        res.append([cost, ns, nr])
    return res

def c(state):
    return (tuple(state[1]), tuple(map(tuple, state[2])))

DP = [start]
visted = set()
while DP:
    state = heapq.heappop(DP)
    cc = c(state)
    if cc in visted:
        continue
    visted.add(cc)
    if state[2] == end:
        print(state[0])
        break
    for k in steps(state):
        if c(k) in visted:
            continue
        heapq.heappush(DP, k)