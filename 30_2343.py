#하나는 반드시 존재 해야하므로, 젤 큰 수로 시작 9

N,M = map(int,input().split())
A=list(map(int,input().split()))
start=0
end=0

for i  in A:
    if(start< i):
        start=i
    end=end+i
# 담는 크기의 최소 조건 + 모든 값을 담아야 한다
#mid의 왼쪽탐색 -> 담는 크기가 너무커서 담는 크기의 최소 조건에 맞지 않는다
#mid의 오른쪽탐색 -> 담는 크기가 작아 전부 안담긴다
#리스트 기준이 아닌, 더한 값을 기준으로 이진 탐색
while(start <= end):
    mid= int((start+end)/2)
    count=0 # 블루레이 개수
    sum=0 #블루레이에 담기는 레슨의 크기
    for  i in range(N):
        if( sum+A[i] > mid):
            count=count+1
            sum=0
        sum=sum+A[i]
    if(sum !=0): #마지막까지 다 더하고, 마지막 레슨들이 담길 블루레이를 더해야하므로
        count+=1
    if(count>M): #개수 초과, 블루레이의 크기가 너무 작다
        start=mid+1
    else:
        end=mid-1

print(start)



