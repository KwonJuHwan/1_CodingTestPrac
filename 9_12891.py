#List 중심이 아닌 조건을 중심으로 세팅하고 루프
#초기조건, 마지막 동작을 생각하여 세팅
#처음 checkList가 0일떄의 동작 처리 -> 초기 조건 세팅이 빡셈
#초기 조건과 조건이 맞을때 확인하는 알고리즘을 생각하기가 어려웠음

checkList = [0]*4
myList= [0]*4
four=0

#  A C G T
def myAdd(c):
    global checkList, myList,four

    if(c=='A'):
         myList[0]+=1
         if(checkList[0] == myList[0]):
             four+=1
    elif (c == 'C'):
        myList[1] += 1
        if (checkList[1] == myList[1]):
            four += 1
    elif (c == 'G'):
        myList[2] += 1
        if (checkList[2] == myList[2]):
            four += 1
    elif (c == 'T'):
        myList[3] += 1
        if (checkList[3] == myList[3]):
            four += 1

def myDel(c):
    global checkList, myList, four

    if (c == 'A'):
        if (checkList[0] == myList[0]):
            four -= 1
        myList[0] -= 1
    elif (c == 'C'):
        if (checkList[1] == myList[1]):
            four -= 1
        myList[1] -= 1
    elif (c == 'G'):
        if (checkList[2] == myList[2]):
            four -= 1
        myList[2] -= 1
    elif (c == 'T'):
        if (checkList[3] == myList[3]):
            four -= 1
        myList[3] -= 1

n,m= map(int,input().split())
dna= list(input())
checkList=list(map(int,input().split()))
cnt=0

for x in range(4):
    if(checkList[x]==0):
        four+=1


for x in range(m):
    myAdd(dna[x])

if(four==4):
    cnt+=1

for i in range(m,n):
    myAdd(dna[i])
    myDel(dna[i-m])
    if (four == 4):
        cnt += 1

print(cnt)
