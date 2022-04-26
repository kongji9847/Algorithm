from copy import deepcopy
delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]
oppo = [1, 0, 3, 2]

def bacteria(M, data):
    # 3차원 arr -> 군집이 2개일 경우를 생각해 주어야 하므로
    arr = [[[] for _ in range(N)] for _ in range(N)]
    for i in range(K):
        r, c = data[i][0], data[i][1]
        # 미생물, 이동방향, 이동횟수
        arr[r][c] = [[data[i][2], data[i][3]-1, 0]]

    for i in range(1, M+1):                                             # 주어진 시간동안 모든 행과 열을 돌면서
        for r in range(N):
            for c in range(N):
                if arr[r][c]:                                           # 움직여야 할 미생물이 있으면
                    remain = []
                    for j in range(len(arr[r][c])):                     # 해당 행에 있는 모든 군집을 돌면서
                        # 1. 이미 새롭게 추가된 군집이 아니라 기존에 있었던 군집이라면
                        if arr[r][c][j][-1] < i:

                            nr = r + delta[arr[r][c][j][1]][0]          # 새로운 인덱스 가져오기
                            nc = c + delta[arr[r][c][j][1]][1]

                            if 1 <= nr <= N-2 and 1 <= nc <= N-2:       # 단순히 이동만 하는 군집이라면
                                new = deepcopy(arr[r][c][j])
                                new[-1] = i                             # 이동 횟수에 1 추가
                                arr[nr][nc].append(new)

                            elif (nr == 0 or nr == N-1 and 1 <= nc <= N-2) or (nc == 0 or nc == N-1 and 1 <= nr <= N-2):        # 벽에 도달하면 군집 수정
                                new = deepcopy(arr[r][c][j])
                                new[0] //= 2
                                new[1] = oppo[new[1]]
                                new[-1] = i
                                if new[0] != 0:
                                    arr[nr][nc].append(new)

                        # 2. 이미 움직인 군집이라면
                        else:
                            new = deepcopy(arr[r][c][j])
                            new[-1] = i
                            remain.append(new)
                    arr[r][c] = remain

        # 2개 이상이 있는 군집 찾아서 하나로 합쳐주기
        for r in range(N):
            for c in range(N):
                if len(arr[r][c]) > 1:
                    new = list(zip(*arr[r][c]))
                    indx = new[0].index(max(new[0]))
                    arr[r][c] = [[sum(new[0]), new[1][indx], new[2][0]]]

    # M시간 후 군집에 있는 미생물 수 더해주기
    answer = 0
    for r in range(N):
        for c in range(N):
            if arr[r][c]:
                answer += arr[r][c][0][0]
    return answer


import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(K)]
    print(f'#{tc}', bacteria(M, data))