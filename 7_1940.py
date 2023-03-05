#앞 뒤에서 시작하는 포인터
#값이 비교값과 크거나, 작거나, 같을때의 케이스를 나누어서 생각하자

n=(int)(input())
m=(int)(input())
myList=list(map(int,input().split()))
myList.sort()
cnt=0
start=0
end=n-1
sum=myList[start]+myList[end]
while start<end :
    if(sum < m):
        start+=1
        sum=myList[start]+myList[end]
    elif(sum > m):
        end-=1
        sum=myList[start]+myList[end]
    else:
        cnt+=1
        start+=1
        end-=1
        sum=myList[start]+myList[end]
print(cnt)







