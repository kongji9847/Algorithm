# 퀸을 둘 때, 겹치는 행과 열은 피하고,
# 앞으로 둘 퀸의 대각선 경로가 다른 퀸과 겹치는지 확인한다.
# 퀸들의 대각선 경로를 미리 표시할 필요가 없다. -> 퀸이 추가될때 대각선에서 만나는지만 확인하면 되니까

import sys
sys.stdin = open('input.txt')

delta = [(1, 1), (-1, -1), (1, -1), (-1, 1)]
# 2. r,c에 퀸을 둘 때, 기존의 퀸과 대각선 자리가 겹치는지 확인한다.
def check(r, c):
    for d in range(4):
        nr, nc = r + delta[d][0], c + delta[d][1]
        while 0 <= nr < N and 0 <= nc < N:
            if board[nr][nc] == '*':
                return 0
            nr += delta[d][0]
            nc += delta[d][1]
    return 1


# 3. dfs로 퀸을 둘 수 있는 경우의 수 찾기
# r:는 현재 자리수, col: 현재까지 사용한 column 리스트
def dfs(r, col):
    global ans
    # 종료조건 -> 온전히 N의 자리까지 가능한 경우만 살아남는다.
    if r == N:
        ans += 1
        return
    # 진행
    for c in range(N):
        if not c in col:
            if check(r, c):
                board[r][c] = '*'
                dfs(r+1, col+[c])
                board[r][c] = 0


# 1. 입력받기
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    board = [[0] * N for _ in range(N)]
    ans = 0
    dfs(0, [])
    print(f'#{tc}', ans)