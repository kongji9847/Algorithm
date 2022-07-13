# dfs로 사이클 찾기
# 사이클을 만드는 모든 경우 생각해 보기 → ← ← ← : 인 경우(엣지 케이스)

import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

direction = {'N' : (-1, 0), 'S': (1, 0), 'W': (0, -1), 'E': (0, 1)}

# 0. 입력 받기
N, M = map(int, input().split())
board = [list(input().strip()) for _ in range(N)]

# 1. dfs로 사이클 찾기
ans = 0
for i in range(N):
    for j in range(M):
        if type(board[i][j]) != int:
            ans += 1
            route = [(i + direction[board[i][j]][0], j + direction[board[i][j]][1])]
            history = [(i, j)]
            board[i][j] = ans

            while route:
                ni, nj = route.pop()
                if type(board[ni][nj]) != int:
                    route.append((ni + direction[board[ni][nj]][0], nj + direction[board[ni][nj]][1]))
                    history.append((ni, nj))
                    board[ni][nj] = ans

                # 사이클을 만났을 때
                else:
                    if board[ni][nj] < ans:                 # 현재 만들고 있는 사이클이 아닐 때 -> 현재 갱신한 사이클 다시 복귀
                        ans -= 1
                        while history:
                            ii, jj = history.pop()
                            board[ii][jj] = ans
                    else:                                   # 현재 만들고 있는 사이클이 종료
                        break

# 2. 답 내기
print(ans)