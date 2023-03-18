


def gcd(s,e):
    if(e==0):
        return s
    else:
        return gcd(e, s%e)

s,e=map(int,input().split())
result=gcd(s,e)

while( result > 0):
    print(1,end='')
    result-=1