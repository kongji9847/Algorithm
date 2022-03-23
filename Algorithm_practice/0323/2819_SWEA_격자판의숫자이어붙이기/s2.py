delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]
def dfs(sr, sc):
    cnt = 0
    stack = [(sr, sc, str(data[sr][sc]))]
    while stack:
        (r, c, ans) = stack.pop()
        if len(ans) == 7:
            answer.add(ans)
            continue

        for i in range(4):
            nr = r + delta[i][0]
            nc = c + delta[i][1]
            if 0 <= nr < 4 and 0 <= nc < 4:
                stack.append((nr, nc, ans + str(data[nr][nc])))
                cnt += 1

    print(cnt)


import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    data = [list(map(int, input().split())) for _ in range(4)]
    answer = set()
    for r in range(4):
        for c in range(4):
            dfs(r, c)
    print(f'#{tc}', len(answer))
