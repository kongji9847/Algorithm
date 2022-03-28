import sys
sys.stdin = open('input.txt')
from copy import deepcopy

#1. 특정 배열이 합격 기준에 도달하는지 검사
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

# 2. 특정 조합에서 재귀 함수를 사용해서 A or B 약물 조합 선택하기
def modify(D, K, i, row_data, r):
    global ans
    if i == r:
        if check(D, W, K, row_data):
            ans = len(nums)
        return

    row_data[nums[i]] = [0] * W
    modify(D, K, i+1, row_data, r)

    row_data[nums[i]] = [1] * W
    modify(D, K, i + 1, row_data, r)


# 3. 조합 생성하는 함수 -> 순열이 아니므로 어떤 숫자가 어디에 위치했는지는 상관없다.
# n개에서 r개를 고르는데, 현재 자리수는 c이고, k인덱스 부터 자리를 선택할 수 있다.
def nCr(n, r, c, k):
    if c == r:
        new = deepcopy(comb)
        numbers.append(new)                     # comb를 바로 append하면 추후에 comb가 수정되면 numbers 안에 있는 comb도 바뀐다.
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

    # 약물 처리 안하고 가능한 경우
    if check(D, W, K, row_data):
        print(f'#{tc}', 0)
    else:
        flag = 0
        for r in range(1, K):
            if flag == 1:
                break
            d = list(range(D))
            used = [0] * D
            comb = [0] * r
            numbers = []
            nCr(D, r, 0, 0)
            #print(numbers)

            for nums in numbers:
                ans = 0
                new_data = deepcopy(row_data)
                modify(D, K, 0, new_data, r)

                if ans:
                    flag = 1
                    print(f'#{tc}', ans)
                    break

        if flag == 0:
            print(f'#{tc}', K)
