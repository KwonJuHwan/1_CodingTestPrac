#전형적인 다익스트라 문제
import sys
from queue import PriorityQueue
input=sys.stdin.readline

n= int(input())
m= int(input())
A=[[]for _ in range(n+1)]
visit=[False]*(n+1)
result=[sys.maxsize]*(n+1)
queue=PriorityQueue()

for i in range(m):
    s, e, c= map(int,input().split())
    A[s].append((e,c))

start,end= map(int,input().split())
result[start]=0
queue.put((0,start))

while(queue.qsize()>0):
    now = queue.get()
    if not visit[now[1]]:
        visit[now[1]]=True
        for next in A[now[1]]:
            if(result[next[0]] > result[now[1]]+next[1]):
                result[next[0]] = result[now[1]]+next[1]
                queue.put((result[next[0]],next[0]))

print(result[end])
