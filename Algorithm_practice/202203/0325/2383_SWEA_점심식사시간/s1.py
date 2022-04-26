# 한 사람 당, 갈 수 있는 경우의 수 -> 계단1, 계단2
import sys
sys.stdin = open('input.txt')

def dfs(indx, stair1, stair2):
    global ans
    # 1. 종료조건, 최소값 갱신
    if indx >= len(people):                                         # 모든 사람이 계단을 선택했을 때 종료
        stair1.sort()
        stair2.sort()

        if stair1:                                                  # 해당 계단으로 가는 사람이 존재한다면,
            for s1 in range(3, len(stair1)):
                if stair1[s1-3] + stair[0][2] > stair1[s1]:         # 4번째 사람부터 자신의 3번째 전 사람과 비교해서 대기해야 되는지 아닌지의 여부를 따진다.
                    stair1[s1] = stair1[s1-3] + stair[0][2]         # 대기 시간보다 빨리 도착한다 되어 있으면 대기 시간 포함해서 갱신한다.
            time1 = stair1[-1]
        else:
            time1 = 0

        if stair2:
            for s2 in range(3, len(stair2)):
                if stair2[s2-3] + stair[1][2] > stair2[s2]:
                    stair2[s2] = stair2[s2-3] + stair[1][2]
            time2 = stair2[-1]
        else:
            time2 = 0
        time = max(time1, time2)

        # 최소값 선택
        if time < ans:
            ans = time
        return

    # 2. 어떤 계단으로 갈 지 선택
    (r, c) = people[indx]
    time1 = abs(r - stair[0][0]) + abs(c - stair[0][1]) + 1 + stair[0][2]
    time2 = abs(r - stair[1][0]) + abs(c - stair[1][1]) + 1 + stair[1][2]

    dfs(indx+1, stair1 + [time1], stair2)
    dfs(indx+1, stair1, stair2 + [time2])


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    people = []
    stair = []
    for r in range(N):
        for c in range(N):
            if data[r][c] == 1:
                people.append((r, c))
            elif data[r][c] > 1:
                stair.append((r, c, data[r][c]))

    ans = 123456789123456789
    # people 인덱스, stair1, stair2
    dfs(0, [], [])
    print(f'#{tc}', ans)