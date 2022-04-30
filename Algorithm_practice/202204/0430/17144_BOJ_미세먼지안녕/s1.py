# import sys
# sys.stdin = open('input.txt')
# #from pprint import pprint

delta = [(0, 1), (-1, 0), (0, -1), (1, 0)]

#2. 1초 동안 일어나는 일
def solution():
    # 2-1. 확산
    after = [[0]*C for _ in range(R)]
    for r in range(R):
        for c in range(C):
            room_cnt = 0
            if data[r][c] == -1:
                after[r][c] = -1
            else:
                for d in range(4):
                    nr = r + delta[d][0]
                    nc = c + delta[d][1]
                    if 0 <= nr < R and 0 <= nc < C and data[nr][nc] != -1:
                        after[nr][nc] += data[r][c]//5
                        room_cnt += 1
                after[r][c] += data[r][c] - (data[r][c]//5) * room_cnt

    # 2-2. 공기청정기 작동
    data[clear_r-1][1] = 0
    data[clear_r][1] = 0
    for c1 in range(1, C-1):                                # → 방향 (공기청정기 2개)
        data[clear_r-1][c1+1] = after[clear_r-1][c1]
        data[clear_r][c1+1] = after[clear_r][c1]

    for r1 in range(clear_r-1, 0, -1):                      # ↓ 방향 (위쪽 공기청정기)
        data[r1-1][C-1] = after[r1][C-1]

    for c2 in range(C-1, 0, -1):                            # ← 방향  (공기청정기 2개)
        data[0][c2 - 1] = after[0][c2]
        data[R-1][c2-1] = after[R-1][c2]

    for r2 in range(0, clear_r-2):                          # ↑ 방향 (위쪽 공기청정기)
        data[r2+1][0] = after[r2][0]

    for r3 in range(clear_r, R-1):                          # ↓ 방향 (아래쪽 공기청정기)
        data[r3+1][C-1] = after[r3][C-1]

    for r4 in range(R-1, clear_r+1, -1):                    # ↑ 방향 (아래쪽 공기청정기)
        data[r4-1][0] = after[r4][0]

    # 2-3. 공기청정기로 이동한 먼지 제외한, 이동하지 않은 먼지 data에 넣어주기
    for r in range(1, R-1):
        for c in range(1, C-1):
            if r == clear_r or r == clear_r-1:
                continue
            else:
                data[r][c] = after[r][c]



# T = int(input())
# for tc in range(1, T+1):
R, C, Time = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(R)]

for clean_r in range(R):
    if data[clean_r][0] == -1:
        clear_r = clean_r+1
        break

# 1. 가동시간만큼 반복
for t in range(Time):
    solution()

# 3. 가동이 끝나고 먼지 수 더해주기
total = 2
for r in range(R):
    for c in range(C):
        total += data[r][c]
print(total)