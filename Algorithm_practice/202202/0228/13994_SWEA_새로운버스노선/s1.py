import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())                    # 노선 수
    arr = [list(map(int, input().split())) for _ in range(N)]

    stops = [0] * (1000+1)
    for i in range(N):
        if arr[i][0] == 1:          # 일반
            for j in range(arr[i][1], arr[i][2]+1):
                stops[j] += 1

        elif arr[i][0] == 2:        # 급행
            stops[arr[i][1]] += 1
            stops[arr[i][2]] += 1

            for j in range(arr[i][1]+2, arr[i][2], 2):
                stops[j] += 1


        else:                       # 광역
            stops[arr[i][1]] += 1
            stops[arr[i][2]] += 1
            if not arr[i][1] % 2:
                for j in range(arr[i][1]+1, arr[i][2]):
                    if not j % 4:
                        stops[j] += 1
            else:
                for j in range(arr[i][1] + 1, arr[i][2]):
                    if j % 3 == 0 and j % 10 != 0:
                        stops[j] += 1

    print(f'#{tc}', max(stops))

