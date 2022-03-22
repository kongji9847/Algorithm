# cctv가 없을 때도 고려해주기 -> 런타임 에러
from copy import deepcopy
from collections import deque
# 0은 빈 칸, 6은 벽, 1~5는 CCTV를 나타내고, 문제에서 설명한 CCTV의 종류이다.
delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]      # 상하좌우
CCTV = {1 : [(0), (1), (2), (3)],
        2 : [(0, 1), (2, 3)],
        3 : [(0, 2), (0, 3), (1, 2), (1, 3)],
        4 : [(0, 2, 3), (1, 2, 3), (2, 0, 1), (3, 0, 1)],
        5 : [(0, 1, 2, 3)]}

def monitor(data):
    ans = []
    cctvs = []
    for r in range(N):
        for c in range(M):
            if data[r][c] != 0 and data[r][c] != 6:
                cctvs.append((r, c, data[r][c]))

    if cctvs:
        Q = deque([ [cctvs[0], data, 0] ])
        while Q:
            [(sr, sc, indx), arr, k] = Q.popleft()

            for i in range(len(CCTV[indx])):
                new_arr = deepcopy(arr)

                if indx == 1:
                    going(sr, sc, CCTV[indx][i], new_arr)

                else:
                    for j in range(len(CCTV[indx][0])):
                        going(sr, sc, CCTV[indx][i][j], new_arr)


                if k == len(cctvs) - 1:
                    ans.append(new_arr)

                elif k+1 < len(cctvs):
                    Q.append([cctvs[k+1], new_arr, k+1])

        answer = []
        for info in ans:
            cnt = 0
            for r in range(N):
                for c in range(M):
                    if info[r][c] == 0:
                        cnt += 1
            answer.append(cnt)

    else:
        cnt = 0
        for r in range(N):
            for c in range(M):
                if data[r][c] != 6:
                    cnt += 1
        return cnt

    return min(answer)



# 시작지점, 방향, data
def going(sr, sc, d, data):
    nr, nc = sr + delta[d][0], sc + delta[d][1]
    while 0 <= nr < N and 0 <= nc < M:
        if data[nr][nc] == 0:
            data[nr][nc] = '#'

        elif data[nr][nc] == 6:
            break
        nr += delta[d][0]
        nc += delta[d][1]



import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    # N: 행의 수, M:열의 수
    N, M = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(N)]
    print(monitor(data))