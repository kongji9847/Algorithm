import sys
sys.stdin = open('input.txt')
from copy import deepcopy

T = int(input())
for tc in range(1, T+1):
    prices = list(map(int, input().split()))
    plan = list(map(int, input().split()))
    plan = [0] + plan + [0, 0]
    #print(plan)

    # 유리해지는 시점 파악
    # 1일과 비교
    # 1-30 / 1-90 / 30-90
    a = [prices[1]/prices[0], prices[2]/prices[0]]
    #print(a)
    #print('#########')

    from collections import deque
    hint = []
    i = 1
    while i <= 12:
        cnt = 0
        total = 0
        if plan[i]:
            cnt += 1
            total += plan[i]
        if plan[i+1]:
            cnt += 1
            total += plan[i+1]
        if plan[i+2]:
            cnt += 1
            total += plan[i+2]

        # 3개월이 가장 이득인 때
        if cnt > a[1]//a[0] and total > a[1]:
            hint.append([i, len(hint)-1+1])                 # 시작점, 인덱스
        i += 1
    print(hint)

    comb = []
    max_num = -1
    for i in range(len(hint)):
        stack = [[hint[i]]]
        while stack:
            k = stack.pop()
            if 12 in (k[-1][0], k[-1][0]+1, k[-1][0]+2) or k[-1][0]+3 > hint[-1][0]+2:

                if len(k) > max_num:
                    max_num = len(k)
                    comb = []
                    comb.append(k)

                elif len(k) == max_num:
                    comb.append(k)
                continue

            flag = 0
            for j in range(k[-1][-1]+1, len(hint)):
                if (hint[j][0] >= k[-1][0]+3):
                    stack.append(k + [hint[j]])
                    flag = 1
            if not flag:
                if len(k) > max_num:
                    max_num = len(k)
                    comb = []
                    comb.append(k)

                elif len(k) == max_num:
                    comb.append(k)
    #print(comb)

    min_price = 365*prices[-1]

    for elements in comb:
        new = deepcopy(plan)
        cnt = 0
        for element in elements:
            cnt1 = 0
            for l in range(3):
                if new[element[0] + l]:
                    if new[element[0] + l] >= a[0]:
                        cnt1 += prices[1]
                    else:
                        cnt1 += prices[0]*new[element[0] + l]
            if cnt1 < prices[2]:
                cnt += cnt1
            else:
                cnt += prices[2]
            new[element[0]], new[element[0] + 1], new[element[0] + 2] = 0, 0, 0
            if cnt > min_price:
                break
        for month in new:
            if month:
                if month >= a[0]:
                    cnt += prices[1]
                else:
                    cnt += prices[0]*month
                if cnt > min_price:
                    break
        if cnt < min_price:
            min_price = cnt
    if min_price > prices[-1]:
        min_price = prices[-1]

    print(f'#{tc}', min_price)
