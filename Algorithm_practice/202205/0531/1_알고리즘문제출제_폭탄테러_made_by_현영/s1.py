# 문제 잘못 읽음요.

import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
from collections import deque


# 1. 함수 정의
delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def solution(r, c):
    visited = [[0]*N for _ in range(M)]
    visited[r][c] = 1
    cnt = 1
    Q = deque([[r, c, K-2]])
    while Q:
        sr, sc, bomb = Q.popleft()
        if bomb <= 0:
            continue

        for d in range(4):
            rr, cc = sr + delta[d][0], sc + delta[d][1]
            if 0 <= rr < M and 0 <= cc < N and not visited[rr][cc]:
                if bomb >= towers[rr][cc]:
                    visited[rr][cc] = 1
                    cnt += 1
                    Q.append([rr, cc, bomb-2])
                else:
                    visited[rr][cc] = 1
                    Q.append([rr, cc, bomb//2])
    return cnt



# 0. input 받기
T = int(input())
for tc in range(1, T+1):
    M, N, K = map(int, input().split())
    towers = [list(map(int, input().split())) for _ in range(M)]
    max_tower = 0

    for r in range(M):
        for c in range(N):
            max_tower = max(max_tower, solution(r, c))

    print(f'#{tc}', max_tower)

