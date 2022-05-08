# 재귀(combinations 구현) + bfs 사용

import sys
#sys.stdin = open('input.txt')
input = sys.stdin.readline
from copy import deepcopy
from collections import deque

# 1. 시작 바이러스 조합 구하기
def combinations(last_indx, cnt, virus_indxs):
    global min_time
    # 종료
    if cnt == M:
        now_time = spread_possible(virus_indxs)
        if now_time:
            min_time = min(min_time, now_time)
        return
    # 진행
    for i in range(last_indx+1, virus_cnt - (M - (cnt+1))):
        combinations(i, cnt+1, virus_indxs+[i])


# 2. 해당 조합에서 바이러스 퍼뜨리기
delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]
def spread_possible(virus_indxs):
    global possible
    new_lab = deepcopy(lab)
    new_hole_cnt = hole_cnt
    Q = deque([])
    for indx in virus_indxs:
        new_lab[viruses[indx][0]][viruses[indx][1]] = 1
        Q.append((viruses[indx][0], viruses[indx][1]))

    while Q:
        r, c = Q.popleft()
        sec = new_lab[r][c]
        if sec > min_time:
            return
        for d in range(4):
            nr = r + delta[d][0]
            nc = c + delta[d][1]
            if 0 <= nr < N and 0 <= nc < N and (new_lab[nr][nc] == 0 or new_lab[nr][nc] == -2):
                new_lab[nr][nc] = sec+1
                new_hole_cnt -= 1
                Q.append((nr, nc))

    if new_hole_cnt == 0:
        possible = 1
        return sec-1
    else:
        return

# 0. input 받기
# T = int(input())
# for tc in range(1, T+1):
N, M = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(N)]
hole_cnt = 0
viruses = []
for r in range(N):
    for c in range(N):
        if lab[r][c] == 0:
            hole_cnt += 1
        elif lab[r][c] == 1:            # wall
            lab[r][c] = -1
        elif lab[r][c] == 2:            # virus가 있는 위치 모두 표현
            lab[r][c] = -2
            hole_cnt += 1
            viruses.append((r, c))

# 3. 이미 바이러스가 모두 퍼뜨러져 있으면 0 출력하고 아니라면 1,2 함수 사용해서 값 구하기
hole_cnt -= M
if hole_cnt == 0:
    print(0)
else:
    possible = 0
    virus_cnt = len(viruses)
    min_time = 1000
    combinations(-1, 0, [])
    if possible:
        print(min_time)
    else:
        print(-1)

