n=int(input())
a= list(map(int,input().split()))
a.sort()
i=len(a)
j=0
sum=0
#1 내가 쓴 코드
while (i>0):
    sum+=(a[j]*i)
    i-=1
    j+=1

print(sum)

#교제 풀이 -> 합배열 공부가 됨
sum=0
s=[0]*(n)
s[0]=a[0]
for i in range (1,n):
    s[i]=s[i-1]+a[i]

for i in range(n):
    sum+=s[i]

print(sum)
