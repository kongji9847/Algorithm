# 부분집합의 조합 구하기와 동일 -> 포함여부로 가지치기
import sys
sys.stdin = open('input.txt')
from copy import deepcopy

# 3. honey[r][c:c+M]에서의 최대 이익을 얻을 수 있는 조합 구하기(부분집합)
def dfs(now, money, total):
    global best
    # 가지치기 -> C보다 total이 크다면 유망하지 않은 것
    if total > C:
        return

    # 종료 조건 + 최댓값 갱신
    if now == c+M:
        best = max(best, money)
        return

    # 진행: 포함O / 포함 X
    dfs(now+1, money+(honey[r][now])**2, total + honey[r][now])
    dfs(now+1, money, total)




# 1. input 받기
T = int(input())
for tc in range(1, T + 1):
    N, M, C = map(int, input().split())
    honey = [list(map(int, input().split())) for _ in range(N)]

    # 2. honey[r][c:c+M]에서의 최대 이익 구하기
    work = []
    for r in range(N):
        for c in range(N-M+1):
            new = deepcopy(honey[r][c:c + M])
            new.sort()
            best = 0
            dfs(c, 0, 0)
            # 수익, 행, 열 -> 추후 두개를 고를 때 겹치는 부분이 없어야 하므로
            work.append((best, r, c))

    # 4. 답 결정하기
    work.sort(reverse=True)                         # 내림차순으로 나열
    max_num = work[0]                               # 가장 큰 이익은 musthave
    for i in range(1, len(work)):                   # 그 다음 이익 결정하기
        if work[i][1] != max_num[1]:                # 행이 겹치지 않으면 바로 가능
            ans = work[i][0] + max_num[0]
            print(f'#{tc}', ans)
            break
        else:                                       # 행이 겹치면 열에서 겹치는 부분이 없어야 한다.
            if abs(work[i][2] - max_num[2]) >= M:
                ans = work[i][0] + max_num[0]
                print(f'#{tc}', ans)
                break

