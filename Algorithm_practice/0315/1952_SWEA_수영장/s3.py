import sys
sys.stdin = open('input.txt')
from copy import deepcopy

T = int(input())
for tc in range(1, T+1):
    prices = list(map(int, input().split()))
    plan = list(map(int, input().split()))
    plan = [0] + plan

    # 3개월 이용권을 쓰며 시작하는 것이 가장 이득인 달 목록 구하기
    hint = []
    i = 1
    while i <= 10:                                                  # 최소 비용일 때, 3개월 이용권이 11이나 12월에 쓰이는 경우는 굳이 없다.
        cnt = 0
        # 각 달에서 한달 또는 일일 이용권을 혼합한 조합으로 사용했을 때의 최소 비용 구하기
        for n in range(3):
            if plan[i+n]:
                if plan[i+n]*prices[0] > prices[1]:
                    cnt += prices[1]
                else:
                    cnt += prices[0]*plan[i+n]

        # 3개월이 가장 이득인 때
        if cnt > prices[2]:
            hint.append([i, len(hint)-1+1])                 # 시작점, 인덱스 -> 뒤에서 다시 앞으로 돌아오는 것을 막기 위해
        i += 1

    # 3개월 이용권을 사용하는 것이 가장 이득인 달의 목록에서 최대한 달이 많은 조합을 뽑자(단, 달이 겹치지 않게) -> dfs 사용
    comb =[]
    max_num = -1
    for i in range(len(hint)):
        stack = [[hint[i]]]
        while stack:
            k = stack.pop()
            if 12 in (k[-1][0], k[-1][0] + 1, k[-1][0] + 2) or k[-1][0] + 3 > hint[-1][0] + 2:              # 12월이 포함된 3개월을 가진 달이거나, 더이상 진행할 곳이 없을 때 현재 조합을 저장
                if max_num < len(k):
                    max_num = len(k)
                    comb = []
                    comb.append(k)
                elif max_num == len(k):
                    comb.append(k)
                continue

            for j in range(k[-1][-1] + 1, len(hint)):                  # 앞으로 다시 돌아와 보는 것을 방지
                if (hint[j][0] >= k[-1][0] + 3):                        # 겹치는 달이 없게
                    stack.append(k + [hint[j]])

            if max_num < len(k):
                max_num = len(k)
                comb = []
                comb.append(k)                                          # 종료조건에 해당하지는 않지만 짧게 끝나는 조합
            elif max_num == len(k):
                comb.append(k)

    # 한달 단위로 최소 비용 구하기
    min_price = 0
    for month in plan:
        if month:
            if month*prices[0] > prices[1]:
                min_price += prices[1]
            else:
                min_price += prices[0] * month

    # 가능한 3개월 조합에서 가장 최소 비용 찾기
    for elements in comb:
        new = deepcopy(plan)
        cnt = 0
        for element in elements:
            cnt += prices[2]
            new[element[0]], new[element[0] + 1], new[element[0] + 2] = 0, 0, 0
            if cnt > min_price:
                break
        for month in new:
            if month:
                if month * prices[0] >= prices[1]:
                    cnt += prices[1]
                else:
                    cnt += prices[0] * month
                if cnt > min_price:
                    break
        if cnt < min_price:
            min_price = cnt

    # 1년 가격과 비교
    if min_price > prices[-1]:
        min_price = prices[-1]

    print(f'#{tc}', min_price)