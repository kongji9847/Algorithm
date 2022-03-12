import sys
sys.stdin = open('input.txt')

delta = [(-1, 0), (1, 0), (0, -1), (0, 1), (0, 0)]      # 상하좌우
structure = [ [], delta, [delta[0], delta[1], delta[-1]], [delta[2], delta[3], delta[-1]],
              [delta[0], delta[3], delta[-1]], [delta[1], delta[3], delta[-1]],
              [delta[1], delta[2], delta[-1]], [delta[0], delta[2], delta[-1]] ]

from collections import deque
def escaping(R, C, L):
    # start 지점 설정
    Q = deque([[R, C]])
    for i in range(1, L):
        for _ in range(len(Q)):
            vr, vc = Q.popleft()
            for element in structure[data[vr][vc]]:
                nr = vr + element[0]
                nc = vc + element[1]
                if 0 <= nr < N and 0 <= nc < M and data[nr][nc] != 0:
                    Q.append([nr, nc])

    ans = tuple(map(tuple, Q))
    answer = set(ans)
    print(len(answer))



T = int(input())
for tc in range(1, T+1):
    # 행, 열, [R, C]: 맨홀 뚜껑 위치, L: 소요시간
    N, M, R, C, L = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(N)]
    escaping(R, C, L)

