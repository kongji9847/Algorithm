# 조합 생성하는 재귀함수
d = list(range(6))
used = [0] * 6
comb = [0] * 3

def nCr(n, r, c, k):
    if c == r:
        print(*comb)
        return
    for i in range(k, n-(r-c)+1):
        if not used[i]:
            comb[c] = d[i]
            used[i] = 1
            nCr(n, r, c+1, i+1)
            used[i] = 0

nCr(6, 3, 0, 0)

# 부분집합 생성하는 함수
# nums = []
# for i in range(1<<3):
#     nums = []
#     for j in range(3):
#         if i & 1<<j:
#             nums.append(1)
#         else:
#             nums.append(0)
#     print(nums)