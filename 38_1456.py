#거의 소수 구하기
import math
a,b = map(int,input().split())

x=int(math.sqrt(b))

A=[0]*(x+1)

for i in range(2,x+1):
    A[i]=i

for i in range(2,x+1):
    if(A[i]!=0):
        plus=2
        while(True):
            temp=A[i]*plus
            if(temp>x):
                break
            A[temp]=0
            plus+=1
cnt=0
for i in range(2,x+1):
    if(A[i]!=0):
        plus=2
        while(True):
            temp=math.pow(A[i],plus)
            if(temp>=a and temp<=b):
                cnt+=1
            elif(temp>b):
                break
            plus+=1


print(cnt)


