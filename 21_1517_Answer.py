#8
#3 2 8 1 7 4 5 6


result=0

def merge_sort(s,e):
    global result
    if(e-s<1): #원소 하나
        return

    mid=int(s+((e-s)/2))
    merge_sort(s,mid) #왼쪽 병합
    merge_sort(mid+1,e)#오른쪽 병합
    for i in range(s,e+1):
        tmp[i]=A[i]  #전에 형성 되었던 정렬 전 집합들 가져오기

    i=s
    j=mid+1
    k=s
    while(i <= mid and j<=e):
        if(tmp[i] > tmp[j]):   #index가 앞으로 땡겨지는 행위는 뒤쪽그룹이 앞쪽그룹으로 이동했을때만 생긴다
            A[k]=tmp[j]
            result=result+(j-k)
            k+=1
            j+=1
        else:
            A[k]=tmp[i]
            k+=1
            i+=1
    while(i<=mid):
        A[k]=tmp[i]
        k+=1
        i+=1
    while(j<=e):
        A[k] = tmp[j]
        k += 1
        j += 1
        #2318 -> 1238


N=int(input())
A=list(map(int,input().split()))
tmp=[0]*N
merge_sort(0,N-1)
print(result)





