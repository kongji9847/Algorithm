#bfs
from collections import deque
delta = [[-1, -2], [-2, -1], [-2, 1], [-1, 2], [1, -2], [2, -1], [2, 1], [1, 2]]
def knight(sr, sc):
    arr[gr][gc] = -1                                                # 도착지점
    arr[sr][sc] = 0                                                 # 출발지점 -> 도착지점과 출발지점 같을 수 있으므로 덮어쓰기
    Q = deque([[sr, sc]])

    while Q:
        r, c = Q.popleft()
        for d in delta:
            nr = r + d[0]
            nc = c + d[1]
            if 0 <= nr < N and 0 <= nc < N:
                if arr[nr][nc] == -1:
                    return arr[r][c] + 1
                elif arr[nr][nc] == 0:
                    arr[nr][nc] = arr[r][c] + 1
                    Q.append([nr, nc])
    return 0                                                        # 모든 노드를 돌아도 도착지에 도달을 하지 못하면 0을 반환



import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(T):
    N = int(input())
    arr = [[0] * N for _ in range(N)]
    R, C = map(int, input().split())
    gr, gc = map(int, input().split())
    print(knight(R, C))