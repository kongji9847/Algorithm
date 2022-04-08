def f(i, N, s, t, rs):  # 조금 더 최적화
    global cnt
    cnt += 1
    # s: 이전까지 고려된 원소의 합
    # t: 목표합(값)
    if s == t:  # 목표값을 찾으면
        for j in range(N):
            if sel[j]:
                print(nums[j], end=' ')
        print()
    elif i == N: # 더 이상 고려할 원소가 없으면 돌아가서 다시 살펴봐!
        return
    elif s > t:  # 지금까지의 합이 이미 목표치를 넘으면? 더 고려 할 필요가 없다.
        return
    elif s + rs < t:
        return
    else:
        sel[i] = 1
        f(i+1, N, s+nums[i], t, rs-nums[i])
        sel[i] = 0
        f(i+1, N, s, t, rs-nums[i])
    return

N = 10
nums = [i for i in range(1, N+1)]
sel = [0] * N
cnt = 0      # 총 호출 횟수
t = 10
f(0, N, 0, t, sum(nums))
print(cnt)