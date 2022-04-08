import sys
sys.stdin = open('input.txt')
from collections import deque

def check(K, visited):
    L = N - K
    new_visited = visited[:]
    if visited.index(0):
        start = visited.index(0)
    else:
        start = visited.index(0)
    new_visited[start] = 3
    L -= 1

    for element in graph[start]:
        if not new_visited[element] or new_visited==2:
            new_visited[element] = 3
            L -= 1
            if L == 0:
                #print(new_visited)
                return True
    if L:
        #print(new_visited)
        return False

def dfs(K, start, node_cnt, cnt):
    global min_ans
    # 종료조건
    if node_cnt == K:
        print(visited)
        if check(K, visited):
            ans = abs(cnt - (total - cnt))
            min_ans = min(ans, min_ans)
        return
    # 진행
    for element in graph[start]:
        if visited[element] == 0:
            for j in range(2):
                if j == 0:
                    visited[element] = 1
                    dfs(K, element, node_cnt+1, cnt + people_N[element-1])
                    visited[element] = 0
                elif j == 1:
                    dfs(K, start, node_cnt, cnt)



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
        dfs(K, 1, 1, people_N[0])

    if min_ans == 987654321:
        print(-1)
    else:
        print(min_ans)
