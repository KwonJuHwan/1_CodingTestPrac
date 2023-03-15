#최솟값을 만드는 괄호 배치 찾기
#정답을 내는건 쉽지만 기호처리하는 것이 쉽지 않음
A=list(map(str,input().split("-")))


for i in range(len(A)):
    if(A[i].find("+")!= -1):
        B=list(map(int,A[i].split("+")))
        A[i]=0
        for j in range(len(B)):
            A[i]+=B[j]
    else:
        A[i]=int(A[i])

sum=A[0]

for i in range(1,len(A)):
    sum-=A[i]

print(sum)

#답지 풀이 (여기서 배울 점은 list와 for문을 자유롭게 사용하는 점
# def MySum(i):
#     sum=0
#     temp=str(i).split("+")   *
#     for i in temp:           *
#         sum+=int(i)          *
#     return sum
#
# result=0
# for i in range(len(A)):
#     temp=mySum(A[i])
#     if(i==0):
#         result+=temp
#     else:
#         result-=temp
#
# print(result)

