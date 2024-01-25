import collections
#8x8 체스판
arr = [list(map(str,input()))for _ in range(8)]
wall = []
for i in range(8):
    for j in range(8):
        if arr[i][j] =="#":
            wall.append([i,j])

#arr[7][0] 시작점 욱제
loc = collections.deque()   
loc.append((7,0))
move = [[0,0],[-1,1],[0,1],[1,1],[1,0],[1,-1],[0,-1],[-1,-1],[-1,0]]

def bfs():
    while(loc):
        stage=0
        if stage ==8:
            return 1
        for _ in range(len(loc)):
            x,y = loc.popleft()
            if [x,y] in wall:
                continue
            if x == 0:
                return 1
            for dx, dy in move:
                ddx = x + dx
                ddy = y + dy
                if ddx>= 0 and ddx<8 and ddy>=0 and ddy<8:
                    if [ddx,ddy] not in wall:
                        loc.append((ddx,ddy))
        for i in range(len(wall)):
            wall[i][0] = wall[i][0] + 1
        stage = stage +1

a=bfs()
if a:
    print(a)
else:
    print(0)