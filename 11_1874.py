n=(int)(input())
A=[0]*n
for i in range(n):
    A[i]=(int)(input())

stack=[]
num=1
result= True
answer=""

for i in range(n):
    a=A[i]
    if(a >= num): #원하는거 pop하기위해 계속 넣기
        while(a >= num):
            stack.append(num)
            answer+="+\n"
            num += 1
        stack.pop()
        answer+="-\n"
    else:
        pop = stack.pop()
        answer+="-\n"
        if(pop > a): #나와야되는게 아래에 있으므로
            print("NO.")
            result=False
            break

if (result):
    print(answer)

