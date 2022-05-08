# itertools 사용 + Q 자료구조 사용해서 해당되는 칸만 확인하기(bfs) -> 성공

import sys
# sys.stdin = open('input.txt')

input = sys.stdin.readline
from itertools import combinations
from copy import deepcopy
from collections import deque

delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# T = int(input())
# for tc in range(1, T+1):

N, M = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(N)]
viruses = []
hole_cnt = 0
for r in range(N):
    for c in range(N):
        if data[r][c] == 1:
            data[r][c] = -1
        elif data[r][c] == 2:
            data[r][c] = '*'
            viruses.append((r, c))
        elif data[r][c] == 0:
            hole_cnt += 1
if hole_cnt == 0:
    print(0)
else:
    possible = 0
    min_time = 10000
    combinations_list = list(combinations(viruses, M))
    for element_list in combinations_list:
        new_data = deepcopy(data)
        Q = deque([])
        for er, ec in element_list:
            Q.append((er, ec))
            new_data[er][ec] = '0'
        sec = 1
        new_hole_cnt = hole_cnt
        while Q:
            r, c = Q.popleft()
            sec = int(new_data[r][c])
            if sec >= min_time:
                break
            for d in range(4):
                nr = r + delta[d][0]
                nc = c + delta[d][1]
                if 0 <= nr < N and 0 <= nc < N:
                    if new_data[nr][nc] == 0:
                        new_data[nr][nc] = f'{sec + 1}'
                        Q.append((nr, nc))
                        new_hole_cnt -= 1
                    elif new_data[nr][nc] == '*' and new_hole_cnt:
                        new_data[nr][nc] = f'{sec + 1}'
                        Q.append((nr, nc))

        if new_hole_cnt == 0:
            possible = 1
            min_time = min(sec, min_time)


    if possible:
        print(min_time)
    else:
        print(-1)