def f(n, k, m):                             # 순열 p[n]을 채우는 함수, k: 배열의 크기, m 주어진 숫자 개수
    if n == k:
        print(p)
    else:
        for i in range(m):
            if used[i] == 0:
                used[i] = 1
                p[n] = a[i]
                f(n+1, k, m)
                used[i] = 0
    return

a = [1, 2, 3, 4, 5]
p = [0] * 3
used = [0] * 5
f(0, 3, 5)