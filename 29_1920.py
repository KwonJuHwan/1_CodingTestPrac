#원하는 정수 찾기

N=int(input())
A=list(map(int,input().split()))
M=int(input())
target=list(map(int,input().split()))
A.sort()

for i in range(M):
    x=target[i]
    find=False
    start=0
    end=N-1
    while start <=end:  #같은 경우도 있음
        midi= int((start+end)/2)
        midv= A[midi]
        if( midv > x): #중간값 제외
            end=midi-1
        elif( midv < x):
            start=midi+1
        else:         #찾음
            find=True
            break
    if(find):
        print(1)
    else:
        print(0)

