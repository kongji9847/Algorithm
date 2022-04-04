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

heap 활용하면 최솟값을 찾는 과정 생략 가능
 - min_heap을 구하면 root는 항상 최소 가중치 위치
 - heap_pop을 할 때마다 root에 있는 최소 가중치 반환
"""
import heapq
def dijstra(start):
    heap = []
    heapq.heappush(heap, (0, start))            # (0: 가중치, 0: 노드 번호)

    while heap:
        w, node = heapq.heappop(heap)
        if not visited[node]:
            visited[node] = 1
            dist[node] = w
            for v in range(V+1):
                if not visited[v]:
                    heapq.heappush(heap, (w + graph[node][v], v))

    return dist



import sys
sys.stdin = open('input.txt')

V, E = map(int, input().split())
graph = [[987654321]*(V+1) for _ in range(V+1)]
for _ in range(E):
    v1, v2, weight = map(int, input().split())
    graph[v1][v2] = weight
for v in range(V+1):
    graph[v][v] = 0

visited = [0]*(V+1)                 # 방문표시
dist = [0] * (V+1)                  # 가중치 갱신
print(dijstra(0))