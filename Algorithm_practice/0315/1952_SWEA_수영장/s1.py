# dp 사용하기
import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T+1):
    prices = list(map(int, input().split()))
    plan = list(map(int, input().split()))
    plan = [0] + plan

    # 한 달을 단위로 1일 이용권, 한 달 이용권 중 이득인 것을 costs에 각 달 별로 저장해준다.
    costs = [0]*13
    for i in range(1, 13):
        costs[i] = min(prices[0] * plan[i], prices[1])

    costs[2] += costs[1]
    for j in range(3, 13):
        costs[j] = min(costs[j-1] + costs[j], costs[j-3] + prices[2])

    if costs[-1] > prices[-1]:
        ans = prices[-1]
    else:
        ans = costs[-1]
    print(costs)
    print(f'#{tc}', ans)



