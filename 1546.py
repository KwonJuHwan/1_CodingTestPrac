# list형태로 input 받기, max, sum 이용

x=(int)(input())
num_list=list(map(int,input().split()))
# mymax=(sorted(num_list))[len(num_list)-1]
mymax=max(num_list)
sum=sum(num_list)
result=(((sum*100)/mymax)/x)

print(result)