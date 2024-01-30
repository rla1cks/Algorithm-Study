#체력 20, 공격력 2, 방어력 2
N, M = map(int,input().split())
#판
arr=[list(map(str,input())) for _ in range(N)]
#커맨드
cmd=list(map(str,input()))

mon=0
item=0
ca=0
cb=0
for i in range(N):
    for j in range(M):
        if arr[i][j]=='&' or arr[i][j]=='M':
            mon += 1
        elif arr[i][j]=='B':
            item +=1
        elif arr[i][j]=='@':
            ca=i
            cb=j
inita=ca
initb=cb
#몬스터
ml=[list(input().split()) for _ in range(mon)]  #R(a) C(b) S(name) W(att) A(def) H(hp) E(exp)
#아이템
il=[list(input().split()) for _ in range(item)]

Lv = 1
Hp = 20
Att= 2
Def=2
Exp=0
wep=0
arm=0
obj=[]
turns=0
Dead=False

def ending():
    fhp = 20+(Lv-1)*5
    fexp = Lv*5
    for i in range(N):
        for j in range(M):
            print(arr[i][j],end='')
        print()
    global Hp
    if Hp<0:
        Hp = 0
    print(f'Passed Turns : {turns}')
    print(f'LV : {Lv}')
    print(f'HP : {Hp}/{fhp}')
    print(f'ATT : {Att}+{wep}')
    print(f'DEF : {Def}+{arm}')
    print(f'EXP : {Exp}/{fexp}')
    if Dead:
        print(f'YOU HAVE BEEN KILLED BY {Dead}..')

arr[ca][cb] ='.'
for i in cmd:
    #print(Lv,Hp,turns)
    turns +=1
    if Dead:
        ca= inita 
        cb= initb
        Hp= 20+(Lv-1)*5
        Dead=False
    da=ca
    db=cb
    if i=='L':
        db-=1
    elif i=='R':
        db+=1
    elif i=='U':
        da-=1
    elif i=='D':
        da+=1
    if da>=N or da<0 or db>=M or db<0:  #out of range check
        if arr[ca][cb] =='^':
            if 'DX' in obj: 
                Hp -=1
            else: Hp -=5
            if Hp <=0:                      #나 사망
                if 'RE' in obj:
                    obj.remove('RE')
                    Dead = 'SPIKE TRAP'
                    continue
                Dead = 'SPIKE TRAP'
                ending()
                exit()
        continue
    if arr[da][db] =='.':               #통로
        pass                            ########3pass
    elif arr[da][db] =='#':             #벽
        if arr[ca][cb] =='^':
            if 'DX' in obj: 
                Hp -=1
            else: Hp -=5
        if Hp <=0:                      #나 사망
            if 'RE' in obj:
                obj.remove('RE')
                Dead = 'SPIKE TRAP'
                continue
            Dead = 'SPIKE TRAP'
            ending()
            exit()
        continue                        #continue 위치이동x
    elif arr[da][db] =='^':             #트랩
        if 'DX' in obj: 
                Hp -=1
        else: Hp -=5
        if Hp <=0:                      #나 사망
            if 'RE' in obj:
                obj.remove('RE')
                Dead = 'SPIKE TRAP'
                continue
            Dead = 'SPIKE TRAP'
            ending()
            exit()
    elif arr[da][db] =='&'or arr[da][db] =='M':                         #몬스터
        if 'HU' in obj and arr[da][db] =='M':
            Hp = 20 + (Lv-1)*5
        for R, C, S, W, A, H, E in ml:
            if R==str(da+1) and C==str(db+1):
                h=int(H)
                round=True

                while(True):
                    if 'CO' in obj and 'DX' in obj and round:           #co, dx 아이템 있을경우*3
                        h=h-(max(1,(Att+wep)*3-int(A)))
                    elif 'CO' in obj and 'DX' not in obj and round:     #co만 있을경우 *2
                        h=h-(max(1,(Att+wep)*2-int(A)))
                    else:                                               #없을 경우 공격
                        h=h-(max(1,(Att+wep-int(A))))
                    if h<=0:                    #몬스터 사망 , 계산 후 break
                        if 'HR' in obj:
                            Hp +=3
                            if Hp >20 + (Lv-1)*5:
                                Hp = 20 + (Lv-1)*5
                        if 'EX' in obj:
                            Exp += int(int(E)*1.2)
                        else:
                            Exp += int(E)
                        if Exp >= Lv*5:
                            Lv +=1
                            Exp = 0
                            Att +=2
                            Def +=2
                            Hp= 20+(Lv-1)*5
                        ca = da
                        cb = db
                        if arr[da][db] =='M':
                            arr[da][db]='@'
                            ending()
                            print('YOU WIN!')    #####3경험치, 레벨 
                            exit()
                        arr[da][db]='.'
                        break
                    #공격턴 끝 몬스터 공격턴
                    if 'HU' in obj and arr[da][db] =='M' and round:
                        round = False
                        continue
                    Hp = Hp - max(1,(int(W)-(Def+arm)))
                    if Hp <=0:                      #나 사망
                        if 'RE' in obj:
                            obj.remove('RE')
                            Dead = S
                            break
                        Dead = S
                        ending()
                        exit()
                    round = False
    elif arr[da][db] =='B':                     #아이템칸
        for R, C, T, S in il:
            if R==str(da+1) and C==str(db+1):
                if T =='W':
                    wep = int(S)
                elif T =='A':
                    arm = int(S)
                elif T =='O':
                    if S not in obj and len(obj)<4:
                        obj.append(S)
        arr[da][db]='.'
    ca = da
    cb = db

arr[ca][cb] ='@'
ending()
if not Dead:
    print('Press any key to continue.')