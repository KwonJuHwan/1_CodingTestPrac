# list 초기화, temp라는 매개변수 사용

num, question=map(int,input().split())
num_list=list(map(int, input().split()))
sum_list=[0]
# sum_list[0]= 0
temp=0
for i in num_list:
    temp=temp+i
    sum_list.append(temp)

for i in range(question):
    start, end=map(int,input().split())

    result=sum_list[end]-sum_list[start-1]
    print(result)
