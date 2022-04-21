'''
주사위가 북, 동, 남, 서로 굴러갔을 때 전개도가 바뀌는 모양

if 주사위가 북쪽으로 굴러가면 change_dice[0]을 사용(4, 1, 5, 3)
새로운 주사위 전개도의 북쪽은 기존 전개도의 4번 인덱스에 해당하는 값과 동일하다.
new_dice[0] = dice[change_dice][0][0]]
'''

# import sys
# sys.stdin = open('input.txt')
from collections import deque

delta = [(-1, 0), (0, 1), (1, 0), (0, -1)]          # 북 동 남 서(0, 1, 2, 3) -> 시계방향 순서
counter_index = [2, 3, 0, 1]                        # 각 반대 방향의 인덱스 북(0)쪽의 반대는 남(2) -> counter_index[0] = 2
change_dice = [(4, 1, 5, 3), (0, 4, 2, 5), (5, 1, 4, 3), (0, 5, 2, 4)]              # 주사위가 북, 동, 남, 서로 굴러갔을 때 전개도가 바뀌는 모양

# 4. 현재 상태에서의 점수 계산 - bfs 사용
def calculate_score(r, c, B):
    global score
    Q = deque([(r, c)])
    visited = [[0]*M for _ in range(N)]
    score += B                              # 지금 밟고 있는 판도 점수에 포함한다.
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


# 3. 시행을 반복하며 방향에 따라 주사위를 굴린다.
def solution(r, c, direction, dice):
    #3-1. 주어진만큼 시행을 반복
    for _ in range(times):
        # 3-2. direction 방향으로 주사위를 굴리고 A, B 값 확인
        nr = r + delta[direction][0]
        nc = c + delta[direction][1]
        if 0 <= nr < N and 0 <= nc < M:                 # 주사위를 direction 방향으로 굴렸을 때 위치가 인덱스 에러 없다.
            A = dice[direction]                         # A: 주사위를 굴린 후 바닥면
            B = data[nr][nc]                            # B: 주사위가 있는 위치의 board 값
        else:
            direction = counter_index[direction]        # 인덱스 에러가 있다면, 반대방향으로 굴리고 위치 수정
            nr = r + delta[direction][0]
            nc = c + delta[direction][1]
            A = dice[direction]
            B = data[nr][nc]

        # 3-3. 주사위를 굴린 상태에서 점수 계산
        calculate_score(nr, nc, B)

        # 3-4. 주사위를 굴렸으므로 주사위 전개도 변화 -> dice에 반영한다.
        dice = [dice[change_dice[direction][0]], dice[change_dice[direction][1]],
                dice[change_dice[direction][2]], dice[change_dice[direction][3]], 7 - A, A]

        # 3-5. A, B 값 비교해서 다음 시행에서 주사위를 굴릴 방향 정하기
        if A > B:
            direction = (direction + 1) % 4                 # 시계 방향
        elif A < B:
            direction = ((direction - 1) + 4) % 4           # 반시계 방향

        # 3-6. 다음 시행에서 현재의 nr, nc가 r, c가 되어야 하므로 값 갱신하기
        r, c = nr, nc



# T = int(input())
# for tc in range(1, T+1):

# 1. input 받기: N:행, M:열, tiems: 시행횟수, data: 보드판
N, M, times = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(N)]

# 2.함수 사용해서 점수 계산하기
score = 0
dice = [2, 3, 5, 4, 1, 6]       # 북 동 남 서 위 아래 -> 초기 주사위 전개도
solution(0, 0, 1, dice)
print(score)