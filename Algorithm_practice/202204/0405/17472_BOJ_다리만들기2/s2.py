import sys
# sys.stdin = open('input.txt')
from collections import deque

# 섬을 구분하기
delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]
def island(data):
    cnt = 1
    for r in range(N):
        for c in range(M):
            if data[r][c] == 1:
                cnt += 1
                Q = deque([(r, c)])
                data[r][c] = cnt
                while Q:
                    sr, sc = Q.popleft()
                    for d in range(4):
                        nr = sr + delta[d][0]
                        nc = sc + delta[d][1]
                        if 0 <= nr < N and 0 <= nc < M and data[nr][nc] == 1:
                            data[nr][nc] = cnt
                            Q.append((nr, nc))
    return cnt

# 다리를 놓을 수 있는 최소 길이
def solution(data, N, M):
    for r in range(N):
        start = -1
        for c in range(M):
            if data[r][c] != 0 and start == -1:
                start = data[r][c]
                start_indx = c
            elif start != -1 and data[r][c] == start:
                start_indx = c
            elif data[r][c] != 0 and start != -1 and data[r][c] != start:
                end = data[r][c]
                if c - start_indx - 1 > 1 and graph[start][end] > c - start_indx - 1:
                    graph[start][end] = c - start_indx - 1
                    graph[end][start] = c - start_indx - 1
                start = data[r][c]
                start_indx = c

def find_set(x):
    while x != keys[x]:
        x = keys[x]
    return x

def make_union(x, y):
    keys[find_set(y)] = find_set(x)


def kruskal():
    ans = 0
    edge_cnt = 0
    now_indx = 0
    while len(edges):                               # edges가 0개인 경우도 있으므로
        w, n1, n2 = edges[now_indx]
        if find_set(n1) != find_set(n2):
            ans += w
            edge_cnt += 1
            make_union(n1, n2)
        now_indx += 1
        if edge_cnt == island_cnt - 2:              # 간선의 개수 = 노드의 개수 - 1
            return ans
        elif now_indx == len(edges):
            return -1
    return -1                                       # 0개인 경우 바로 -1 출력


# T = int(input())
# for tc in range(1, T+1):
N, M = map(int, sys.stdin.readline().split())
data = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
island_cnt = island(data)
col_data = list(zip(*data))

graph = [[987654321]*(island_cnt+1) for _ in range(island_cnt+1)]
solution(data, N, M)
solution(col_data, M, N)

edges = []
for i in range(2, island_cnt+1):
    for j in range(2, island_cnt+1):
        if graph[i][j] != 987654321:
            edges.append([graph[i][j], i, j])
edges.sort()
keys = list(range(island_cnt+1))
print(kruskal())
