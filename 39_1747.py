# 소수 & 팰린드롬 수 중에서 최솟값 찾기

n=int(input())
b=1000001
A=[0]*b

for i in range(2,b):
    A[i]=i

for i in range(2,b): #에라토스테네스 체
    if(A[i]!=0):
        plus=2
        while(True):
            temp=A[i]*plus
            if(temp>b-1):
                break
            A[temp]=0
            plus+=1

def peln(n): #거울수 찾기 리스트로 찾는 아이디어
    k=list(str(n))
    i=1
    result=True
    s=0
    e=len(k)-1
    while(s<e):
        if( k[s] != k[e]):
            return False
        s+=1
        e-=1
    return True


    # while(i<1000000): #자릿수 찾기
    #     temp=int(n/i)
    #     if(temp<10):
    #         break
    #     i=i*10
    #     cnt+=1
    # for j in range(int(cnt/2)):
    #     if(k[j] != k[cnt-j-1]):
    #         result=False
    # return result

for i in range(n,b):
    if(A[i]!=0):
        if(peln(A[i])):
            print(A[i])
            break
