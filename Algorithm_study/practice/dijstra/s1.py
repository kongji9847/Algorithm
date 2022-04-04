"""
1. 기본 정보
0번 지점에서 V번 지점까지 이동하는데 걸리는 최소 거리 출력
방향 존재

2. 입력 정보 (유향 그래프)
첫 째 줄에 마지막 노드 번호 V(0번 부터 시작)와 간선의 개수 E
다음 줄부터 E개의 줄에 걸쳐 간선의 시작(start)과 끝(end) 그리고 구간의 거리(w) 정보

다익스트라
 - 시작 지점으로부터 특정 지점까지의 최소 거리(비용)을 아는 것이 포인트
  - 어떤 정점을 거쳐왔는지 알 수 없음
 - prim과 비슷한 방식으로 구현
  - 다만, 최소 비용을 갱신 하는 과정에서 차이가 발생
 - 음수 가중치 허용하지 않음
"""
"""
    A -> E        dist[j]
    A -> B -> E   dist[min_idx] + G[min_idx][j]
"""

import sys
sys.stdin = open('input.txt')

# 2. start 노드에서 각 노드까지의 최단거리 리스트 출력 함수
def dijkstra(start):
    values[start] = 0                                                   # 0번 인덱스에서의 최단 경로
    # 노드의 개수 V+1개
    # start 노드와 end 노드까지 존재할 수 있는 최대한의 간선 개수는 V개(start - v1 - v2- ... - end) => V번 반복
    for _ in range(V):

        #  2-1. 현재 방문하지 않은 노드 중 최솟값 찾아서 방문 표시하기
        min_value = 987654321               # 새로운 values 리스트를 돌기전 값 초기화
        min_indx = 0
        for v in range(V+1):
            if not visited[v] and min_value > values[v]:
                min_value = values[v]
                min_indx = v
        visited[min_indx] = 1

        # 2-2. 최근에 방문한 노드와 인접한 노드의 최솟값 갱신 : 원래의 최솟값 vs 최근에 방문한 노드를 거쳐가는 경우 비교
        for end in range(V+1):
            new_dist = values[min_indx] + graph[min_indx][end]
            if not visited[end] and values[end] > new_dist:
                values[end] = new_dist

    return values                                                            # 0번 인덱스로부터 각 지점까지의 최단 거리



# 1. input 받고 graph 만들기
V, E = map(int, input().split())
graph = [[987654321]*(V+1) for _ in range(V+1)]
# graph -> 자기 자신: 0, 인접할 때: weight, 인접하지 않을 때:987654321(임의의 큰 수)
for _ in range(E):
    start, end, weight = map(int, input().split())
    graph[start][end] = weight
for v in range(V+1):
    graph[v][v] = 0

values = [987654321] * (V+1)                        # 각 최단거리 담을 통
visited = [0] * (V+1)                               # 방문 표시
print(dijkstra(0))

