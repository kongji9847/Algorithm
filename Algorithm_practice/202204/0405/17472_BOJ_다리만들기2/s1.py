'''
이중 for문에서 맘대로 상위 for에 속해 있는 변수(여기서는 r) 바꿔서 사용하지 말자
예를 들면
for r in range(2):
    for c in range(4):
        if c == 1:
            r += 2
        print([r, c], end=' ')

# [0, 0] [2, 1] [2, 2] [2, 3] [1, 0] [3, 1] [3, 2] [3, 3]
# r이 0인 turn에서 r += 2 상태로 쭉 진행된다.
'''

# import sys
# sys.stdin = open('input.txt')

from collections import deque
import heapq

# 1. 섬을 구분하고 라벨링 해주기 - bfs 활용
delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]
def island(data):
    indx = 1
    for r in range(N):
        for c in range(M):
            if data[r][c] == 1:                     # 섬 탐색의 시작지점 -> 시작지점과 연결되어 있으면 indx인 이름의 섬
                indx += 1                           # 탐색 지점을 찾을 때마다 indx를 늘려준다. -> 첫번째 섬은 라벨 2
                Q = deque([(r, c)])
                data[r][c] = indx
                while Q:
                    sr, sc = Q.popleft()             # 여기서 r, c = Q.popleft() 로 해줘서 오류가 났다. => r이 0인 턴에서 r이 바뀌어서 c를 돈다.
                    for d in range(4):
                        nr = sr + delta[d][0]
                        nc = sc + delta[d][1]
                        if 0 <= nr < N and 0 <= nc < M and data[nr][nc] == 1:
                            data[nr][nc] = indx         # 시작지점과 연결되어 있으므로 라벨링한다.
                            Q.append((nr, nc))
    # 마지막 섬의 indx 출력
    return indx

# 2. r과 c 섬 사이에 다리를 놓을 수 있는 최소 길이
def solution(data, N, M):
    for r in range(N):                                      # r번째 행에서 다리를 만들 수 있는지 확인한다.
        start = -1
        for c in range(M):
            if data[r][c] != 0 and start == -1:             # 섬이 처음으로 발견되면 다리의 시작지점이다.
                start = data[r][c]
                start_indx = c                              # start_indx: 다리를 놓을 부분

            elif start != -1 and data[r][c] == start:       # 섬이 진행되고 있으면 다리를 놓을 부분 갱신
                start_indx = c

            elif data[r][c] != 0 and start != -1 and data[r][c] != start:                   # 다른 섬이 나타나면
                end = data[r][c]                                                            # 다른 섬의 라벨을 확인하고
                if c - start_indx - 1 > 1 and graph[start][end] > c - start_indx - 1:       # graph에 start 섬과 end 섬 사이의 다리의 길이를 갱신한다. -> 기존보다 작은 경우에만
                    graph[start][end] = c - start_indx - 1
                    graph[end][start] = c - start_indx - 1

                start = data[r][c]                           # end 섬은 그 뒤의 섬의 또다른 시작지점이 된다.
                start_indx = c

# 3. prim 알고리즘을 사용해서 MST 형성 여부 및 MST 길이 구하기
def prim():
    ans = 0
    node_cnt = 0
    visited = [0]*(island_cnt+1)                            # 노드 방문 여부 확인
    heap = []
    heapq.heappush(heap, (0, 2))                            # 섬의 시작 인덱스는 2이므로

    while heap:                                             # heap에서 가장 작은 weight의 노드를 뽑아서 ans 갱신
        weight, node = heapq.heappop(heap)

        # 3-1. 종료조건1 -> weight가 초기 입력한 임의의 큰 수로 나오면
        # -> MST는 형성 불가능하다는 말 = 현재 최소 값이 9876543210이라는 뜻이고 더이상 다리를 연결할 수 없다는 말
        if weight == 9876543210:
            return -1

        # 뽑은 node가 아직 방문한 곳이 아니라면 visited에 추가
        if not visited[node]:
            ans += weight
            visited[node] = 1
            node_cnt += 1

            # 3-2. 종료조건2 모든 노드가 visited에 채워지면 ans 반환
            if node_cnt == island_cnt - 1:
                return ans

            # 최근에 뽑은 노드와 인접한 노드들을 heap에 넣어주기 -> 넣어주면 자동적으로 최소 힙 구조
            for v in range(2, island_cnt+1):
                if not visited[v]:
                    heapq.heappush(heap, (graph[node][v], v))



# T = int(input())
# for tc in range(1, T+1):
# 0. 사전 준비
N, M = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(N)]              # 행기준
island_cnt = island(data)                                               # 섬을 라벨링하고 섬의 개수를 반환(섬의 실제 개수 = island_cnt - 1)
col_data = list(zip(*data))                                             # 열기준

# 섬과 섬사이의 최단 다리 길이를 graph에 입력한다.
graph = [[9876543210]*(island_cnt+1) for _ in range(island_cnt+1)]
solution(data, N, M)
solution(col_data, M, N)

print(prim())
