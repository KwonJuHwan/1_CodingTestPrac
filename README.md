# 1_CodingTestPrac
DoIt


```
D[i][j]= D[i-1][j] + D[i-1][j-1]
현재 문제를 부분 문제로 나누어서 생각 -> 점화식과 같이 문제 접근
초기화를 어떻게 할 것인가, for 문의 처음과 시작을 무슨 값으로 할 것인가
어떤 값으로 나누어라 -> 모듈러 계산 (MOD)
```
<div>
76번:
 #조합 
 #모든 부분 문제가 해결 했다고 가정
 #이항 계수 구하기 1
 </div>
<div>
77번 : 76번과 같음
 </div>
 <div>
 <div>78번: 
D[a][b] = D[a-1][1] + ... +D[a-1][b-1] +  D[a-1][b]</div>
<div>여기서 D[a-1][1] + ... +D[a-1][b-1] 이 부분을 D[a][b-1]로 치환 가능 (부분 문제들의 합)</div>
<div>이렇게 부분 문제의 합으로 문제를 분석 해보는 능력을 길러야 한다.</div>
 </div>
<div>
81번: 팩토리얼 공부 다시 하기
</div>
-82번: k에 대한 이해가 필요 다시보기
