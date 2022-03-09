from collections import deque


# 최단 거리 찾기와 원리 동일
# r ~ c : ( [r, c1], [c2, c3], [c3, c] )
# visited 마킹 시, 양방향을 모두 마킹해 불필요한 왕복을 하지 않는다.

def bfs(V):
    ans = [100]  # 0부터 인덱스 시작 맞춰주려고
    for r in range(1, V + 1):
        for c in range(r + 1, V + 1):  # 양방향 연결이므로 f(i, j) == f(j, i) -> 최초만 보면 된다.
            if data[r][c] == 0:  # r에서 c까지 가는 최단 거리 구하기
                visited = [[0] * (V + 1) for _ in range(V + 1)]  # 방문 기록 초기화
                min_box = 100  # 가능한 최대값은 100이다.
                Q = deque()  # FIFO 구조 사용 준비

                for i in range(1, V + 1):  # 연결의 시작점 찾기 -> r에서부터 시작할
                    if data[r][i] == 1:
                        visited[r][i] = 1  # 양방향에 방문 표시하기
                        visited[i][r] = 1
                        Q.append((r, i))
                while Q:  # Q 안의 요소가 전부 없어질 때까지 반복
                    nr, nc = Q.popleft()  # 부모 요소
                    for j in range(1, V + 1):  # 연결된 자식 요소 찾아 다니기
                        if data[nc][j] == 1 and not visited[nc][j]:  # 연결 + 방문한 적 없으면 조건 부합
                            visited[nc][j] = visited[nr][nc] + 1  # 부모 요소에서 한단계 더 나아갔으므로 표시하기
                            visited[j][nc] = visited[nr][nc] + 1
                            Q.append((nc, j))
                            if j == c and visited[nc][j] < min_box:
                                min_box = visited[nc][j]

                data[r][c] = min_box
                data[c][r] = min_box
    for k in range(1, V + 1):
        ans.append(sum(data[k]) + 1)
    #     print(ans, k)
    return ans.index(min(ans))


import sys

sys.stdin = open('input.txt')

V, E = map(int, input().split())
data = [[0] * (V + 1) for _ in range(V + 1)]
visited = [[0] * (V + 1) for _ in range(V + 1)]
for _ in range(E):
    f1, f2 = map(int, input().split())
    data[f1][f2] = 1
    data[f2][f1] = 1
for v in range(1, V + 1):
    data[v][v] = -1  # 대각 성분 구별하기
print(bfs(V))