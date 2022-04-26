# dp 사용하기 -> 1칸 혹은 2칸씩 오를 수 있는 계단의 모든 방법의 수와 비슷한 느낌
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

    # 각 인덱스에 해당하는 달까지의 최소 비용 구하기 -> if 4라면 1~4월까지 누적 최소 비용
    # 이때, 3개월치 이용권 고려 -> 계단을 3칸 올라가는 경우
    # 한달 이용권 단위로 사용했을 때, or 3개월 이용권 단위 중 최소의 결과를 선택해 해당 지점에서의 최솟값 구하기
    # 인덱스가 12일 때는, 12월까지의 누적 최소 비용이 구해진다.
    costs[2] += costs[1]
    for j in range(3, 13):
        costs[j] = min(costs[j-1] + costs[j], costs[j-3] + prices[2])

    # 1년치 이용권과 12월 비교
    if costs[-1] > prices[-1]:
        ans = prices[-1]
    else:
        ans = costs[-1]

    #print(costs)
    print(f'#{tc}', ans)



