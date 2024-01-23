#리스트길이
n = int(input())
#리스트
arr = list(map(int,input().split()))

val = arr[0]    #제일 큰 수
sum = 0    #묶음 합

for i in range(n):

    if arr[i]>=0 and sum >=0:   #양수
        sum += arr[i]
    elif arr[i]>=0 and sum <0:
        sum = arr[i]

    if arr[i] < 0 and sum >=0:  #음수
        sum += arr[i]
    elif arr[i]<0 and sum <0:
        sum = arr[i]

    if val<sum:                 #큰 수 저장
        val = sum

print(val)