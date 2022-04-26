# 시간 초과 - 부분집합 조합 구하기
import sys
sys.stdin = open('input.txt')
from copy import deepcopy

# 합격 기준에 도달하는지 검사
def check(D, W, K, row_data):
    for i in range(W):
        cnt = 1
        for j in range(1, D):
            if row_data[j-1][i] == row_data[j][i]:
                cnt += 1
                if cnt == K:
                    break
            else:
                cnt = 1
        if cnt != K:
            return 0                # check에서 걸림
    return 1


def modify(D, K, nums, AB, row_data):
    for i in range(len(nums)):
        row_data[nums[i]] = [AB[i]] * W
    if check(D, W, K, row_data):
        return len(nums)

    return 0

def nCr(n, r, c, k):
    if c == r:
        new = deepcopy(comb)
        numbers.append(new)
        return

    for i in range(k, n-(r-c)+1):
        if not used[i]:
            comb[c] = d[i]
            used[i] = 1
            nCr(n, r, c+1, i+1)
            used[i] = 0



T = int(input())
for tc in range(1, T+1):
    D, W, K = map(int, input().split())
    row_data = [list(map(int, input().split())) for _ in range(D)]
    if check(D, W, K, row_data):
        print(f'#{tc}', 0)
    else:
        flag = 0
        for r in range(1, K):
            d = list(range(D))
            used = [0] * D
            comb = [0] * r
            numbers = []
            nCr(D, r, 0, 0)

            for k in range(1<<r):
                AB = []
                for j in range(r):
                    if k & 1<<j:
                        AB.append(1)
                    else:
                        AB.append(0)

                for nums in numbers:
                    new_data = deepcopy(row_data)
                    ans = modify(D, K, nums, AB, new_data)
                    if ans:
                        flag = 1
                        print(f'#{tc}', ans)
                        break

                if flag == 1:
                    break
            if flag == 1:
                break
        if flag == 0:
            print(f'#{tc}', K)




