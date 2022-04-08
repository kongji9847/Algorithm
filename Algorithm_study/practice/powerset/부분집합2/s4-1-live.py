def f(i, N, K):
    global cnt
    cnt += 1
    if i == N: # 한 개의 부분집합 완성
        s = 0
        for j in range(N):
            if sel[j]:
                s += nums[j]

        if s == K: # 찾는 합이면
            for j in range(N):
                if sel[j]:
                    print(nums[j], end=' ')
            print()
    else:
        sel[i] = 1
        f(i+1, N, K)
        sel[i] = 0
        f(i+1, N, K)
    return

N = 10
nums = [i for i in range(1, N+1)]
sel = [0] * N
cnt = 0      # 총 호출 횟수
f(0, N, 10)
print(cnt)