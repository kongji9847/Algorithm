from collections import deque


def bfs(V):
    cnt = 0
    ans = [100]
    for r in range(1, V+1):
        for c in range(1, V+1):
            if data[r][c] == 0:
                visited = [[0] * (V+1) for _ in range(V+1)]
                min_box = 100
                Q = deque()
                for i in range(1, V+1):
                    if data[r][i] == 1:
                        visited[r][i] = 1
                        Q.append((r, i))
                while Q:
                    nr, nc = Q.popleft()
                    for j in range(1, V+1):
                        if data[nc][j] == 1 and not visited[nc][j] and j != nr:
                            visited[nc][j] = visited[nr][nc] + 1
                            Q.append((nc, j))
                            cnt += 1
                            if j == c and visited[nc][j] < min_box:
                                min_box = visited[nc][j]

                data[r][c] = min_box
    for k in range(1, V+1):
        ans.append(sum(data[k])+1)
    #     print(ans, k)
    print(cnt)

    return ans.index(min(ans))



import sys
sys.stdin = open('input.txt')
V, E = map(int, input().split())
data = [[0] * (V+1) for _ in range(V+1)]
visited = [[0] * (V+1) for _ in range(V+1)]
for _ in range(E):
    f1, f2 = map(int, input().split())
    data[f1][f2] = 1
    data[f2][f1] = 1
for v in range(1, V+1):
    data[v][v] = -1
print(bfs(V))