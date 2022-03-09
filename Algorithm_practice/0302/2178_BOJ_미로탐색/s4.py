# bfs + deque 사용
# dfs -> 시간 초과
from collections import deque
delta = [[1, 0], [0, 1], [-1, 0], [0, -1]]

def bfs(v):
    stack = deque([v])
    while stack:
        r, c = stack.popleft()          # stack 안에서 기준점 뽑기
        if not visited[r][c]:                                                                                   # 출발점인 [0, 0]을 1칸으로 친다.
            visited[r][c] = 1

        for d in delta:                 # 델타 방향 이동
            nr = r + d[0]
            nc = c + d[1]
            if 0 <= nr < N and 0 <= nc < M:                                                                     # 인덱스 안에서
                # if arr[nr][nc] == 1 and (visited[nr][nc] == 0 or visited[nr][nc] > visited[r][c] + 1):        # dfs 에서는 필요하지만 bfs에서는 필요치 않다.
                if arr[nr][nc] == 1 and visited[nr][nc] == 0:               # bfs 에서는 이미 visited가 채워졌다면 가장 최단 거리로 채워져 있음 -> 갱신할 필요가 없다.
                    visited[nr][nc] = visited[r][c] + 1                     # visited에 해당 거리 갱신
                    if nr == N-1 and nc == M-1:                             # 목적지에 도달하면 해당 거리 출력
                        return visited[nr][nc]
                    else:
                        stack.append([nr, nc])                              # nr, nc를 stack에 추가

import sys
sys.stdin = open('input.txt')

for tc in range(4):
    N, M = map(int, input().split())
    arr = [list(map(int, input())) for _ in range(N)]
    visited = [[0]*M for _ in range(N)]
    print(bfs([0, 0]))