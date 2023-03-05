from collections import deque
n=(int)(input())
myQueue= deque()
for i in range(1,n+1):
    myQueue.append(i)
# 1 2 3 4

for i in range(n-1): #while len(myQueue) >1: 이걸로 대체가능 이게 더 직관적임
    myQueue.popleft()
    popleft = myQueue.popleft()
    myQueue.append(popleft)




print(myQueue.pop())

