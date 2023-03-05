#우선순위큐의 자동정렬 장점
#비교할 조건이 많아도 하나로 묶어서 비교 가능

from queue import PriorityQueue


n=(int)(input())
myQueue= PriorityQueue()

for i in range(n):
    ins= (int)(input())
    if ins == 0:
        if(myQueue.empty()):
            print("0\n")
        else:
            temp=myQueue.get()
            print(str(temp[1])+"\n")
    else:
        myQueue.put((abs(ins), ins))


