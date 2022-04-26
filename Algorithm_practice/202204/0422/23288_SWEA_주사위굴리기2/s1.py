# 재귀 버전 -> maximum recursion을 넘는다.
import sys
sys.stdin = open('input.txt')
from collections import deque

# 시계방향
delta = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # 북 동 남 서(0, 1, 2, 3)
counter_index = [2, 3, 0, 1]
change_dice = [(4, 1, 5, 3), (0, 4, 2, 5), (5, 1, 4, 3), (0, 5, 2, 4)] # 북 동 남 서

def calculate_score(r, c, B):
    global score
    Q = deque([(r, c)])
    visited = [[0]*M for _ in range(N)]
    score += B
    visited[r][c] = 1
    while Q:
        sr, sc = Q.popleft()
        for d in range(4):
            nr = sr + delta[d][0]
            nc = sc + delta[d][1]
            if 0 <= nr < N and 0 <= nc < M and data[nr][nc] == B and not visited[nr][nc]:
                visited[nr][nc] = 1
                score += 1*B
                Q.append((nr, nc))


def solution(r, c, direction, dice, times):
    if times == 0:
        return

    nr = r + delta[direction][0]
    nc = c + delta[direction][1]
    if 0 <= nr < N and 0 <= nc < M:
        A = dice[direction]
        B = data[nr][nc]

    else:
        direction = counter_index[direction]
        nr = r + delta[direction][0]
        nc = c + delta[direction][1]
        A = dice[direction]
        B = data[nr][nc]

    calculate_score(nr, nc, B)
    now_dice = [dice[change_dice[direction][0]], dice[change_dice[direction][1]],
                dice[change_dice[direction][2]], dice[change_dice[direction][3]], 7 - A, A]

    if A > B:
        new_direction = (direction + 1) % 4
    elif A < B:
        new_direction = ((direction - 1) + 4) % 4
    else:
        new_direction = direction

    return solution(nr, nc, new_direction, now_dice, times-1)



T = int(input())
for tc in range(1, T+1):
    N, M, times = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(N)]

    score = 0
    dice = [2, 3, 5, 4, 1, 6]     # 북 동 남 서 위 아래

    solution(0, 0, 1, dice, times)
    print(score)