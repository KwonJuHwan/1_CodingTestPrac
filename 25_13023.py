#재귀의 깊이가 5이상이면 1 ,아니면 0
import sys
input=sys.stdin.readline
sys.setrecursionlimit(10000)

N,E=map(int,input().split())
A=[[] for _ in range(N)]
visit=[0]*(N)
result=False

for i in range(E):
    s,e= map(int,input().split())
    A[s].append(e)
    A[e].append(s)

#depth를 초기화 하지 않아도 되는구나~
def DFS(v,depth):
    global result
    if(depth==5): #depth가 5
        result=True
        return
    visit[v]=1
    for i in A[v]:
        if(visit[i]==0):
            DFS(i,depth+1)
    visit[v]=0 #Search목적이 아니라 Depth를 알아내는 것이 목적이므로
            #방문한것도 Depth에 영향을 미치므로, DFS가 한번 끝났을때, visit 초기화 필요

for i in range(N):
    DFS(i,1)
    if(result):
        break

if(result):
    print(1)
else:
    print(0)

# #내가 만든 것은 depth를 측정하는 것이 아닌 연결정도만 파악하는 것
# def DFS(v):
#     global cnt
#     visit[v]=1
#     cnt+=1
#     for i in A[v]:
#         if(visit[i] ==0): #방문하지 않았으면 실행
#             DFS(i)
#     return cnt
#
# for i in range(N):
#      if(visit[i] ==0):
#          k=DFS(i)
#          print(k)
#          if(k>=5):
#              result=True
#          cnt=0
