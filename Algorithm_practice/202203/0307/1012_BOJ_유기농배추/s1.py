import sys
sys.stdin = open('input.txt')

# bfs로 1로 연결된 섬들의 개수 찾기
from collections import deque

delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]
def bfs(arr, N, M):
    Q = deque()
    k = 0
    for r in range(N):
        for c in range(M):
            if arr[r][c] == 1:              # 기준점을 이동하다 1을 발견하면 섬의 개수에 더해준다.
                arr[r][c] = 0
                k += 1
                Q.append([r, c])
                while Q:                    # 더는 연결된 곳이 없을 때까지 돈다.
                    sr, sc = Q.popleft()
                    for d in delta:         # 상하좌우 방향으로 1로 연결된 곳이 있는지 확인하고
                        nr = sr + d[0]
                        nc = sc + d[1]
                        if 0 <= nr < N and 0 <= nc < M and arr[nr][nc] == 1:        # 인덱스도 맞고, 1로 연결되어 있다면
                            arr[nr][nc] = 0                                         # 방문 표시를 해주고 Q에 추가해주어 다음으로 상하좌우를 살필 곳으로 지정해준다.
                            Q.append([nr, nc])

    return k


T = int(input())
for tc in range(T):
    M, N, K = map(int, input().split())
    data = [[0]*M for _ in range(N)]
    for k in range(K):
        i, j = map(int, input().split())
        data[j][i] = 1
    print(bfs(data, N, M))