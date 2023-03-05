#슬라이딩 윈도우 이는 구조를 이용하는 것이니까 일단 넘어가자


n, l = map(int,input().split())
ins= list(map(int,input().split()))
result = [0]*(n)
#초기값 세팅
min= ins[0]
result[0]=min

#초기값 빼는게 없음
for i in range(1,l):
    if(ins[i]<min):
        min=ins[i]
    result[i]=min


for i in range(l,n):
    #min이 없어졌을시, 예외 처리
    if(ins[i-l]==min):
        min=ins[i-l+1]
        if(i-l+2 <= l-1):
            for j in range(i-l+2,l-1):
                if(ins[j]<min):
                    min=ins[j]
    if(ins[i]<min):
        min=ins[i]

    result[i]=min

print(result)

