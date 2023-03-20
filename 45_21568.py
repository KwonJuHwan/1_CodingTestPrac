#방정식의 해를 구하기
#미리 필요한 값 세팅 후, 문제풀기(q_list, cnt)
q_list=[0]*100
cnt=0
def gcd(a,b):
    global cnt,q_list
    if(b==0):
        return a
    else:
        q_list[cnt]=int(a//b)
        cnt+=1
        return gcd(b,a%b)
#x,y
def exgcd(a,b):
    global cnt,q_list
    x=b
    y=a-(b*q_list[cnt])
    cnt-=1
    if(cnt == -1):
        return x,y
    else:
        return exgcd(x,y)

a,b,c=map(int,input().split())
mygcd=gcd(a,b) #몫리스트 업데이트
if(c%mygcd !=0):
    print(-1)
else:
    a,b=exgcd(0,1)
    k= c/mygcd
    a= int(a*k)
    b= int(b*k)
    print(a,b)


