# dfs 재귀 -> recursion error 가능한 호출 범위 초과

delta = [[-1, 0], [1, 0], [0, -1], [0, 1]]
def dfs(v):
    global ans
    stack = [v]
    r, c = stack.pop()
    if not visited[r][c]:
        visited[r][c] += 1
    for d in delta:
        nr = (r-1) + d[0]
        nc = (c-1) + d[-1]
        if 0 <= nr < N and 0 <= nc < M:
            if arr[nr][nc] == 1 and (visited[nr+1][nc+1] == 0 or visited[nr+1][nc+1] > visited[r][c] + 1):
                visited[nr+1][nc+1] = visited[r][c] + 1
                if nr == N-1 and nc == M-1:
                    ans.append(visited[nr + 1][nc + 1])
                    return
                else:
                    dfs([nr+1, nc+1])



import sys
sys.stdin = open('input.txt')

for tc in range(4):
    N, M = map(int, input().split())
    arr = [list(map(int, input())) for _ in range(N)]
    visited = [[0]*(M+1) for _ in range(N+1)]
    ans = []
    dfs([1, 1])
    print(min(ans))