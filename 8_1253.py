#정수라는 조건에 의한, 예외 고려

n=(int)(input())
numList=list(map(int,input().split()))
numList.sort()
k=2
cnt=0

for k in range(n):
    tmp = numList[k]
    i = 0
    j = n-1
    while(i < j):
        if ( numList[i]+ numList[j] == tmp):
            if(i != k and j!=k):
                cnt+=1
                break
            elif(i==k):
                i+=1
            elif(j==k):
                j-=1
        elif(numList[i]+ numList[j] > tmp):
            j-=1
        else:
            i+=1
print(cnt)

