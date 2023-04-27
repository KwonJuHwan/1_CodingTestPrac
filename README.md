# 1_CodingTestPrac
DoIt

[![Solved.ac Profile](http://mazassumnida.wtf/api/generate_badge?boj=kjh307ok)](https://solved.ac/kjh307ok)<br/>

Dynamic Programming:
- 큰 문제를 작은 문제로 나누기 ->다이나믹 프로그래밍으로 풀 수 있는지에 대한 여부 확인
- 작은 문제들을 반복되어 나타나고, 이의 결과값이 항상 같아야 함. -> 전체 문제와 부분 문제 간의 인과 관계를 파악하는 훈련이 필요 (이게 잘 안됨)
- memorization : 작은 문제들은 한번만 계산하고, 이를 테이블로 저장-> 꺼내 사용(계산 줄이기) 
- Top-down : 주로 재귀함수로 구현, 코드의 가독성이 좋고, 이해하기 편함
- Bottom-up : 가장 작은 부분 문제부터 문제를 해결하면서 큰 문제로 확장 - 반복문의 형태로 구현 
-> 둘의 큰 차이보다 자신이 편한 방법을 택해서 사용하는 것이 정답

문제 풀이
- 84: 먼저 무조건 계산한 다음 min 을 통해 비교 , 어차피 min 함수로 비교 하기 때문에, 순서 상관 X
- 85:  일반식 + 예외로 문제풀이 
```
직접 수를 넣어보고 판단 -> 규칙을 찾아내고 일반식을 도출 + 예외 잡아내기
DP table을 사용하기 때문에, index에 신경을 쓰자. 
```
