#3. 한 턴씩 함수 호출해서 board 변경해주기
# 8방향 확인하기
delta = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
def othello(c, r, who):                                                         # c: 열, r: 행
    board[r-1][c-1] = who
    for i in range(8):
        nr, nc = (r-1), (c-1)
        cnt = 0
        flag = 0
        # 특정 방향으로 직진했을 때, 자신의 돌이 있는지 확인한다.
        while True:
            nr += delta[i][0]
            nc += delta[i][1]
            cnt += 1
            if 0 <= nr < N and 0 <= nc < N:
                if board[nr][nc] == who:                            # 돌이 있다면 현재 반복문 종료하고 다음 반복문으로 넘어가기
                    flag = 1
                    break
                elif board[nr][nc] == 0:
                    break
            else:
                break
        if flag:                                                    # 조건에 부합하면 돌 바꿔주기
            for j in range(1, cnt):
                rr = nr - delta[i][0]*j
                rc = nc - delta[i][1] * j
                board[rr][rc] = who


import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    #1. 초기 세팅
    board = [[0]*N for _ in range(N)]
    board[N//2-1][N//2-1] = 2
    board[N//2][N//2] = 2
    board[N // 2 - 1][N // 2] = 1
    board[N // 2][N // 2 - 1] = 1
    #2. 게임 시작
    for turn in range(M):
        c, r, who = map(int, input().split())
        othello(c, r, who)

    # 4. 결과 내기
    ans = {'black':0, 'white':0}
    for r in range(N):
        for c in range(N):
            if board[r][c] == 1:
                ans['black'] += 1
            elif board[r][c] == 2:
                ans['white'] += 1
    print(f'#{tc}', ans['black'], ans['white'])
