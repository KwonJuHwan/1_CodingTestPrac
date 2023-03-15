N,K =map(int,input().split())
A=[0]*N

for i in range(N):
    A[i]=int(input())

i=N-1
cnt=0
money=A[i]
# while(K !=0): #K원을 맞추기 위해 계속 for loop 돌기
#     while(K<money): #가장 큰 동전 찾기
#         i-=1
#         money=A[i]
#     cnt+=int(K/money) #동전 개수
#     K=K-(int(K/money)*money) #동전의 값만큼 빼기

for i in range (N-1, -1 , -1): #for문에서 3번째 파라미터는 gap
    if A[i] <= K:
        cnt+=int(K[A[i]])
        K=K%A[i]


print(cnt)

