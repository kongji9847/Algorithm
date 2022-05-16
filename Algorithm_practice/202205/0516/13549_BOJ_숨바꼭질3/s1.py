# bfs 사용: 오답 -> 가지 개수가 같아도 가중치가 다르다.

import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

from collections import deque

def bfs():
    Q = deque([[N, 0]])
    while True:
        now = Q.popleft()
        now_indx = now[0]
        now_value = now[1]
        if now_indx == K:
            print(now_value)
            return
        for next in [now_indx*2, now_indx+1, now_indx-1]:
            if 0 <= next < 100001 and not visited[next]:
                visited[next] = 1
                if next == now_indx*2:
                    Q.append([next, now_value])
                else:
                    Q.append([next, now_value+1])


N, K = map(int, input().split())
visited = [0] * 100001
visited[N] = 1
bfs()

