import sys
sys.stdin = open('input.txt')

delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]
def search(arr):
    every = {}
    for r in range(1, N-1):
        for c in range(1, N-1):
            if arr[r][c] == 1:
                every[(r,c)] = [0, 0, 0, 0, 0]     # 상하좌우
                cnt = 0
                for d in delta:
                    pos = delta.index(d)
                    nr = r + d[0]
                    nc = c + d[1]
                    plag = 0

                    while (0 <= nr < N and 0 <= nc < N):
                        if arr[nr][nc] != 1:
                            if arr[nr][nc] == 0:
                                arr[nr][nc] = []
                            arr[nr][nc].append((r, c, pos))
                            cnt += 1
                            nr += d[0]
                            nc += d[1]
                        else:
                            plag = 1
                            break

                    if plag == 1:
                        while True:
                            nr -= d[0]
                            nc -= d[1]
                            if nr == r and nc == c:
                                break
                            else:
                                arr[nr][nc].pop()
                    else:
                        #arr[r][c] += 1                  # 가능한 경로 숫자 세기
                        every[(r, c)][pos] = cnt

    print(every)
    return arr


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    print(search(data))
    break