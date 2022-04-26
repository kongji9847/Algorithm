# import sys
# sys.stdin = open('input.txt')

from pprint import pprint
from collections import deque

delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]
# def rotate_arr(data):
#     for level in levels:
#         new_data = [[] for _ in range(2**N)]
#         for i in range(2**(N-level)):
#             for j in range(2**(N-level)):
#                 for k in range(2**level):
#                     for l in range((i+1)*2**level-1, i*2**level-1, -1):
#                         new_data[i*2**level+k].append(data[l][j*2**level + k])
#
#
#         reduce_ice = []
#         for r in range(2**N):
#             for c in range(2**N):
#                 flag = 4
#                 for d in range(4):
#                     nr = r + delta[d][0]
#                     nc = c + delta[d][1]
#                     if not (0 <= nr < 2**N and 0 <= nc < 2**N):
#                         flag -= 1
#                     else:
#                         if new_data[nr][nc] == 0:
#                             flag -= 1
#                 if flag < 3:
#                     reduce_ice.append((r, c))
#
#         for element in reduce_ice:
#             new_data[element[0]][element[1]] -= 1
#
#         data = new_data
#
#     total_ice = 0
#     max_ice = 0
#     ice_box = 0
#     for r in range(2**N):
#         for c in range(2**N):
#             if data[r][c] > 0:
#                 ice_box = 1
#                 Q = deque([(r, c)])
#                 total_ice += data[r][c]
#                 data[r][c] = 0
#
#                 while Q:
#                     sr, sc = Q.popleft()
#                     for d in range(4):
#                         nr = sr + delta[d][0]
#                         nc = sc + delta[d][1]
#                         if 0 <= nr < 2**N and 0 <= nc < 2**N and data[nr][nc] > 0:
#                             Q.append((nr, nc))
#                             total_ice += data[nr][nc]
#                             data[nr][nc] = 0
#                             ice_box += 1
#
#             max_ice = max(max_ice, ice_box)
#     #pprint(data)
#     print(total_ice)
#     print(max_ice)



# T = int(input())
# for tc in range(1, T+1):
N, Q = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(2**N)]
levels = list(map(int, input().split()))
#rotate_arr(data)

for level in levels:
    new_data = [[] for _ in range(2**N)]
    for i in range(2**(N-level)):
        for j in range(2**(N-level)):
            for k in range(2**level):
                for l in range((i+1)*2**level-1, i*2**level-1, -1):
                    new_data[i*2**level+k].append(data[l][j*2**level + k])


    reduce_ice = []
    for r in range(2**N):
        for c in range(2**N):
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

    for element in reduce_ice:
        new_data[element[0]][element[1]] -= 1

    data = new_data

total_ice = 0
max_ice = 0
ice_box = 0
for r in range(2**N):
    for c in range(2**N):
        if data[r][c] > 0:
            ice_box = 1
            Q = deque([(r, c)])
            total_ice += data[r][c]
            data[r][c] = 0

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

        max_ice = max(max_ice, ice_box)
#pprint(data)
print(total_ice)
print(max_ice)