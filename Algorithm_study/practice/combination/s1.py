def nCr(n, r, s):       # n개에서 r개를 고르는 조합, s는 선택할 수 있는 구간의 시작
    if r == 0:
        print(*comb)
    else:
        for i in range(s, n-r+1):
            comb[3-r] = A[i]
            nCr(n, r-1, i+1)

n = 5
r = 3
comb = [0]*3
A = [1, 2, 3, 4, 5]
nCr(n, r, 0)