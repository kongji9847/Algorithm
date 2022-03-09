import sys
sys.stdin = open('input.txt')

def sq(N, arr):
    area = 0
    for c in range(N):
        k = abs(c - N//2)
        for r in range(0+k, N-k):
            area += arr[r][c]

    return area

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    print(f'#{tc}', sq(N, arr))