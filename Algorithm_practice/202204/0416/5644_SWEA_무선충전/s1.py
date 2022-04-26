'''
충전량을 구할 때,
userA: 가능한 충전기 1개/userB: 가능한 충전기 2개일 경우
userA에서 무조건 충전기 1개를 사용해야하므로, 해당 충전량을 방문 상관없이 더해주기만 했다.
이렇게 되면 나중에 userA: 가능한 충전기 2개/userB:가능한 충전기 1개일 경우 이미 사용한 충전기를 중복해서 충전량을 더해주게 된다.
'''

import sys
sys.stdin = open('input.txt')
from collections import deque
delta = [(0, 0), (-1, 0), (0, 1), (1, 0), (0, -1)]

# 4. dfs 함수로 각 위치에서 최대 충전량 구하기
# Ar, Ac, Br, Bc : A와 B의 위치 인덱스, value: 해당 위치에서의 충전량, n: 현재 충전이 완료된 사용자
def dfs(Ar, Ac, Br, Bc, value, n):
    global max_val
    # 종료
    if n == 2:
        max_val = max(max_val, value)
        return
    #4-1. 진행
    if n == 0:                                                                      # 현재 봐야할 유저가 A일 때,
        if len(data[Ar][Ac]) == 1:                                                  # 가능한 충전기가 1개일 때
            if not used[data[Ar][Ac][0][0]]:                                        # 현재 충전기가 사용중이 아니라면,
                used[data[Ar][Ac][0][0]] = 1                                        # 사용중으로 표시하고
                dfs(Ar, Ac, Br, Bc, value+data[Ar][Ac][0][1], n+1)                  # value에 현재 충전기의 충전량을 더해주고, 다음 유저로 넘어가기
                used[data[Ar][Ac][0][0]] = 0                                        #
            else:
                dfs(Ar, Ac, Br, Bc, value, n + 1)
        elif len(data[Ar][Ac]) == 0:
            dfs(Ar, Ac, Br, Bc, value, n+1)
        elif len(data[Ar][Ac]) > 1:
            for i in range(len(data[Ar][Ac])):
                if used[data[Ar][Ac][i][0]] == 0:
                    used[data[Ar][Ac][i][0]] = 1
                    dfs(Ar, Ac, Br, Bc, value + data[Ar][Ac][i][1], n+1)
                    used[data[Ar][Ac][i][0]] = 0
                else:
                    dfs(Ar, Ac, Br, Bc, value, n + 1)

    elif n == 1:
        if len(data[Br][Bc]) == 1:
            if not used[data[Br][Bc][0][0]]:
                used[data[Br][Bc][0][0]] = 1
                dfs(Ar, Ac, Br, Bc, value + data[Br][Bc][0][1], n + 1)
                used[data[Br][Bc][0][0]] = 0
            else:
                dfs(Ar, Ac, Br, Bc, value, n + 1)
        elif len(data[Br][Bc]) == 0:
            dfs(Ar, Ac, Br, Bc, value, n+1)
        elif len(data[Br][Bc]) > 1:
            for i in range(len(data[Br][Bc])):
                if used[data[Br][Bc][i][0]] == 0:
                    used[data[Br][Bc][i][0]] = 1
                    dfs(Ar, Ac, Br, Bc, value + data[Br][Bc][i][1], n+1)
                    used[data[Br][Bc][i][0]] = 0
                else:
                    dfs(Ar, Ac, Br, Bc, value, n + 1)


# 1. input 받기
T = int(input())
for tc in range(1, T+1):
    M, A = map(int, input().split())
    data = [[[] for _ in range(10)] for _ in range(10)]
    userA = list(map(int, input().split()))
    userB = list(map(int, input().split()))

    # 2. bfs로 각 충전 범위만큼 data에 BC 인덱스, 충전성능 표시하기
    visited = [[-1] * 10 for _ in range(10)]                                                # used 사용해서 이미 방문한 부분은 다시 방문하지 않기
    for a in range(A):                                                                      # 충전기 개수만큼 반복
        AP_x, AP_y, C, P = map(int, input().split())                                        # 충전기 input 정보 받기
        Q = deque([(AP_y-1, AP_x-1, 0)])
        data[AP_y-1][AP_x-1].append((a, P))
        visited[AP_y-1][AP_x-1] = a
        while Q:
            rr, cc, dist = Q.popleft()
            if dist < C:                                                                    # 충전 가능 범위 따지기
                for d in range(1, 5):
                    nr = rr + delta[d][0]
                    nc = cc + delta[d][1]
                    if 0 <= nr < 10 and 0 <= nc < 10 and visited[nr][nc] != a:
                        visited[nr][nc] = a
                        data[nr][nc].append((a, P))
                        Q.append((nr, nc, dist+1))


    # 3. 경로로 이동하며 answer에 충전량 누적하기
    # 3-1. 0초일 때,
    answer = 0
    Ar, Ac = 0, 0
    Br, Bc = 9, 9
    max_val = 0
    used = [0] * A                          # 충전기 사용 유무 따져야 하므로
    dfs(Ar, Ac, Br, Bc, 0, 0)               # dfs 함수 사용해서 해당 시간에 가능한 최대 충전 범위 찾기
    answer += max_val
    # 3-2. 1초부터 M초까지 확인
    for time in range(M):
        Ar += delta[userA[time]][0]
        Ac += delta[userA[time]][1]
        Br += delta[userB[time]][0]
        Bc += delta[userB[time]][1]
        max_val = 0                         # 해당 구간에서 사용할 최댓값 상자 초기화
        dfs(Ar, Ac, Br, Bc, 0, 0)
        answer += max_val                   # 최댓값을 answer에 더하여 갱신하기
    print(f'#{tc}', answer)