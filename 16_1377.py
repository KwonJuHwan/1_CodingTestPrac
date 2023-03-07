#몇번 루프안에 버블 정렬이 끝났는지
# 10 1 5 2 3
#다음과 같은 아이디어를 도출하는것이 포인트
# 1 2 3 5 10 오른쪽으로 이동 -> 수열안에서 얼마든지 가능 왼쪽은 무조건 for문에서 한번씩 전체 swap를 다 하므로
#왼쪽으로 이동한 최댓값만 구하면 된다 -> 얘가 swap을 안하고 for문을 돌 수는 없다 -> 전체 수 전체를 swap을 걸기때문에

n=int(input())
a=[]

for i in range (n):
    a.append((int(input()),i))

sorted_a=sorted(a)

max=0
for i in range(n):
    if(sorted_a[i][1]-i > max):
        max=sorted_a[i][1]-i

print(max+1)


