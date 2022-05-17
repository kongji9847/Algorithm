# 시간 초과 -> case가 거대함
import sys
input = sys.stdin.readline

from collections import deque

# ABCD => DABC
road_indx = {'A':0, 'B':1, 'C':2, 'D':3}
counter_road = [3, 0, 1, 2]

N = int(input())
all_cars = [-1] * N
roads = [deque([]), deque([]), deque([]), deque([])]

# 1. input 받기
ft, fw = input().split()
now = int(ft)
roads[road_indx[fw]].append((0, int(ft)))

for i in range(1, N):
    t, w = input().split()
    roads[road_indx[w]].append((i, int(t)))

# 2. 시간 흐름에 따라 교차로에 있는 차 정리하기
cnt = 0
while cnt < N:
    cars = []
    flag = 0
    for d in range(4):
        if roads[d] and roads[d][0][1] <= now:
            flag += 1
            if not (roads[counter_road[d]] and roads[counter_road[d]][0][1] <= now):
                cars.append(d)

    if cars:
        for car in cars:
            indx, s = roads[car].popleft()
            cnt += 1
            all_cars[indx] = now

    else:
        if flag > 0:
            break

    now += 1

for i in range(N):
    print(all_cars[i])