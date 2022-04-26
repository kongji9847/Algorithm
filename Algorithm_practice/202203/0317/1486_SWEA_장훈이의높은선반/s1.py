# dfs로 부분집합의 합 구하기 -> stack 사용
from copy import deepcopy
def dfs(N, B):
    total = sum(data)
    ans = []
    # visited = [현재 자리 위치, 1~N, 현재 누적합]
    visited = [0] * (N+2)
    stack = [visited]

    while stack:
        v = stack.pop()

        # 현재 누적합에 다음 자릿수를 모두 더해도 B보다 작으면 유망하지 않으므로 다음 반복문으로 넘어가기
        num = sum(data[:v[0]])
        if v[-1] + (total - num) < B:
            continue

        # 현재 누적합에 다음 자릿수를 모두 더했을 때, B와 같으면 바로 0 return
        elif v[-1] + (total - num) == B:
            return 0

        # 종료 조건 - 모든 자리수가 채워지자 마자 ans에 append 한다. -> stack에 N 이상의 자리수가 쌓이지 못한다.
        if v[0] == N:
            ans.append(v[-1])
            continue

        # 자리수 늘려 주기
        v[0] += 1
        for i in range(2):
            if i == 0:
                new = deepcopy(v)
                new[v[0]] = 1
                new[-1] += data[v[0]-1]
                stack.append(new)
                # 현재 누적합이 B이 되면 바로 0 리턴
                if new[-1] == B:
                    return 0
            else:
                new = deepcopy(v)
                stack.append(new)
                if new[-1] == B:
                    return 0

    return min(ans) - B


import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, B = map(int, input().split())
    data = list(map(int, input().split()))
    print(f'#{tc}', dfs(N, B))