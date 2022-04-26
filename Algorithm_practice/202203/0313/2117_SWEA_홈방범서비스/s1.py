#2. 해당 인덱스가 있는지 확인하고 인덱스에 해당하는 수를 반환해주는 함수
def check(r, c, N):
    if 0 <= r < N and 0 <= c < N:
        return arr[r][c]
    return 0

# 3. 마름모의 중심을 선택해서 마름모 범위 안의 집의 개수를 세어준다.
# k가 N+1일 때는 전체 범위를 감쌀 수 있다.
def security(N, M):
    ans = 0
    for k in range(N+1, 1, -1):                             # k가 1일 때는 집들을 굳이 다 볼 필요가 없다.
        cost = k*k + (k-1)*(k-1)
        if cost > total*M:
            continue
        for r in range(N):
            for c in range(N):
                cnt = 0
                cnt += arr[r][c]
                for i in range(1, k):
                    cnt += check(r - i, c, N)
                    cnt += check(r + i, c, N)
                    cnt += check(r, c - i, N)
                    cnt += check(r, c + i, N)

                    for j in range(1, (k - 1) - i+1):
                        cnt += check(r - j, c - i, N)
                        cnt += check(r + j, c - i, N)
                        cnt += check(r - j, c + i, N)
                        cnt += check(r + j, c + i, N)

                if M * cnt - cost >= 0 and cnt > ans:
                    ans = cnt

    if ans != 0:
        return ans
    else:                               # k가 1일 때는 집 1개만 할 수 있다.
        return 1


# 1. input 받기
import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    total = 0
    for l in range(N):
        total += sum(arr[l])
    print(f'#{tc}', security(N, M))