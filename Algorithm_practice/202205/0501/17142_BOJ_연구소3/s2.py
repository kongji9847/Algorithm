# 재귀로 조합 구현 + 모든 칸 돌면서 바이러스 퍼질 수 있는지 확인 + deepcopy 사용 안함 -> 시간 초과
# import sys
# sys.stdin = open('input.txt')
# from pprint import pprint
import sys
input = sys.stdin.readline

def choosing(choosing_cnt, chosen):
    global min_time
    global possible
    # 종료
    if choosing_cnt == M:
        now_time = spread(chosen)

        for wall_element_r, wall_element_c in walls:
            new_data[wall_element_r][wall_element_c] = -1
        for viruse_r, viruse_c in viruses:
            new_data[viruse_r][viruse_c] = '*'
        for hole_r, hole_c in hole_box:
            new_data[hole_r][hole_c] = 0


        if now_time != -1:
            min_time = min(min_time, now_time)
            possible = 1
        return

    # 진행
    for now in range(chosen[-1]+1, len(viruses)-(M-(choosing_cnt+1))):
        choosing(choosing_cnt+1, chosen+[now])

delta = [(-1, 0), (1, 0), (0, 1), (0, -1)]
def spread(chosen):
    for element in chosen[1:]:
        new_data[viruses[element][0]][viruses[element][1]] = '0'

    sec = 1
    new_hole = holes
    new_new_hole = new_hole
    while True:
        if sec > min_time:
            return -1
        for r in range(N):
            for c in range(N):
                if sec == 1:
                    if new_data[r][c] == '0':
                        for d in range(4):
                            nr = r + delta[d][0]
                            nc = c + delta[d][1]
                            if 0 <= nr < N and 0 <= nc < N and new_data[nr][nc] == 0:
                                new_data[nr][nc] = 1
                                new_new_hole -= 1

                else:
                    if new_data[r][c] == sec-1:
                        for d in range(4):
                            nr = r + delta[d][0]
                            nc = c + delta[d][1]
                            if 0 <= nr < N and 0 <= nc < N and new_data[nr][nc] == 0:
                                new_data[nr][nc] = sec
                                new_new_hole -= 1

        if new_new_hole == 0:
            #print(new_new_hole)
            #print(sec)
            return sec
        elif new_hole == new_new_hole:
            return -1
        else:
            new_hole = new_new_hole
            sec += 1

#
# T = int(input())
# for tc in range(1, T+1):
N, M = map(int, input().split())
new_data = [list(map(int, input().split())) for _ in range(N)]
viruses = []

walls = []
hole_box = []
for r in range(N):
    for c in range(N):
        if new_data[r][c] == 1:
            new_data[r][c] = -1
            walls.append((r,c))
        elif new_data[r][c] == 2:
            new_data[r][c] = '*'
            viruses.append((r, c))
        elif new_data[r][c] == 0:
            hole_box.append((r, c))

holes = len(hole_box)
min_time = 1000
if holes == 0:
    print(0)
else:
    possible = 0
    choosing(0, [-1])
    if possible:
        print(min_time)
    else:
        print(-1)