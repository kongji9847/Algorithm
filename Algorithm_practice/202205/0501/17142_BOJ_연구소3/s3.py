# itertools 사용 + 모든 칸 돌면서 바이러스 퍼질 수 있는지 확인 + deepcopy 사용 -> 시간 초과
import sys
#sys.stdin = open('input.txt')
from copy import deepcopy
#import sys
input = sys.stdin.readline
from itertools import combinations

from pprint import pprint

def choosing():
    global min_time
    global possible
    # 종료
    every_list = list(combinations(viruses, M))
    #pprint(every_list)
    for element in every_list:
        now_time = spread(element)
        if now_time != -1:
            min_time = min(min_time, now_time)
            possible = 1


delta = [(-1, 0), (1, 0), (0, 1), (0, -1)]
def spread(chosen):
    new_data = deepcopy(data)
    for element in chosen:
        new_data[element[0]][element[1]] = '0'

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


# T = int(input())
# for tc in range(1, T+1):
N, M = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(N)]
viruses = []
holes = 0
for r in range(N):
    for c in range(N):
        if data[r][c] == 1:
            data[r][c] = -1
        elif data[r][c] == 2:
            data[r][c] = '*'
            viruses.append((r, c))
        elif data[r][c] == 0:
            holes += 1

min_time = 1000
if holes == 0:
    print(0)
else:
    possible = 0
    choosing()
    if possible:
        print(min_time)
    else:
        print(-1)