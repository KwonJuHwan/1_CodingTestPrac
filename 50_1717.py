#집합 표현하기
# 0: union , 1:find 구현
import sys
input=sys.stdin.readline

n,m=map(int,input().split())
parent=[0]*(n+1) #parent

#value와 index 초기화
for i in range(n+1):
    parent[i]=i

# find 연산
def find(a): #업데이트를 유니온에서 하는 것이 아닌 find에서 업데이트
    global parent
    if parent[a]==a:
        return a
    else:
        parent[a]=find(parent[a])  #핵심 부분 재귀형태로 진행하여, 대표노드 업데이트가 안된부분을 업데이트
        return parent[a]

#유니온 연산
def union(a,b):
    global parent
    a= find(a)
    b= find(b)
    if a !=b:
        parent[b]=a



#입력받기
for i in range(m):
    x,a,b= map(int,input().split())
    if(x==0):
        union(a,b)
        print(parent)
    elif(x==1):
        if find(a)==find(b):
            print("YES")
        else:
            print("NO")




