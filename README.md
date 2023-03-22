# 1_CodingTestPrac
DoIt


46번. 특정 거리의 도시 찾기
1.최단거리에 대한 문제이므로, DFS로 풀 수 없다(stack 구조이기 때문에) -> BFS로 문제해결
2. BFS에서 필요한 visit값을 depth갚과 합쳐서 공간을 최소화하였다.
3. import에 익숙해지기
import sys
from collections import deque
input=sys.stdin.readline 


47번.
처음에는 최대깊이를 구하는 문제라 DFS접근하였다. 답은 구해지지만 백준에 넣어본 결과, 시간초과가 발생한다.
그래서 최대깊이를 구하는 것이 아닌, 신뢰도 리스트를 만들고, 신뢰도를 부여하는 방식으로 생각하면 BFS로 풀 수 있다.

=> BFS가 DFS보다 시간복잡도가 더 낮으므로, 그래프 문제일때, BFS로 먼저 접근하는 방식을 채택하자.
