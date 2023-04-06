# 1_CodingTestPrac
DoIt

64번: 최소 신장 트리의 기본
최소 신장 트리
조건: 사이클 X , n개의 노드 -> 최소 신장 트리를 구성 하는 에지의 개수는 항상 n-1
엣지 중심 -> 엣지 리스트로 저장 + 유니온 파인드
가중치 정렬 후, 낮은 것 부터 연결 시도 ->
파인드로 확인 후(대표 노드가 같으면 사이클 발생) , 사이클이 아닐 때에만 union 연산
```
#최소 확정(정렬로 인해) ,노드의 사이클이 없는 것도 확정(find 값이 다름) -> 무조건 최소 신장 트리의 노드
#유니온 파인드의 핵심은 find에서 재귀함수로 업데이트 시켜주기 *잊지말자
```

65번: 모든 섬의 좌표를 넣고, 같은 섬을 만나면 뺴는것 = 전체집합-여집합을 하는 아이디어 
어떤 자료구조를 활용하여 데이터를 처리할 것인지에 대한 고민
문제를 어떤방식으로 풀어나가야할까에 대한 고민

66번: 유용한 코드: ord(): ord('a')=97 -> char를 아스키 코드 숫자로 변환해줌
