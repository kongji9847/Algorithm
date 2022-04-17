import sys
sys.stdin = open('input.txt')

delta = [(0, 0), (-1, 0), (0, 1), (1, 0), (0, -1)]

def dfs(Ar, Ac, Br, Bc, value, n):
    global max_val
    # 가지치기
    # 종료
    if n == 2:
        max_val = max(max_val, value)
        return
    # 1, 진행
    if n == 0:
        if len(data[Ar][Ac]) == 1:
            visited[data[Ar][Ac][0][0]] = 1
            dfs(Ar, Ac, Br, Bc, value+data[Ar][Ac][0][1], n+1)
        elif len(data[Ar][Ac]) == 0:
            dfs(Ar, Ac, Br, Bc, value, n+1)
        elif len(data[Ar][Ac]) > 1:
            for i in range(len(data[Ar][Ac])):
                if visited[data[Ar][Ac][i][0]] == 0:
                    visited[data[Ar][Ac][i][0]] = 1
                    dfs(Ar, Ac, Br, Bc, value + data[Ar][Ac][i][1], n+1)
                    visited[data[Ar][Ac][i][0]] = 0
                else:
                    dfs(Ar, Ac, Br, Bc, value, n + 1)
    elif n == 1:
        if len(data[Br][Bc]) == 1:
            visited[data[Br][Bc][0][0]] = 1
            dfs(Ar, Ac, Br, Bc, value+data[Br][Bc][0][1], n+1)
        elif len(data[Br][Bc]) == 0:
            dfs(Ar, Ac, Br, Bc, value, n+1)
        elif len(data[Br][Bc]) > 1:
            for i in range(len(data[Br][Bc])):
                if visited[data[Br][Bc][i][0]] == 0:
                    visited[data[Br][Bc][i][0]] = 1
                    dfs(Ar, Ac, Br, Bc, value + data[Br][Bc][i][1], n+1)
                    visited[data[Br][Bc][i][0]] = 0
                else:
                    dfs(Ar, Ac, Br, Bc, value, n + 1)



T = int(input())
for tc in range(1, T+1):
    M, A = map(int, input().split())
    data = [[[] for _ in range(10)] for _ in range(10)]
    userA = list(map(int, input().split()))
    userB = list(map(int, input().split()))
    for a in range(A):
        AP_r, AP_c, C, P = map(int, input().split())
        data[AP_c-1][AP_r-1].append((a, P))
        for n in range(1, C+1):
            for d in range(1, 5):
                nr = AP_c-1 + delta[d][0] * n
                nc = AP_r-1 + delta[d][1] * n
                if 0 <= nr < 10 and 0 <= nc < 10:
                    data[nr][nc].append((a, P))

    value = 0
    Ar, Ac = 0, 0
    Br, Bc = 9, 9
    max_val = 0
    visited = [0] * A
    dfs(Ar, Ac, Br, Bc, 0, 0)
    print(max_val)
    value += max_val
    for time in range(M):
        Ar += delta[userA[time]][0]
        Ac += delta[userA[time]][1]
        Br += delta[userB[time]][0]
        Bc += delta[userB[time]][1]
        visited = [0]*A
        max_val = 0
        dfs(Ar, Ac, Br, Bc, 0, 0)
        print(max_val)
        value += max_val
    print(data)
    print(f'#{tc}', value)