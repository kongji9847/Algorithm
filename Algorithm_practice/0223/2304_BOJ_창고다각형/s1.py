import sys

sys.stdin = open('input.txt')

max_num = 0
T = int(input())
arr = [list(map(int, input().split())) for _ in range(T)]
arr.sort()
print(arr)

stack_max = [arr[0]]
stack_min = [arr[-1]]
area1 = 0
area2 = 0

for i in range(1, T):
    if arr[i][-1] >= stack_max[-1][-1]:
        area1 += (arr[i][0] - stack_max[-1][0])*stack_max[-1][-1]
        stack_max.append(arr[i])

    if arr[-1-i][-1] >= stack_min[-1][-1]:
        area2 += (stack_min[-1][0] - arr[-1-i][0]) * stack_min[-1][-1]
        stack_min.append(arr[-1-i])
print(stack_min)
print(stack_max)

if len(stack_max) > 1 and stack_max[0][-1] == stack_max[-1][-1]:
    # 지붕이 -자
    if len(stack_min) > 1 and stack_min[0][-1] == stack_min[-1][-1]:
        area = stack_max[0][-1] * (arr[-1][0] + 1 - arr[0][0])
    # 지붕이 내려가기만 한다.
    elif len(stack_min) > 1 and stack_min[0][-1] != stack_min[-1][-1]:
        area = area2 + stack_max[-1][-1]

# 지붕이 올라가기만 한다.
elif len(stack_min) > 1 and stack_min[0][-1] == stack_min[-1][-1]:
    if len(stack_max) > 1 and stack_max[0][-1] != stack_max[-1][-1]:
        area = area1 + stack_max[-1][-1]

else:
    area = area1 + area2 + stack_max[-1][-1]

print(area)
