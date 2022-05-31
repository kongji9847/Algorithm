import sys
sys.stdin = open('eval_input.txt')
input = sys.stdin.readline

# 1. 함수 정의
delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def solution(r, c):
    cnt = 1
    stack = []

    for d in range(4):
        stack.append((r, c, K-2, d))

    while stack:
        sr, sc, bomb, d = stack.pop()
        if bomb <= 0:
            continue
        rr, cc = sr + delta[d][0], sc + delta[d][1]

        if 0 <= rr < M and 0 <= cc < N:
            if bomb >= towers[rr][cc]:
                cnt += 1
                stack.append([rr, cc, bomb-2, d])

            else:
                stack.append([rr, cc, bomb//2-2, d])

    return cnt



# 0. input 받기
T = int(input())
for tc in range(1, T+1):
    M, N, K = map(int, input().split())
    towers = [list(map(int, input().split())) for _ in range(M)]
    max_tower = 0

    for r in range(M):
        for c in range(N):
            max_tower = max(max_tower, solution(r, c))

    print(f'#{tc}', max_tower)

