# 1_CodingTestPrac
DoIt

위상정렬

53: 
공간 최적화: 처음부터 0인거와, 위상정렬로 인해, 0이된 것을 분리해서 visit을 없앰
아이디어 : 정렬의 순서는 관계가 없으므로, queue를 굳이 동적으로 append 할 필요 없음

54: 그래프탐색에 있어 내가 반드시 봐야할 메커니즘 노드 경로를 선택할때, 하나를 선택하게 함으로써, 노드 weight의 덧셈 중복 방지
#둘 중에 하나를 선택함으로써, 노드 weight의 중복 덧셈 방지 (길이 여러가지 이므로)
        # answer[4]= 1->4 // answer[3]+weight[3] = 1->3->4 둘중에 높은 값으로 선택
        answer[i] = max(answer[i],answer[now]+weight[now])
