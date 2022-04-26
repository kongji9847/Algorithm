# import sys
# sys.stdin = open('input.txt')
# from pprint import pprint

from collections import deque
delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# T = int(input())
# for tc in range(1, T+1):

# 1. input 받기
N, Q = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(2**N)]
levels = list(map(int, input().split()))

# 2. 각 level에서 파이어스톰 마법 시전하기
for level in levels:        # 주어진 각 level을 돌면서

    # 2.1 배열을 2**N X 2**N으로 나누고 시계방향으로 90도 돌리기
    new_data = [[] for _ in range(2**N)]
    for i in range(2**(N-level)):                                               # 새로운 행의 위치를 표현하기 위해
        for j in range(2**(N-level)):                                           # 현재 data의 열의 위치를 표현하기 위해
            for k in range(2**level):                                           # 2**level의 개수만큼
                for l in range((i+1)*2**level-1, i*2**level-1, -1):
                    new_data[i*2**level+k].append(data[l][j*2**level + k])

    # 2.2 깎아야 할 ice 위치 모으기
    reduce_ice = []
    for r in range(2**N):
        for c in range(2**N):
            if new_data[r][c] > 0:
                flag = 4
                for d in range(4):
                    nr = r + delta[d][0]
                    nc = c + delta[d][1]
                    if not (0 <= nr < 2**N and 0 <= nc < 2**N):
                        flag -= 1
                    else:
                        if new_data[nr][nc] == 0:
                            flag -= 1
                if flag < 3:
                    reduce_ice.append((r, c))

    # 2.3 ice 깎기
    for element in reduce_ice:
        new_data[element[0]][element[1]] -= 1

    # 2.4 하나의 레벨이 끝나고 배열을 마법이 적용된 배열로 갱신하기
    data = new_data

# 3. 모든 레벨에 따른 마법이 끝나고,
# 가장 큰 얼음 덩어리 찾고, 얼음 개수 다 합치기 - bfs
total_ice = 0                                       # 남아있는 얼음 총합
max_ice = 0                                         # 가장 큰 얼음 덩어리
ice_box = 0                                         # 얼음 덩어리
for r in range(2**N):
    for c in range(2**N):                           # 모든 배열을 돌면서 얼음 덩어리가 있다면, 해당 얼음 덩어리와 연결된 섬 찾으며 얼음 덩어리 카운팅
        if data[r][c] > 0:                          # 얼음 덩어리를 발견했다면
            ice_box = 1                             # 섬의 넓이를 1로 초기화하고
            total_ice += data[r][c]                 # total 얼음에도 추가를 하고
            data[r][c] = 0                          # 방문 표시한다.
            Q = deque([(r, c)])                     # Q에 넣어 시작한다.

            # bfs를 진행하면서 모든 연결된 얼음덩어리 개수 구하고 방문표시한다. 탐색한 얼음덩어리는 total에 추가한다.
            while Q:
                sr, sc = Q.popleft()
                for d in range(4):
                    nr = sr + delta[d][0]
                    nc = sc + delta[d][1]
                    if 0 <= nr < 2**N and 0 <= nc < 2**N and data[nr][nc] > 0:
                        Q.append((nr, nc))
                        total_ice += data[nr][nc]
                        data[nr][nc] = 0
                        ice_box += 1

        # 더이상 연결된 얼음 덩어리가 없을 때,
        # 최대 얼음 덩어리 값을 갱신하고, 다시 반복문으로 넘어가 다른 얼음 덩어리를 찾는다.
        max_ice = max(max_ice, ice_box)

print(total_ice)
print(max_ice)