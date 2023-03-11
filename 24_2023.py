n=int(input())
#앞서 리스트로 DFS를 구현하려고만 해서 구애받음 -> 넣고 하는 것이 아닌 넣어가면서 판단
# A=[[] for _ in range(4)]
#
# # ex) 4자리수
# for _ in range(n-1):
#     for j in (1,2,3,5,7,9):
#         A[2].append(j)
#         A[3].append(j)
#         A[5].append(j)
#         A[7].append(j)
#
def isPrime(num):
    for i in range(2,int(num/2+1)):
        if num %i ==0:
            return False
    return True

def DFS (num):
    if (len(str(num))==n and isPrime(num)==True):
        print(num)
    else:
        if(isPrime(num)==False):
            return
        else:
            for i in range(1,10):
                if(i%2 !=0):
                    DFS( num*10+i)
#풀이 isPrime을 DFS전에 먼저 확인해서 빠져나갈때
# 이미 소수임을 검증하고 나가기때문에, 소수를 확인할 필요가 없음
def DFS2 (num):
    if((len(str))==n):
        print(num)
    else:
        for i in range(1,10):
            if(i%2==0):
                continue
            if(isPrime(num*10+i)):
                DFS2(num*10+i)

DFS(2)
DFS(3)
DFS(5)
DFS(7)


