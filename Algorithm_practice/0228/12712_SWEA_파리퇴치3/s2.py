import sys
sys.stdin = open('input.txt')

# 합치기
delta = [[0, -1], [1, 0], [0, 1], [-1, 0], [-1, -1], [1, 1], [-1, 1], [1, -1]]
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_sum = 0
    for r in range(N):
        for c in range(N):                                              # 중심값 정하기

            total = arr[r][c]                                           # 중심값 더하기
            total2 = arr[r][c]
            for i in range(4):                                          # 상하좌우 방향 돌기
                for size in range(1, M):                                # 중심에서 떨어진 크기를 점차 키우며 더해주기
                    nr = r + delta[i][0]*size
                    nc = c + delta[i][1]*size
                    if 0 <= nr <= N-1 and 0 <= nc <= N-1:               # 인덱스 에러 방지
                        total += arr[nr][nc]

                    nnr = r + delta[4 + i][0] * size
                    nnc = c + delta[4 + i][1] * size
                    if 0 <= nnr <= N - 1 and 0 <= nnc <= N - 1:  # 인덱스 에러 방지
                        total2 += arr[nnr][nnc]

            if total > max_sum and total > total2:                                         # 한 기준값의 합을 다 더하면 초기화 해주기
                max_sum = total
            elif total2 > total and total2 > max_sum:
                max_sum = total2


    print(f'#{tc}', max_sum)
