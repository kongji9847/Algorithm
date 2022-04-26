# import sys
# sys.stdin = open('input.txt')

# 허리케인 이동방향
delta = [(0, -1), (1, 0), (0, 1), (-1, 0)]

# 2. 허리케인 방향에 맞춰 비율 배열 바꾸기 -> arr를 반시계방향으로 90도 회전하는 함수
def rotate_90(proportion):
    new_proportion = list(reversed(list(zip(*proportion))))
    return new_proportion
p = [[0, 0, 0.02, 0, 0], [0, 0.1, 0.07, 0.01, 0], [0.05, 0, 0, 0, 0], [0, 0.1, 0.07, 0.01, 0], [0, 0, 0.02, 0, 0]]
p1 = rotate_90(p)
p2 = rotate_90(p1)
p3 = rotate_90(p2)
proportions = [p, p1, p2, p3]
alphas = [(2, 1), (3, 2), (2, 3), (1, 2)]           # 허리케인 이동 방향에 따른 알파 위치

# 3. 허리케인 이동 + 모래 이동
def solution():
    # 3-1. 초기 조건 맞추기
    outer_sand = 0                                  # 배열 밖으로 나간 sand
    tr = sr                                         # 토네이도 위치 인덱스 -> 시작 지점 부터 시작
    tc = sc
    curl = 0                                        # 현재 토네이도 방향
    turn = 2                                        # 토네이도 방향 바꾸는 지표 -> 좌-하 : turn = 2 /우-상: turn = 4, 2씩 늘어난다.
    now = 0                                         # 토네이도 직선 길이
    proportion = proportions[0]                     # 토네이도 방향에 따른 비율 배열

    # 3-2 토네이도가 종료될때까지 토네이도 이동 -> 모래 이동 -> 토네이도 방향 바꾸기
    while not (tr == 0 and tc == 0):                # 토네이도가 종료될 때까지 반복한다.

        # 3-2-1. 토네이도 이동
        tr += delta[curl][0]                        # 현재 토네이도 위치
        tc += delta[curl][1]
        now += 1                                    # 토네이도 길이 갱신
        sand = data[tr][tc]
        data[tr][tc] = 0                            # 토네이도 위치에 있는 모래는 모두 proportion에 따라 이동한다.
        left = sand                                 # proportion으로 이동하고 남은 모래

        # 3-2-2. proportion의 y위치와 data의 토네이도 위치를 일치 시켜 모래 정보 갱신하기
        for r in range(5):
            for c in range(5):
                now_sand = int(sand * proportion[r][c])
                left -= now_sand
                if 0 <= tr + r - 2 < N and 0 <= tc + c - 2 < N:                                 # data 배열 안에 가능하다면 data 갱신
                    data[tr + r - 2][tc + c - 2] += now_sand
                else:                                                                           # 불가능 하다면 밖으로 나간 모래
                    outer_sand += now_sand

        # alph 위치에 남은 모래 두기
        if 0 <= tr + alphas[curl][0]- 2 < N and 0 <= tc + alphas[curl][1] - 2 < N:
            data[tr + alphas[curl][0] - 2][tc + alphas[curl][1] - 2] += left
        else:
            outer_sand += left

        # 3-2-3. 토네이도 방향 바꾸기
        if now == turn // 2 or now == turn:
            curl = (curl + 1) % 4
            proportion = proportions[curl]
            if now == turn:
                now = 0
                turn += 2

    # 3-3. 토네이도 종료 후 바깥의 모래
    print(outer_sand)
    return


# 1. input 받기
# T = int(input())
# for tc in range(1, T+1):
N = int(input())
sr = sc = N//2              # 허리케인 시작지점
data = [list(map(int, input().split())) for _ in range(N)]
solution()