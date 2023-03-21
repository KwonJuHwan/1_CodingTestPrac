# 1_CodingTestPrac
DoIt


46번. 특정 거리의 도시 찾기
1.최단거리에 대한 문제이므로, DFS로 풀 수 없다(stack 구조이기 때문에) -> BFS로 문제해결
2. BFS에서 필요한 visit값을 depth갚과 합쳐서 공간을 최소화하였다.
3. import에 익숙해지기
import sys
from collections import deque
input=sys.stdin.readline 
