import sys
sys.stdin = open('input.txt')

delta = [(1, 1), (-1, -1), (1, -1), (-1, 1)]

# 2. 현재 상태에서 r, c에 퀸을 두어도 되는지 확인하는 함수
def check(r, c):
    for i in range(N):
        if board[r][i] == '*' or board[i][c] == '*':
            return 0
    for d in range(4):
        nr, nc = r + delta[d][0], c + delta[d][1]
        while 0 <= nr < N and 0 <= nc < N:
            if board[nr][nc] == '*':
                return 0
            nr += delta[d][0]
            nc += delta[d][1]
    return 1


# 3. r, c에 퀸을 놓고 방문 표시하기
def Queen(r, c):
    board[r][c] = '*'
    for i in range(N):
        if i != c:
            board[r][i] += 1
    for j in range(N):
        if j != r:
            board[j][c] += 1
    for d in range(4):
        nr, nc = r + delta[d][0], c + delta[d][1]
        while 0 <= nr < N and 0 <= nc < N:
            board[nr][nc] += 1
            nr += delta[d][0]
            nc += delta[d][1]

# 4. r, c에 퀸 지우고 방문 표시 지우기
def remove_Queen(r, c):
    board[r][c] = 0
    for i in range(N):
        if i != c:
            board[r][i] -= 1
    for j in range(N):
        if j != r:
            board[j][c] -= 1
    for d in range(4):
        nr, nc = r + delta[d][0], c + delta[d][1]
        while 0 <= nr < N and 0 <= nc < N:
            board[nr][nc] -= 1
            nr += delta[d][0]
            nc += delta[d][1]

# dfs로 퀸을 둘 수 있는 경우의 수 찾기
def dfs(i):
    global ans
    # 종료조건 -> 온전히 N의 자리까지 가능한 경우만 살아남는다.
    if i == N:
        ans += 1
        return
    # 진행
    for j in range(N):
        if board[i][j] == 0 and check(i, j):
            Queen(i, j)
            dfs(i+1)
            remove_Queen(i, j)

# 1. 입력받기
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    board = [[0] * N for _ in range(N)]
    ans = 0
    dfs(0)
    print(f'#{tc}', ans)