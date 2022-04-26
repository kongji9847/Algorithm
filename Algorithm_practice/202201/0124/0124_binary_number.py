def binary(N):
    if N // 2 == 0:
        remainder = N % 2
        return str(remainder)

    else:
        remain = N % 2
        return binary(N//2) + str(remain)

print(binary(55))