'''
greedy 접근 NO -> 현재의 최단 거리가 다음 단계에서도 최단 루트가 아님
뒤집자 -> 현재 단계(N)에서 각 라인(K)에 멈췄을 때 해당하는 누적 시간 구하기 -> top down이 아니라 bottom up!

total = [1, 2, 3, 1, 2]
now = [1, 1, 2, 2, 4]

new_total = now + min(min(total)+이동비용, total[동일 라인])
'''

import sys
input = sys.stdin.readline

# K: 라인수(열의 개수), N: 작업장 수(행의 개수)
K, N = map(int, input().split())

# 1단계 작업은 직접 input 받고, 바로 누적 값으로 반영하기
pre = list(map(int, input().split()))
total = pre[:K]

# 2단계 작업부터 N단계 작업까지 반복해서 input 받으며 누적 시간 갱신
for i in range(1, N):
    now = list(map(int, input().split()))           # 현재 단계의 각 k개의 라인이 작업하는 시간
    min_total = min(total)                          # 누적 값 중 가장 작은 값 -> 시간 복잡도: O(n) -> 아래 중첩된 for문에서 받으면 시간 초과남

    new_total = [0] * K                             # 새로운 누적값을 넣을 통
    for now_k in range(K):                          # 현재 단계의 각 라인을 살혀본다.
        no_id_change = total[now_k]                 # 라인이 바뀌지 않은 채로 현재 라인에 멈췄을 때,
        id_change = min_total + pre[-1]             # 라인이 바뀌어 현재 라인에 멈췄을 때,

        new_total[now_k] = min(no_id_change, id_change) + now[now_k]    # 현재 라인에 멈췄을 때의 최솟 누적값을 새로운 누적값에 넣어준다.

    pre = now                       # 현재 단계가 다음 단계에서는 이전 단계가 된다.
    total = new_total               # 현재 누적 값이 다음 단계에서는 total 값으로 바뀐다.

# 모든 단계가 끝났을 때 누적값 중 최솟값 구하기
print(min(total))