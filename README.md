# 1_CodingTestPrac
DoIt

61번:
#전체 경로의 최단 경로는 부분 경로의 최단 경로의 조합으로 이뤄진다.
//
모든 노드 간의 최단 거리를 알려주는 것이 특징(문제 조간)
//
#삼중 for 문 k - s - e
#경유지인 k를 기준으로 계산하기 위해서
#D[s][e] = Math.min(D[s][e],D[s][k]+D[k][e])

62번: 같은 알고리즘으로 계산식만 조금 다름
