import sys
sys.stdin = open('input.txt')

N = int(input())
arr = list(map(int, input().split()))

# 숫자가 커질때
cnt = 1
max_len = 0
for i in range(1, N):
    if arr[i-1] <= arr[i]:
        cnt += 1
    else:                                   # 수열 흐름에서 벗어나면 최댓값인지 확인하고 갱신
        if cnt > max_len:
            max_len = cnt
        cnt = 1
if cnt > max_len:                           # 최대 길이 값 갱신
    max_len = cnt

# 숫자가 작아질 때
cnt = 1
for i in range(1, N):
    if arr[i-1] >= arr[i]:
        cnt += 1
    else:
        if cnt > max_len:
            max_len = cnt
        cnt = 1
if cnt > max_len:                           # 반복이 다 끝난 후 최대 길이 값 갱신
    max_len = cnt

print(max_len)