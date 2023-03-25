Excep=False
n,m = map(int,input().split())
Know=list(map(int,input().split()))
party=[[] for _ in range(m)]

if(len(Know)==1):
    Excep=True
    Know.insert(1,0) #뒤 계산에서 out of range를 방지하기 위한 허수
parent=[0]*(n+1)

for i in range(n+1): #대표노드 값을 나타내는 리스트
    parent[i]=i

def find(a):
    if(parent[a]== a):
        return a
    else:
        parent[a]=find(parent[a])
        return parent[a]

def union(a,b):
    a= find(a)
    b = find(b)
    if(a != b):
        if( a>b):
            parent[a]=b
        else:
            parent[b]=a

if(not Excep):   #아는사람이 1명이라도 있을때, 실행 -Exception 방지
    for i in range(1,len(Know)):
        union(Know[1],Know[i]) #아는사람들 한 집합으로 묶기

cnt=0 #답
for i in range(m):
    party[i]=list(map(int,input().split())) #파티에 오는 사람들 담기

for i in range(m):
    for j in range(1,len(party[i])): #일반적인 상황
        union(party[i][1],party[i][j])

for i in range(m):
    if (len(party[i]) == 1):  # 파티에 오는 사람이 없으면, 무조건 파티 참가 가능하므로 예외로 추가
        cnt += 1
    else:
        if (find(Know[1]) != find(party[i][1])):
            cnt += 1

if(Excep): #아는 사람이 한명도 없으면, 파티 개수만큼 출력
    print(m)
else:
    print(cnt)



