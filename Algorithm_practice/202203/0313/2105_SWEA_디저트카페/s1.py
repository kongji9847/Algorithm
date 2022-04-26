# dfs 구현 -> 직진 or 방향을 꺾을 것인지(모든 노드는 2가지 경우로 나눠짐)

# 2. 함수 정의
from copy import deepcopy
delta = [(1, -1), (1, 1), (-1, 1), (-1, -1)]            # 반시계방향 돌기
def cafe(N, data):
    ans = -1
    # 2-1. 기준점 찾기 -> 반시계방향으로 최소 4개를 돌 수 있는 시작점
    for r in range(N-2):
        for c in range(1, N-1):
            # 시작점에서 왼쪽 아래로 내려가서 숫자가 같으면 포기
            if data[r][c] == data[r+1][c-1]:
                continue

            # 2-2. 기준점에서 움직이기
            # 그렇지 않으면 두번째 step부터 시작하기 -> 두번째 스텝부터 직진을 할 것인지 방향을 꺾을 것인지 선택할 수 있다.
            # 단, 왼쪽 위로 가는 경우는 방향을 꺾을 수 없다.
            stack = [[r+1, c-1, 0, [data[r][c], data[r+1][c-1]]]]
            while stack:                                                    # 한 기준점에서 나올 수 있는 모든 경우를 구하기
                sr, sc, pos, dessert = stack.pop()
                for i in range(2):
                    # 2-2-1. 직진
                    if i == 0:
                        nr = sr + delta[pos%4][0]
                        nc = sc + delta[pos%4][1]
                        if 0 <= nr < N and 0 <= nc < N:
                            if nr == r and nc == c:                         # 첫 시작점으로 돌아왔다면 ans 갱신
                                if len(dessert) > ans:
                                    ans = len(dessert)
                            else:
                                if not (data[nr][nc] in dessert):          # dessert가 중복되었는지 여부 따지기
                                    dessert1 = deepcopy(dessert)
                                    dessert1.append(data[nr][nc])
                                    stack.append([nr, nc, pos, dessert1])
                    # 2-2-2. 방향 꺾기
                    else:
                        if pos%4 == 3:                                     # 왼쪽 위로 가는 경우는 방향을 꺾을 수 없다.
                            break
                        nr = sr + delta[(pos+1)%4][0]
                        nc = sc + delta[(pos+1)%4][1]
                        if 0 <= nr < N and 0 <= nc < N:
                            if nr == r and nc == c:
                                if len(dessert) > ans:
                                    ans = len(dessert)
                            else:
                                if not (data[nr][nc] in dessert):
                                    dessert2 = deepcopy(dessert)
                                    dessert2.append(data[nr][nc])
                                    stack.append([nr, nc, pos+1, dessert2])
    return ans


# 1. input 받기
import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    print(f'#{tc}', cafe(N, data))