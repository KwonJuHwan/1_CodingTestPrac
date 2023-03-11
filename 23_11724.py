import sys
sys.setrecursionlimit(10000) #재귀함수를 사용할때 필수인 조건(default가 1000이라 많은 데이터를
                            #이용할때는 오류남
input= sys.stdin.readline   #이걸 왜 해야되지

N,M=map(int,input().split())

#노드의 숫자가 1부터 시작이므로 N+1 (직관적으로)
visit_list=[0]*(N+1) # 0이면 방문X, 1이면 방문O
A=[[] for _ in range(N+1)]

#양방향이므로, 처음부터 if문으로 방문했는지 안했는지 조건걸고 들어가야함
def DFS(v):
    visit_list[v]=1
    for i in A[v]:
        if(visit_list[i]==0):
            DFS(i)


# 양방향이기때문에, 둘다 넣어줘야함
for _ in range(M):
    s , e = map(int,input().split())
    A[s].append(e)
    A[e].append(s)

count=0

for i in range(1,N+1):
    if( visit_list[i]==0):
        count+=1
        DFS(i)

print(count)
