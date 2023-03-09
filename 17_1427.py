n=list(input())


for i in range(len(n)):
    max=i
    for j in range(i+1,len(n)):
        if(n[max]< n[j]):
            max=j
    if(n[i]< n[max]): # swap이 일어났다면
        temp=n[i]
        n[i]=n[max]
        n[max]=temp


for i in range (len(n)):
    print(n[i])
