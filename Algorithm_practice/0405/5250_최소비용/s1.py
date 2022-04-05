# bfs + 다익스트라 → 최소값이 갱신된 것만 Q에 넣어주기
# dist의 각 좌표는 0,0에서 해당 좌표까지 가는 최소 비용 거리

import sys
sys.stdin = open('input.txt')
from collections import deque

delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]
def solution():
    Q = deque([(0, 0)])
    dist[0][0] = 0
    while Q:
        (sr, sc) = Q.popleft()
        for d in range(4):
            nr = sr + delta[d][0]
            nc = sc + delta[d][1]

            if 0 <= nr < N and 0 <= nc < N:
                if data[sr][sc] >= data[nr][nc] and dist[sr][sc] + 1 < dist[nr][nc]:
                    dist[nr][nc] = dist[sr][sc]+1
                    Q.append((nr, nc))

                elif data[sr][sc] < data[nr][nc] and (dist[sr][sc] + 1 + data[nr][nc] - data[sr][sc]) < dist[nr][nc]:
                    dist[nr][nc] = dist[sr][sc] + 1 + data[nr][nc] - data[sr][sc]
                    Q.append((nr, nc))

    return dist[N-1][N-1]


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    dist = [[9876543210] * N for _ in range(N)]
    print(f'#{tc}', solution())