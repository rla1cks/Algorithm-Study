from collections import deque
#접시의 수, 초밥 가짓수, 연속해서 먹는 접시의 수, 쿠폰 번호
N,d,k,c = map(int,input().split())
arr = list(int(input()) for _ in range(N))
#먹은 접시 저장
ad=[0]*(d+1)
#먹은 가짓수
mn=0; cnt=0
for i in range(k):
    ad[arr[i]] +=1
    if ad[arr[i]]==1:
        mn+=1
if ad[c]==0:
    mn+=1
cnt=mn

for i in range(N):
    ad[arr[i]] -=1
    if ad[arr[i]]==0 and arr[i] !=c :
        mn-=1
    kk = i+k
    if kk>=len(arr):
        kk = kk-len(arr)
    ad[arr[kk]] +=1
    if ad[arr[kk]]==1 and arr[kk] != c:
        mn+=1
    if mn>cnt:
        cnt=mn
print(cnt)