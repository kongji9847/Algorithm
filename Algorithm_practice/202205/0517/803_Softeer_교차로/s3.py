# 시간 흐름에 따라 input 받기 -> 정답(input을 받은 for문이 1개)
import sys
input = sys.stdin.readline
from collections import deque

# ABCD => DABC
road_indx = {'A': 0, 'B': 1, 'C': 2, 'D': 3}
counter_road = [3, 0, 1, 2]

N = int(input())
all_cars = [-1] * N         # 0. 모든 차량이 빠져나오는 시각 구하기 -> 우선 default는 -1로 두기!
roads = [deque([]), deque([]), deque([]), deque([])]

# 1. 첫번째 input -> 시작 시각 정하기
ft, fw = input().split()
now = int(ft)
roads[road_indx[fw]].append(0)

# deadlock 상황인지 확인하는 flag 변수 -> deadlock이면 input만 받을꺼임
deadlock = 0

# 2. 2번째 input부터 받으면서 시간 흐름 로직 작성
for i in range(1, N):
    t, w = input().split()
    t = int(t)

    # 2-1. deadlock이 아니며, 현재 시각과 input 시각이 동일한 경우, 차로에 input 값 저장하기
    if not deadlock and t == now:
        roads[road_indx[w]].append(i)

    # 2-2. deadlock이 아니며, input 시각이 현재 시각보다 큰 경우
    elif not deadlock and t > now:

        # 1) now가 input 시각과 같아질 때까지 반복문으로 시간 흐르면서 차를 통과시키기
        for time in range(now, t):
            cars = []
            flag = 0

            # 1-1) 4방향의 도로를 보면서 빠져나갈 차가 있는 지 확인
            for d in range(4):
                if roads[d]:
                    flag += 1       # 차 자체가 도로에 있는지 확인하는 flag 변수
                    if not (roads[counter_road[d]]):    # 차가 빠져나갈 수 있는 상태라면 우선 cars에 저장해두기
                        cars.append(d)

            # 1-2) 모든 도로를 확인한 후, 빠져나갈 차가 있다면
            if cars:
                for car_d in cars:
                    indx = roads[car_d].popleft()       # 빠져나간 차의 indx를 저장
                    all_cars[indx] = time               # 현재 시각 저장

            # 1-3) 빠져나간 차가 없는데,
            else:
                if flag > 0:                            # 도로에 차는 있다면 교착 상태
                    deadlock = 1
                    break                               # 시간 흐름 for문 빠져나오기
                else:                                   # 도로에 차가 없어서 차가 빠져나오지 않았으므로
                    break                               # 바로 다음 input으로 가기 위해 for문 빠져나오기

        # 2) 시간이 모두 흘렀거나 break문으로 시간 흐름을 빠져나왔다면
        now = t                                         # now는 현재의 input의 시각이 된다.
        roads[road_indx[w]].append(i)


# 3. 모든 input은 받았지만, 교착상태가 아니고 도로에 차가 남아있다면 -> 해당 조건 중 하나를 만족시킬때까지 시간 흐름
while not deadlock and (roads != [deque([]), deque([]), deque([]), deque([])]):
    cars = []
    flag = 0
    for d in range(4):
        if roads[d]:
            flag += 1
            if not (roads[counter_road[d]]):
                cars.append(d)
    if cars:
        for car in cars:
            indx = roads[car].popleft()
            all_cars[indx] = now
    else:
        if flag > 0:
            end = 0
            break
        else:
            break
    now += 1                # 시간 흐름


for i in range(N):
    print(all_cars[i])