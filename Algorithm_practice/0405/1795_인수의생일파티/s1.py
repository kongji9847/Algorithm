# 다익스트라 : X에서 Y로 가는 최단 경로
'''
Y -> X : Y -> C -> X == X -> C -> Y
같은 경로라면 Y에서 시작하던, 그래프의 방향을 바꿔 X에서 시작하던 동일한 최단 거리의 결과가 나온다.
'''
# 인수 집으로 가는 최단 경로는 그래프의 방향을 거꾸로 해서
# 인수 집에서 시작하는 최단 경로를 찾으면 된다.

import sys
sys.stdin = open('input.txt')
import heapq

# 1. X로부터 모든 노드 사이의 최단 거리를 보는 함수
def dijstra(graph, X):
    heap = []
    heapq.heappush(heap, (0, X))
    visited = [0] * (N+1)
    node_cnt = 0
    dist = [0] * (N + 1)

    while heap:
        weight, node = heapq.heappop(heap)
        if not visited[node]:
            visited[node] = 1
            dist[node] = weight
            node_cnt += 1

            if node_cnt == N:
                return dist

            for v in range(len(graph[node])):
                indx = graph[node][v][0]                # 확인해야할 인덱스
                if not visited[indx]:
                    heapq.heappush(heap, (weight + graph[node][v][1], indx))


T = int(input())
for tc in range(1, T+1):
    N, M, X = map(int, input().split())

    # N의 개수가 크므로 행렬 형태는 보지 않아도 될 987654321이란 임의의 큰 수도
    # dijstra 함수 안에서 계속 heap에 담게 하여 시간이 오래 걸린다.
    graph1 = [[]*(N+1) for _ in range(N+1)]
    graph2 = [[]*(N+1) for _ in range(N+1)]

    for _ in range(M):
        x, y, c = map(int, input().split())
        graph1[x].append([y, c])                 # 인덱스, cost
        graph2[y].append([x, c])

    # 인수네 집에서 자신의 집으로 돌아가는 최단경로.
    fromX = dijstra(graph1, X)
    # 인수네 집에 가는 모든 사람들의 최단경로
    toX = dijstra(graph2, X)

    max_num = 0
    for i in range(1, N+1):
        if max_num < toX[i] + fromX[i]:
            max_num = toX[i] + fromX[i]
    print(f'#{tc}', max_num)