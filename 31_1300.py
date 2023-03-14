#이 아이디어는 얻기 힘듬
# 많은 복습 필요

N=int(input())
K=int(input())

# idea : 자신보다 낮은 수를 세면서, 자신보다 낮은 수 = index
# 주어진 배열에 해당값/N(열) 을 하면, 해당값보다 작은 수의 개수를 알 수 있다 -> 해당 행의 배수이기 때문에
start=0
end=K
while(start>end):
    mid=int((start+end)/2)
    cnt = 0
    for i in range(1, N+1):
        cnt+=min(mid/i,N) #중앙값보다 작은 값 몇개인지 세기(mid의 index 측정)
    if(cnt < k): #중앙값으로 찾은 인덱스가 k보다 작다 -> 중앙값을 더 키워야 함
        start=mid+1
    else: #중앙값으로 찾은 인덱스가 k보다 크다 -> 현재 mid는 B[K]에 해당하는 값보다 크다.
        ans=mid
        end=mid-1

#처음에 mid 값이 B[k]보다 낮게 시작 -> 첫번째 if 문에 걸리면서 start값 높아짐 -> mid보다 낮은 값들이 많아짐 ->인덱스가 올라감

print(ans)
