# 1_CodingTestPrac
DoIt

56번: 우선순위 큐 사용
#다익스트라 제약조건: 항상 양수
#다익스트라: 최단거리를 구하는 알고리즘
#출발노드와 다른 모든 노드들 간의 최단거리
#우선순위 큐를 사용해서 시간초과 면하기 -> 최소거리 먼저 탐색 + 최소거리 아니면 queue 넣지 않음

57번: 56번과 동일한 문제

58번: 아이디어는 알았으나, sort를 for문에 넣으면 안된다는 강박이 있어, 밖에서 풀어볼려다가 못풀었음. 
+idea 앞에서부터 채우는 것이 아니라 인덱스 k 값보다 큰 값들은 다 버리기 (뒤부터 채우기) k보다 큰 인덱스를 가진 값들은 필요 없으므로 크기를 정해놓고, k보다 큰 값들은 drop하는 형태
+우선순위 큐보다 힙이 더욱 시간복잡도가 작으므로 힙을 사용해버릇하자.
