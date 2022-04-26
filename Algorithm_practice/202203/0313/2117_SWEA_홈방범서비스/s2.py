# 마름모 만드는 함수
def rhombus(r, c, k, arr, N):
    # 가운데
    arr[r][c] = 1
    cnt = 1
    for i in range(1, k):           # k-1 만큼
        if 0 <= r-i < N and 0 <= c < N:
            cnt += 1
            arr[r-i][c] = 1
        if 0 <= r + i < N and 0 <= c < N:
            cnt += 1
            arr[r+i][c] = 1
        if 0 <= r < N and 0 <= c-i < N:
            cnt += 1
            arr[r][c - i] = 1
        if 0 <= r < N and 0 <= c+i < N:
            cnt += 1
            arr[r][c + i] = 1

        for j in range(1, ((k-1)-i)+1):
            if 0 <= r - j < N and 0 <= c-i < N:
                cnt += 1
                arr[r-j][c-i] = 1
            if 0 <= r + j < N and 0 <= c - i < N:
                cnt += 1
                arr[r+j][c-i] = 1

            if 0 <= r - j < N and 0 <= c+i < N:
                cnt += 1
                arr[r-j][c+i] = 1
            if 0 <= r + j < N and 0 <= c + i < N:
                cnt += 1
                arr[r+j][c+i] = 1
    print(cnt)
    return arr

data = [[0]*8 for _ in range(8)]
print(rhombus(3, 3, 3, data, 8))