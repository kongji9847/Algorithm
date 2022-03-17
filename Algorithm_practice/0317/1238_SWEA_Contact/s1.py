# 원형으로 순환하는 형태도 있기 때문에, 1차원 visited를 사용해서 해당 숫자는 다른 루트로도 더 이상 가지 않겠다는 표시가 필요하다.

from collections import deque
# 2. 중심에서 같은 거리는 동시에 진행 -> bfs
def bfs(start):
    Q = deque([(start, 0)])
    visited[start] = 1
    max_cnt = 0
    stack = []

    while Q:
        start, cnt = Q.popleft()
        for i in range(1, 100+1):
            if phone_book[start][i] == 1 and not visited[i]:
                visited[i] = 1
                Q.append((i, cnt+1))
                if max_cnt < cnt+1:
                    max_cnt = cnt+1
                    stack = []
                    stack.append(i)
                elif max_cnt == cnt+1:
                    stack.append(i)
    return max(stack)

# 1. input 받기
import sys
sys.stdin = open('input.txt')

T = 10
for tc in range(1, T+1):
    N, start = map(int, input().split())
    phone_book = [[0]*(100+1) for _ in range(100+1)]
    data = list(map(int, input().split()))
    visited = [0] * 101
    for i in range(N//2):
        phone_book[data[i*2]][data[i*2+1]] = 1

    print(f'#{tc}', bfs(start))