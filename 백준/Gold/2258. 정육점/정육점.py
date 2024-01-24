#덩어리 개수, 필요한 고기 양
N,M = map(int,input().split())

#[무게,가격]배열
arr = [list(map(int,input().split())) for _ in range(N)]

arr.sort(key=lambda x: (x[1], -x[0]))    #sort 가격 오름차순 같으면 무게 내림차순

i=1
we = arr[0][0]  #무게 0
pr = arr[0][1]  #가격 1
if N == 1:
    if we>= M:
        print(pr)
    else: print(-1)
    exit()

check0 = True
while(i<N):
    we += arr[i][0]
    if arr[i-1][1]==arr[i][1]:  #가격이 같으면
        pr += arr[i][1]
    else:
        pr = arr[i][1]
    
    if we >= M:                 #양이 충분하면
        check0 =False
        break
    i=i+1

if check0:
    print(-1)
    exit()

check = True
if arr[i][1]>arr[i-1][1]:       #한개만 구매하고 나머지 덤
    check = False
    print(pr)
else:                           #가격이 같아 두덩이 이상 구매
    for k in range(N):
        if arr[k][1]>arr[i][1]:
            if pr > arr[k][1]:
                print(arr[k][1])
            else:
                print(pr)
            check = False
            break

if check:                       #두덩이 이상 구매 했지만 이거보다 비싼 덩어리가 없는 경우
    print(pr)
