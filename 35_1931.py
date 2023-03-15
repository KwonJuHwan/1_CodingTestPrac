#회의실 배정하기
#
# 11
# 1 4
# 3 5
# 0 6
# 5 7
# 3 8
# 5 9
# 6 10
# 8 11
# 8 12
# 2 13
# 12 14

#회의시간이 가장 짧은것으로 그리디를 하였더니 실패 / 그리디의 기준을 잘 못 생각함
#회의 끝나는시간이 가장 짧은 것을 우선으로 greedy

N=int(input())
A=[[0]*2 for _ in range(N)]

for i in range(N):
    s,e= map(int,input().split())
    A[i][0]=e
    A[i][1]=s

A.sort() #끝나는시간 기준으로 정렬
cnt=0
start=-1
for i in range(N):
    if(A[i][1]>=start): #시작시간이 마지막으로 끝난시간보다 크거나 같을때,
        cnt+=1
        start=A[i][0]  #회의를 시작할 수 있는 시간 업데이트

print(cnt)


# from queue import PriorityQueue
#
# N=int(input())
# min, max = map(int,input().split())
# pq=PriorityQueue()
#
# for _ in range(1,N):
#     s,e= map(int,input().split())
#     if(min> s):
#         min=s
#     if(max<e):
#         max=e
#     pq.put((e-s,s,e))
#
# A=[True for _ in range(min,max)]
# cnt=0
#
#
#
# while(not pq.empty()):
#     temp=pq.get()
#     start=temp[1]
#     end=temp[2]
#     to=True
#     for i in range(start,end):
#         if(not A[i]): #빈시간이 아님
#             to=False
#             break
#         A[i]=False
#     if(to):
#         cnt+=1
#
# print(cnt)






