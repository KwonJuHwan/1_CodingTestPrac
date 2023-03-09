#bubble 정렬 시, Swap의 개수 출력
#왼쪽으로 이동한놈 + 오른쪽으로 이동했는데, 왼쪽에 자기보다 큰 수 있는 놈
#시간초과 worstCase가 N^2 이므로
N=int(input())
A=list(map(int,input().split()))
# (3,0) (2,1) (8,2) (1,3) (7,4) (4,5) (5,6) (6,7)
# 1 2 3 4 5 6 7 8
K=[[0 for j in range(2)] for i in range(N)]
for i in range (N):
    K[i][0]=A[i]
    K[i][1]=i

cnt=0
for i in range (N):
    if(K[i][0] <K[i][1]+1):
        cnt=cnt+(K[i][1]+1-K[i][0])
    elif(K[i][0] > K[i][1]+1):
        if(i!=0):
            for j in range (i-1):
                if(K[i][0]<K[j][0]):
                    cnt=cnt+(K[i][1]-K[j][1])

print(cnt)

# 병합정렬과 swap간의 이해를 해야함


