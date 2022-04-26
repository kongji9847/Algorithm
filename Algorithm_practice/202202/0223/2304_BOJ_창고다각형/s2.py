# 처음에 풀 때 오름차순으로 정렬한 블록과 내림차순으로 정렬한 블록들의 중복을 고려하지 않았다 → set 을 활용해 없애 주었다.

import sys
sys.stdin = open('input.txt')

T = int(input())
arr = [tuple(map(int, input().split())) for _ in range(T)]                  # set을 사용하므로 리스트 대신 tuple로 만들기 -> hashable 한 것은 set으로 처리할 수 없다.
arr.sort()                                                                  # 위치 순서대로 정렬

goup = [arr[0]]
godown = [arr[-1]]

for i in range(1, T):
    if arr[i][-1] >= goup[-1][-1]:                                          # 오른쪽으로 갈 수록 벽의 높이가 커지는 블록만 담기 -> 맨 끝에는 가장 높은 벽이 담아진다.
        goup.append(arr[i])
    if arr[T-1-i][-1] >= godown[-1][-1]:                                    # 왼쪽으로 갈 수록 벽의 높이가 높아지는 블록만 담기 -> 맨 끝에는 가장 높은 벽이 담아진다.
        godown.append(arr[T-1-i])

every = list(set(goup + godown))                                            # set 사용해서 중복된 블록 버리기
every.sort()
# print(every)

area = goup[-1][-1]                                                         # 가장 높이 솟은 블록 한 개 넓이 구해주기
for j in range(1, len(every)):                                              # 오른쪽으로 돌면서 가장 높이 솟은 블록까지 면적 더해주기
    if every[j][0] <= goup[-1][0]:
        area += every[j-1][-1] * (every[j][0] - every[j-1][0])
    elif every[j][0] > goup[-1][0]:                                         # 가장 높이 솟은 블록 이후의 블록들 면적 더해주기
        area += every[j][-1] * (every[j][0] - every[j-1][0])
print(area)