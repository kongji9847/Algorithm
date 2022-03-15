import sys
sys.stdin = open('input.txt')
from copy import deepcopy

T = int(input())
for tc in range(1, T+1):
    prices = list(map(int, input().split()))
    plan = list(map(int, input().split()))
    plan = [0] + plan + [0, 0]

    hint = []
    i = 1
    while i <= 10:
        cnt = 0
        for n in range(3):
            if plan[i+n]:
                if plan[i+n]*prices[0] > prices[1]:
                    cnt += prices[1]
                else:
                    cnt += prices[0]*plan[i+n]
        # 3개월이 가장 이득인 때
        if cnt > prices[2]:
            hint.append([i, len(hint)-1+1])                 # 시작점, 인덱스
        i += 1
    # print(hint)
    # 3개월이 가장 이득인데, 이득인게 많으면 좋은거 아냐.....?????? 왜????????? 뭐가 문제지??????

    comb = []
    max_num = -1
    for i in range(len(hint)):
        stack = [[hint[i]]]
        while stack:
            k = stack.pop()
            if 12 in (k[-1][0], k[-1][0] + 1, k[-1][0] + 2) or k[-1][0] + 3 > hint[-1][0] + 2:
                comb.append(k)
                continue

            flag = 0
            for j in range(k[-1][-1] + 1, len(hint)):
                if (hint[j][0] >= k[-1][0] + 3):
                    stack.append(k + [hint[j]])
                    flag = 1
            comb.append(k)
    #print(comb)

    min_price = 0
    for month in plan:
        if month:
            if month*prices[0] > prices[1]:
                min_price += prices[1]
            else:
                min_price += prices[0] * month

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