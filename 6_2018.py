#for문 두개를 포인터 두개를 사용함으로써 시간 복잡도 줄이기
#index를 먼저 더할지 sum을 먼저 계산할지 알고리즘 잘 생각하기

# n=(int)(input())
# max= (int)(n/2) + 2
# sum=0
# result=1
# for x in range(1, max):
#     for y in range(x, max):
#         sum+=y
#         if(sum==n):
#             result=result+1
#     sum=0
#
# print(result)

n=(int)(input())
start=1
end=1
sum=1
cnt=1

while end != ((int)(n/2)+2) :
    if(sum==n):
        cnt+=1
        end += 1
        sum+=end
    elif(sum>n):
        sum -= start
        start += 1
    else:
        end += 1
        sum += end
print(cnt)









