n=(int)(input())
myList=list(map(int,input().split()))
ans= [0]*n
myStack=[]
cnt=0
#시간 복잡도를 줄여야된다 -> 이미 계산 끝난 것들을 제외하고 싶다
#stack의 pop기능을 통해, 계산이 끝난 수열들을 제외시킨다.
# i = index
for i in range(n):
    while( myStack and myList[myStack[-1]]< myList[i]):
        index = myStack.pop()
        ans[index]=myList[i]

    myStack.append(i)

while myStack:
    index = myStack.pop()
    ans[index] =-1

print(ans)

result=""

for i in range(n):
    result+=str(ans[i])+" "

print(result)
