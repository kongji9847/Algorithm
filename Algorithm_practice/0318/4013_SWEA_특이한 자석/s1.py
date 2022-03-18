# pointer 활용해서 자석의 배열을 변경하지 않기
import sys
sys.stdin = open('input.txt')
from collections import deque

def solution(m, circle):
    #2. 상태파악 -> 회전 가능성 파악
    state = [1, int(magnets[0][ma[0][0]] == magnets[1][ma[1][0]]),
             int(magnets[0][ma[0][0]] == magnets[1][ma[1][0]]), int(magnets[1][ma[1][1]] == magnets[2][ma[2][0]]),
             int(magnets[1][ma[1][1]] == magnets[2][ma[2][0]]), int(magnets[2][ma[2][1]] == magnets[3][ma[3][0]]),
             int(magnets[2][ma[2][1]] == magnets[3][ma[3][0]]), 1]

    # 3. bfs로 선택한 자석 기준에서 회전시켜야할 자석 확인하고 change에 회전 방향 명시하기
    Q = deque([m-1])
    change = [0, 0, 0, 0]
    change[m-1] = circle

    while Q:
        q = Q.popleft()
        # 왼쪽, 오른쪽 -> 더 이상 이동하면 안되는 경우에 자리수에 2 표시해서 전진 막기
        for i in range(2):
            if i == 0:
                nq = q + 1
                if 0 <= nq <= 3 and not change[nq]:
                    change[nq] = 2
                    if not state[q*2 + 1]:
                        change[nq] = -1 * change[q]
                        Q.append(nq)
            else:
                nq = q - 1
                if 0 <= nq <= 3 and not change[nq]:
                    change[nq] = 2
                    if not state[q * 2]:
                        change[nq] = -1 * change[q]
                        Q.append(nq)

    # 4. 회전 구현 -> pointer 이용해서
    # 주기: 8 -> 양수던 음수던 %8 => -1 % 8 == 7
    # 회전방향 주의!!!
    for j in range(4):
        if change[j] == 1 or change[j] == -1:
            ma[j] = list(map(lambda x: (x - change[j]) % 8, ma[j]))


T = int(input())
for tc in range(1, T+1):
    K = int(input())
    magnets = [list(map(int, input().split())) for _ in range(4)]

    # 1. 각 자석에서 집중해야할 position 지정하기 -> position 변경하면서 자석을 회전시켰다고 표현
    # 1번 자석: magnet[2], 2번 자석: magnet[6], [2], 3번 자석: magnet[6][2], 4번 자석: [6]
    ma = [[2, 0], [6, 2, 0], [6, 2, 0], [6, 0]]
    score = 0

    # input 받아서 회전시키기
    for _ in range(K):
        magnet, circle = map(int, input().split())
        solution(magnet, circle)

    # 5. 결과값 내기
    for k in range(4):
        if magnets[k][ma[k][-1]]:
            score += 2**k

    print(f'#{tc}', score)