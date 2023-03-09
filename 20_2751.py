
def merge_sort(s,e):
    global tmp,A
    if(e-s< 1):
        return     #원소의 개수가 하나인 집합일 때는 그냥 리턴 -> 정렬이 필요 없으므로
    m=int(s+(e-s)/2)  #중앙 값
    merge_sort(s,m)
    merge_sort(m+1,e)
    for i in range(s, e+1): #tmp에 A 복사본 저장하고, A 정렬 시켜주기 e+1까지 해야 e도 넣음
        tmp[i]=A[i]
    k=s
    index1=s
    index2=m+1
    while(index1 <= m and index2 <=e): #두 집합 중, 한쪽이 모두 정리 되면 종료
        if(tmp[index1] < tmp[index2]):
            A[k]=tmp[index1]
            k+=1
            index1+=1
        else:
            A[k]=tmp[index2]
            k+=1
            index2+=1
    while(index1 <=m): #왼쪽 집합이 정리 안되었을 때
        A[k]=tmp[index1]
        k+=1
        index1+=1
    while(index2 <=e): #오른쪽 집합이 정리 안되었을 때
        A[k] = tmp[index2]
        k += 1
        index2 += 1

N=int(input())
A=[0]*N
tmp=[0]*N
for i in range(N):
    A[i]=int(input())
print(A)
merge_sort(0,N-1)

print(A)



