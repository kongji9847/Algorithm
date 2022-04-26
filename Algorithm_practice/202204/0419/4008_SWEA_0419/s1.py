import sys
sys.stdin = open('input.txt')

# dfs 사용
def solution(n, value):
    global min_val
    global max_val
    # 종료조건
    if n == N-1:
        min_val = min(min_val, value)
        max_val = max(max_val, value)
        return

    # 진행
    for operator_indx in range(4):
        if operators[operator_indx]:
            if operator_indx == 0:
                new_value = value + nums[n+1]
            elif operator_indx == 1:
                new_value = value - nums[n+1]
            elif operator_indx == 2:
                new_value = value * nums[n+1]
            else:
                new_value = int(value / nums[n+1])

            if -100000000 <= new_value <= 100000000:
                operators[operator_indx] -= 1
                solution(n+1, new_value)
                operators[operator_indx] += 1


# 입력받기
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    operators = list(map(int, input().split()))
    nums = list(map(int, input().split()))
    max_val = -100000001
    min_val = 100000001
    solution(0, nums[0])
    print(f'#{tc}', max_val-min_val)
