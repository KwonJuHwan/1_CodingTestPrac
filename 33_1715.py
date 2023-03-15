#카드 정렬하기
#합친 값을 다시 sort해야함 -> 자료구조를 써야됨을 상기

from queue import PriorityQueue

mq=PriorityQueue()

N=int(input())

for i in range(N):
    mq.put(int(input()))
result = 0

for i in range(N-1):
    temp1=mq.get()
    temp2=mq.get()
    result+=temp1+temp2
    mq.put(temp1+temp2)

print(result)


