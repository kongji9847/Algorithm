from copy import deepcopy

# 2. 개수가 절반인 부분집합 구성 찾기 -> dfs 이용하기
def dfs(N):
    ans = []
    stack = [[0, [0]*N]]
    while stack:                                            # stack이 빌 때까지 반복
        v = stack.pop()                                     # stack의 마지막 요소를 뽑아서

        # 2.2 종료조건
        if v[0] == N:                                       # 모든 자리수를 확인했으면 아래 재귀 코드는 실행하지 않는다.
            continue

        # 2.1 재귀 한창 진행중
        for i in range(2):                                  # 모든 자리수는 0이거나 1
            if i == 0:                                      # 0일 때
                visited1 = deepcopy(v[1])                   # v가 2차원 배열이므로 deepcopy 필요하다.
                visited1[v[0]] = 0
                if sum(visited1) == N//2:                   # 자릿수가 이미 N//2개 존재하면 ans값에 집어넣는다.
                    ans.append(visited1)
                else:
                    stack.append([v[0]+1, visited1])        # 위 조건이 아니면, 자릿수를 up시키고, 현재 상태를 stack에 집어 넣는다.
            else:
                visited2 = deepcopy(v[1])
                visited2[v[0]] = 1
                if sum(visited2) == N//2:
                    ans.append(visited2)
                else:
                    stack.append([v[0]+1, visited2])

    return ans

#3. 음식 시너지 계산하기
from collections import deque
def cook(info):                                 # info : 위에서 받아온 부분집합 조합
    ans = deque([])
    for comb in info:                           # 조합들에서 하나의 조합을 뽑아서

        # 3.1 A 음식에 넣을 재료들의 배열 만들기 -> nC2 하기 싫어서,,,
        arr = [[0]*N for _ in range(N)]         # A 음식 조합을 저장할 배열을 만들어준다.
        for i in range(N):                      # A 음식에 넣을 재료들의 배열을 만든다.
            if comb[i] == 1:
                for j in range(N):              # 시너지 부분은 2가 된다.
                    arr[i][j] += 1
                    arr[j][i] += 1
                arr[i][i] = 0

        # 3.2 위에서 만든 배열 참고해서 시너지 계산하기
        dish = 0                                # A 음식 시너지 계산
        for r in range(N):
            for c in range(N):
                if arr[r][c] == 2:
                    dish += data[r][c]
                    dish += data[c][r]
                    arr[r][c] = 0
                    arr[c][r] = 0
        ans.append(dish)
    # 3.3 결과값 내기 -> 양쪽에서 하나씩 빼서 서로의 차이 구하기(ex) 1100 - 0011  조합: 양끝이 서로 대응된다)
    answer = []
    n = len(ans)
    for k in range(n//2):
        dish1 = ans.popleft()
        dish2 = ans.pop()
        answer.append(abs(dish1 - dish2))
    return min(answer)


#1. 입력
import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    print(f'#{tc}', cook(dfs(N)))