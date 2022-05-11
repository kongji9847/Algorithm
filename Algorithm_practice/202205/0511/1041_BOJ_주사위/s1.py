# A B C D E F => (A, F) (B, E) (C, D)
# counter = [5, 4, 3, 2, 1, 0]

# 주사위 그려보면서 최소값을 가진 면이 필요한 개수를 구하기 -> 2면이 필요할 때, 3면이 필요할 때
# 맞은 편 면만 아니면 모두 인접하다.

import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline


# T = int(input())
# for tc in range(1, T+1):
N = int(input())
data = list(map(int, input().split()))
dice = []
for i in range(6):
    dice.append((data[i], i))

sorted_data = sorted(dice)
# 가장 작은 면
first_indx = sorted_data[0][1]
first_val = data[first_indx]

# 2번째로 작고 가장 작은 면과 인접한 면
second = 1
if sorted_data[second][1] + first_indx == 5:
    second += 1
second_indx = sorted_data[second][1]
second_val = data[second_indx]

# 3번째로 작고 위의 두 면과 인접한 면 -> 두 면과 맞은 편만 아니면 된다.
third = second + 1
if sorted_data[third][1] + first_indx == 5 or sorted_data[third][1] + second_indx==5:
    third += 1
third_indx = sorted_data[third][1]
third_val = data[third_indx]

# 주사위를 1개만 쌓을 때는 N-2 연산이 안된다.
if N == 1:
    total = sum(data) - max(data)
    print(total)

else:
    total = (first_val + second_val + third_val) * 4 \
            + (first_val + second_val)*((N-2)*4 + (N-1)*4) \
            + first_val * ((N-2)*(N-1)*4 + (N-2)**2)
    print(total)
