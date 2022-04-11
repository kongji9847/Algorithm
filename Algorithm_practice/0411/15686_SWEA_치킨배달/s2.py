# greedy 도전 -> 불가능
import sys
sys.stdin = open('input.txt')

import heapq
def dfs(numbers):
    # 종료
    ans = 0
    visited = [0]*(len(houses))
    flag1 = 0
    flag2 = 0
    while flag1 < len(houses):
        dist, chick, house = heapq.heappop(heap)

        if not visited[house]:
            if numbers[chick] == 1:
                visited[house] = 1
                ans += dist
                flag1 += 1
            elif numbers[chick] == 0 and flag2 < M:
                visited[house] = 1
                ans += dist
                flag1 += 1
                numbers[chick] = 1
                flag2 += 1
    return ans


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(N)]
    chickens = []
    houses = []
    for r in range(N):
        for c in range(N):
            if data[r][c] == 1:
                houses.append((r, c))
            elif data[r][c] == 2:
                chickens.append((r, c))

    heap = []
    for i in range(len(chickens)):
        for j in range(len(houses)):
            distance = abs(chickens[i][0] - houses[j][0]) + abs(chickens[i][1] - houses[j][1])
            heapq.heappush(heap, (distance, i, j))

    min_ans = 987654321
    print(dfs([0]*len(chickens)))