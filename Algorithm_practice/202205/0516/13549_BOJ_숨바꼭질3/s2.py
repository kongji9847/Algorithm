# 다익스트라 사용 : 정답

import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

import heapq

def dijstra():
    heap = []
    heapq.heappush(heap, (0, N))
    while True:
        now = heapq.heappop(heap)
        now_indx = now[1]
        now_value = now[0]
        visited[now_indx] = 1

        if now_indx == K:                                           # 목표 지점이 나오면 return으로 while True 중지
            print(now_value)
            return

        for next in [now_indx*2, now_indx+1, now_indx-1]:
            if 0 <= next < 100001 and not visited[next]:
                if next == now_indx*2:
                    heapq.heappush(heap, (now_value, next))
                else:
                    heapq.heappush(heap, (now_value+1, next))


N, K = map(int, input().split())
visited = [0] * 100001
dijstra()

