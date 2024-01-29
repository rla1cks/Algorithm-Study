N, M = map(int, input().split())
np = []

for i in range(N):
    a, b = map(int, input().split())
    ar = list(map(int,input().split()))
    
    if a<b:
        np.append(1)
    elif b==a:
        np.append(min(ar))
    elif b<a:
        ar.sort(reverse=True)
        np.append(ar[b-1])
    
np.sort()
point=0

if N == 0:
    print(0)
    exit()
for i in range(N):
    point += np[i]
    if point>M:
        print(i)
        exit()

print(N)