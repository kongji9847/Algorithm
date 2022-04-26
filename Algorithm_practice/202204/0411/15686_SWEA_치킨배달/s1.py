# 모든 조합을 확인 + heap 사용해서 최소값 뽑기
# import sys
# sys.stdin = open('input.txt')

import heapq
def dfs(now, N, numbers):
    global min_ans
    # 종료 - 모든 자리수가 채워지는 순간
    if N == M:
        heap2 = []
        ans = 0
        visited = [0]*(len(houses))                             # 집을 방문했는지 확인
        flag = 0                                                # 방문한 집의 개수 체크

        while flag < len(houses):
            dist, chick, house = heapq.heappop(heap)
            heap2.append((dist, chick, house))                  # heap에서 뺀 원소 heap2에 저장하기 -> 결과값 나온후 heap에 다시 넣어줌

            if not visited[house] and chick in numbers:         # 조합 안에 있는 치킨이고 방문한적 없는 집이면
                visited[house] = 1                              # 방문체크
                ans += dist                                     # 거리 누적
                flag += 1                                       # 집 개수 추가

        if min_ans > ans:                                       # min_ans 갱신
            min_ans = ans

        for i in range(len(heap2)-1, -1, -1):                   # heap2를 다시 heap에 넣어준다.
            heapq.heappush(heap, heap2[i])
        return

    # 진행 - 범위 맞춰서 뽑기
    for i in range(now+1, len(chickens)-(M-N)+1):
        dfs(i, N+1, numbers+[i])

# 1. input 받기
# T = int(input())
# for tc in range(1, T+1):
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

# i번째 치킨집에서 j번째 집까지 가는 치킨거리
heap = []
for i in range(len(chickens)):
    for j in range(len(houses)):
        distance = abs(chickens[i][0] - houses[j][0]) + abs(chickens[i][1] - houses[j][1])
        heapq.heappush(heap, (distance, i, j))

min_ans = 987654321
dfs(-1, 0, [])
print(min_ans)