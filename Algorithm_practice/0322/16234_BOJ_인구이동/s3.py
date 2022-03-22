# python은 시간초과, pypy
from collections import deque
delta = [(-1, 0), (1, 0), (0, 1), (0, -1)]
def country(data):
    answer = 0
    while True:
        info = [[0] * N for _ in range(N)]
        modi = []
        cnts = []
        for r in range(N):
            for c in range(N):
                if info[r][c] == 0:
                    modify = [(r, c)]                           # sr, sc에서 시작했을 때 인구변화가 일어날 위치들
                    cnt = data[r][c]                            # 위치 변화할 나라의 인구수
                    info[r][c] = 1

                    Q = deque([(r, c)])
                    while Q:
                        sr, sc = Q.popleft()
                        for i in range(4):
                            nr = sr + delta[i][0]
                            nc = sc + delta[i][1]
                            if 0 <= nr < N and 0 <= nc < N and info[nr][nc] == 0:
                                if L <= abs(data[nr][nc] - data[sr][sc]) <= R:
                                    info[nr][nc] = 1
                                    Q.append((nr, nc))
                                    cnt += data[nr][nc]
                                    modify.append((nr, nc))

                    if len(modify) > 1:
                        modi.append(modify)
                        cnts.append(cnt)

        if modi:
            for i in range(len(modi)):
                for j, k in modi[i]:
                    data[j][k] = cnts[i] // len(modi[i])
            answer += 1
        else:
            return answer

import sys
# sys.stdin = open('input.txt')
#
# T = int(input())
# for tc in range(1, T + 1):

N, L, R = map(int, sys.stdin.readline().split())
data = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
print(country(data))
