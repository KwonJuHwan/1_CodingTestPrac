#여행 계획 짜기

n=int(input())
m=int(input())
A=[[0 for _ in range(n)]for _ in range(n)]
parent=[0]*(n)

for i in range(n):
    A[i]=list(map(int,input().split()))
    parent[i]=i


#경로를 분석하는 것이 아닌, 연결이 되어있는지만 확인하기때문에, union으로 충분히 풀 수 있는 문제

def find(a):
    if parent[a]==a:
        return a
    else:
        parent[a]=find(parent[a])
        return parent[a]

def union(a,b):
    a= find(a)
    b= find(b)
    if( a != b):
        parent[b]=a

for i in range(n):
    for j in range(n):
        if A[i][j] == 1:
            union(i,j)

answer=list(map(int,input().split()))
for i in range(len(answer)):
    answer[i]-=1

result=True
for i in range(len(answer)-1):
    if find(answer[i]) != find(answer[i+1]):
        result=False

if(result):
    print("YES")
else:
    print("NO")