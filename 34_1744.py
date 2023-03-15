#수를 묶어서 최댓값 만들기
#두 수의 곱셈을 통해, 수열의 합을 최대한으로 끌어내야됨

from queue import PriorityQueue

mpq=PriorityQueue() # 음의 정수를 담는 우선순위 큐
ppq=PriorityQueue() # 양의 정수를 담는 우선순위 큐

N=int(input())
sum=0
for i in range(N): #핵심 : 예외사항을 input에서 걸러내기
    inp=int(input())
    if(inp==1):
        sum+=1
    elif(inp<=0):
        mpq.put(inp)
    elif(inp >0):
        ppq.put((-inp,inp))

while(not mpq.empty()):
    if(mpq.qsize()==1):
        sum+=mpq.get()
        break
    temp1=mpq.get()
    temp2=mpq.get()
    sum+=(temp2*temp1)

while(not ppq.empty()):
    if(ppq.qsize()==1):
        sum+=ppq.get()[1]
        break
    temp1=ppq.get()[1]
    temp2=ppq.get()[1]
    sum+=(temp1*temp2)

print(sum)


