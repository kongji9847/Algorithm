from collections import deque

# 최대 거리 구하기 -> bfs 사용
delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]      # 상하좌우
def bfs(r, c):
    max_cnt = 0
    Q = deque([(r, c, 1)])
    while Q:
        (r, c, cnt) = Q.popleft()

        # 상하좌우 움직이기 -> visited 할 필요없음 지나온 자리는 이미 1만큼 작기 때문에 되돌아가지 않는다.
        for i in range(4):
            nr, nc = r + delta[i][0], c + delta[i][1]
            if 0 <= nr < N and 0 <= nc < N and data[nr][nc] == data[r][c] + 1:
                Q.append((nr, nc, cnt+1))

            # 더 이상 갈 곳이 없으면 max_cnt 갱신
            else:
                if max_cnt < cnt:
                    max_cnt = cnt

    return max_cnt


import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]

    # 결과 출력하는 과정
    max_ans = 0
    answer = 0
    for r in range(N):
        for c in range(N):
            now_cnt = bfs(r, c)

            if now_cnt > max_ans:
                max_ans, answer = now_cnt, data[r][c]

            elif now_cnt == max_ans and answer > data[r][c]:
                max_ans, answer = now_cnt, data[r][c]

    print(f'#{tc}', answer, max_ans)