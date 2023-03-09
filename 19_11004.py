n,k= map(int,input().split())
a=list( map(int,input().split()))
#quick sort와 다른점: k를 기준으로 sort를 하는 부분을 하나로 할 수 있다 .( elif , else 부분)
def quickSort(s, e, k):
    global a
    if (s < e):
        pivot=partition(s,e)
        if(k==pivot):
            return
        elif(k> pivot):
            quickSort(pivot+1,e,k) #정렬된 값 빼기
        else:
            quickSort(s, pivot-1,k)

def swap(n,m):
    global a
    temp=a[n]
    a[n]=a[m]
    a[m]=temp

def partition(s,e):
    global a
    if( s+1 == e):  #사이의 값이 없을때,
        if(a[s]>a[e]):
            swap(s,e)
        return e
    mid = (s+e)//2
    swap(mid,s)
    pivot=a[s] #중간값으로 피벗 & 맨왼쪽으로 피벗 빼놓기
    i=s+1 #피벗제외
    j=e
    while(i<=j):
        while((a[i]< pivot)and i<len(a)-1):
            i+=1
        while((a[j]>pivot)and j>0):
            j-=1
        if(i<=j):
            swap(i,j)
            j=j-1
            i=i+1
    a[s]=a[j]
    a[j]=pivot
    return j

quickSort(0,n-1,k-1)
print(a)

print(a[k-1])

