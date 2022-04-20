# 문제에서 알려준 순서대로 코드짜기 -> 순서가 중요한 문제
# 상어는 원래 자기 위치로 돌아갈 수 있다. 좌 우 우 가능

import sys
sys.stdin = open('input.txt')

from copy import deepcopy
from collections import deque
# 반시계는 역순으로
delta = [(0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]              # 물고기 이동 방향
delta2 = [(-1, 0), (0, -1), (1, 0), (0, 1)][::-1]                                           # 상어 이동 방향 -> 거꾸로된 사전순

# 2. 물고기가 움직일 수 있는지 확인하고, 움직일 수 있다면 new_data에 표시해준다.
# fr, fc 물고기 현재 위치, direction: 이동방향
def fish_move(fr, fc, direction):
    nr = fr + delta[direction][0]
    nc = fc + delta[direction][1]
    # 인덱스 에러 안나고, 상어 위치와 겹치지 않고, 물고기 냄새와 겹치지 않아야 한다.
    if 0 <= nr < 4 and 0 <= nc < 4 and not(nr == Sr and nc == Sc) and smell_data[nr][nc] == 0:
        new_data[nr][nc].append(direction)
        return True
    # 움직일 수 없다면 false 반환
    else:
        return False

# 3. 상어가 이동해야 하는 방향 확인하는 함수(bfs) -> 역 사전순으로 탐지하고, 값이 갱신될 때마다 방향도 갱신해준다.
# 결국 마지막엔 사전순으로 가장 먼저 있는 방향이 반환되게 된다.
# sr, sc : 현재 상어 위치
def shark_move(sr, sc):
    max_fish = 0
    Q = deque([[0, (sr, sc)]])                                  # [없앤 물고기 수, (시작하는 상어 위치)]
    while Q:                                                    # [없앤 물고기 수, (시작하는 상어 위치), (1칸 움직임), (2칸 움직임), (3칸 움직임)]
        now = Q.popleft()                                       # now: Q에서 뽑아낸 원소 -> 다음 위치를 추가해서 Q에 다시 집어 넣어야 한다.
        # 3-2. 종료조건
        if len(now) == 5:                                       # 3칸을 이동했다면, continue 해줘서 다음 Q 원소 보기
            if max_fish <= now[0]:                              # max_fish 값을 갱신하거나 값이 동일하다면
                max_fish = now[0]
                position = [now[2], now[3], now[4]]             # position 갱신 -> position: 상어가 3칸 움직인 궤적
            continue

        # 3-1. 진행
        r, c = now[-1][0], now[-1][1]                           # 현재 상어 위치
        for d in range(4):                                      # 4방향을 모두 돌면서
            nr, nc = r+delta2[d][0], c+delta2[d][1]
            if 0 <= nr < 4 and 0 <= nc < 4:                     # 새로운 위치가 인덱스 에러가 나지 않는지 확인한다.
                new_now = deepcopy(now)                         # new_now를 생성(now는 다음 방향에서도 써야하므로)
                if not (nr, nc) in now[2:]:                     # 전에 방문해서 물고기를 잡았다면 다시 물고기를 카운팅하지 않는다.(시작 위치로는 돌아갈 수 있다.)
                    new_now[0] += len(new_data[nr][nc])         # 잡은 물고기 카운팅
                new_now.append((nr, nc))                        # 새로운 상어 위치를 new_now에 추가하고 new_now를 Q에 추가한다.
                Q.append(new_now)

    # 3-3. 상어가 갈 수 있는 최종 궤적 리턴
    return position

# 4. 주어진 순서대로 연습 1회 하는 함수
def solution():
    # 상어 위치가 함수 안에서 갱신되므로 필요하다.
    global Sr
    global Sc

    # 4-1. 모든 칸을 돌면서 물고기를 이동시킨 결과를 new_data에 입력한다.
    for fr in range(4):
        for fc in range(4):
            if data[fr][fc]:
                for fish_direction in data[fr][fc]:                         # 물고기 한 마리씩 이동한다.
                    change_direction = fish_direction                       # 물고기가 이동하며 방향이 바뀌기도 하는 것을 change_dir로 나타낸다.
                    while True:                                             # break 문을 만날 때까지 반복
                        if fish_move(fr, fc, change_direction):             # 물고기가 이동가능하다면 반복문 빠져나오기
                            break
                        else:
                            change_direction -= 1                           # 이동불가능 하다면 회전하기
                            if change_direction < 0:
                                change_direction += 8                       # 방향을 양수 인덱스로 바꿔줘야 하므로
                            if fish_direction == change_direction:          # 모든 방향을 다 봐도 불가능하면 이동시키지 않고 new_data에 추가하고 break
                                new_data[fr][fc].append(fish_direction)
                                break

    # 4-2. shark_move 함수 써서 상어 이동해주고, 물고기 제거하기
    position = shark_move(Sr, Sc)
    for pos in position:                                # 상어를 한칸씩 이동하면서
        if new_data[pos[0]][pos[1]]:                    # 물고기가 있다면
            new_data[pos[0]][pos[1]] = []               # 물고기 제거
            smell_data[pos[0]][pos[1]] = -3             # -3으로 물고기 냄새 표시
    Sr, Sc = pos[0], pos[1]                             # 마지막 3번째 칸에서 상어 위치 갱신

    # 4-3. 냄새 데이터 사라지게 하기
    for r in range(4):
        for c in range(4):
            if smell_data[r][c]:                        # 냄새가 있다면 (-1, -2, -3)
                smell_data[r][c] += 1                   # 1을 더해줘서 냄새 제거하기 (0, -1, -2) -> 결국 함수가 다 끝나면 -3은 -2로 끝난다.

    # 4-4. 복제한 물고기와 합쳐 data 갱신하기
    for r in range(4):
        for c in range(4):
            data[r][c] += new_data[r][c]


T = int(input())
for tc in range(1, T+1):

    # 1. input 받기
    M, S = map(int, input().split())                                # M = 물고기 수, S = 연습 횟수

    # 1-1. data : 4x4 격자에 물고기 넣기(인덱스는 0부터)
    data = [[[] for _ in range(4)] for _ in range(4)]
    for _ in range(M):
        fr, fc, d = map(int, input().split())
        data[fr-1][fc-1].append(d-1)

    # 1-2. 상어 좌표(Sr, Sc), 인덱스 맞추기
    Sr, Sc = map(int, input().split())
    Sr, Sc = Sr-1, Sc-1

    smell_data = [[0]*4 for _ in range(4)]                          # 물고기 냄새 표시할 데이터

    # 1-3. 연습 횟수만큼 시행 반복하기
    for practice in range(S):
        new_data = [[[] for _ in range(4)] for _ in range(4)]       # 이동한 물고기를 담을 새로운 격자 - 매 연습마다 필요
        solution()

    # 5. 결과 내기 - 물고기 숫자 세기
    ans = 0
    for r in range(4):
        for c in range(4):
            ans += len(data[r][c])
    print(ans)