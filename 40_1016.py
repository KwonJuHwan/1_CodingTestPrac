import math
s,e= map(int,input().split())
x=int(math.sqrt(e)) #max의 제곱근
answer=[0]*(e+1)
A=[0]*(x+1)

for i in range(2,x+1):
    answer[int(math.pow(i,2))]=int(math.pow(i,2))
cnt=0
for i in range(s,e+1):
    if(answer[i]==0):
        cnt+=1
        if(i==1):
            cnt-=1

print(cnt)



