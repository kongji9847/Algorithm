import sys
sys.stdin = open('input.txt')
from collections import deque

def check(K, visited):
    L = N - K
    new_visited = visited[:]
    start = visited.index(0)
    new_visited[start] = 2
    L -= 1

    for element in graph[start]:
        if not new_visited[element]:
            new_visited[element] = 2
            L -= 1
            if L == 0:
                print(new_visited)
                return True
    if L:
        print(new_visited)
        return False



# def dfs(K, i, node_cnt, cnt):
#     global min_ans
#     # 종료조건
#     if node_cnt == K:
#         print(visited)
#         if check(K, visited):
#             ans = abs(cnt - (total - cnt))
#             min_ans = min(ans, min_ans)
#         return
#     # 진행
#     for element in graph[i]:
#         if not visited[element]:
#             visited[element] = 1
#             dfs(K, element, node_cnt+1, cnt + people_N[element-1])
#             visited[element] = 0

def bfs(K, visited):
    global min_ans
    Q = deque([ (1, 1, people_N[0], visited) ])

    while Q:
        start, node_cnt, cnt, new_visited = Q.popleft()

        if node_cnt == K:
            if check(K, new_visited):
                ans = abs(cnt - (total - cnt))
                min_ans = min(ans, min_ans)
                continue

        for element in graph[start]:
            if not new_visited[element]:
                new = new_visited[:]
                new[element] = 1
                Q.append((element, node_cnt+1, cnt+people_N[element], new))



T = int(input())
for tc in range(1, T+1):
    N = int(input())
    people_N = list(map(int, input().split()))
    total = sum(people_N)

    graph = [[]*(N+1) for _ in range(N+1)]
    for i in range(1, N+1):
        M, *adj = map(int, input().split())
        for element in adj:
            graph[i].append(element)

    min_ans = 987654321
    for K in range(1, N):
        visited = [0]*(N+1)
        visited[0] = 1
        visited[1] = 1
        bfs(K, visited)

    if min_ans == 987654321:
        print(-1)
    else:
        print(min_ans)
