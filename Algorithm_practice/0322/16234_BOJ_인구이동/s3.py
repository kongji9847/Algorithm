# python은 시간초과, pypy 사용은 통과
# bfs 사용시, 현재는 연결되지 않았더라도 다음 단계에서 연결 될수 있으므로 지나가더라도 연결이 아니면 방문체크 안한다.
from collections import deque
delta = [(-1, 0), (1, 0), (0, 1), (0, -1)]
def country(data):
    answer = 0
    while True:
        info = [[0] * N for _ in range(N)]                  # 새로운 날마다 방문체크(섬체크) 초기화
        modi = []                                           # 인구변화가 일어나는 모든 인덱스 담기 [[(r1, c1), (r2, c2)], [(r3, c3), (r4, c4)] ]
        cnts = []                                           # 인구변화가 일어나는 나라의 인구수    [cnt1, cnt2 ]
        for r in range(N):
            for c in range(N):
                if info[r][c] == 0:
                    modify = [(r, c)]                           # modify : r, c에서 시작했을 때 인구변화가 일어날 위치들
                    cnt = data[r][c]                            # cnt: 위치 변화할 나라의 인구수
                    info[r][c] = 1                              # info에 지나갔다고 표시해주기

                    Q = deque([(r, c)])                         # Q에 시작지점을 넣어놓고 bfs 돌리기
                    while Q:
                        sr, sc = Q.popleft()                    # 시작지점에서 상하좌우로 움직여 연결된 부분 찾기
                        for i in range(4):
                            nr = sr + delta[i][0]
                            nc = sc + delta[i][1]
                            if 0 <= nr < N and 0 <= nc < N and info[nr][nc] == 0:
                                if L <= abs(data[nr][nc] - data[sr][sc]) <= R:
                                    info[nr][nc] = 1            # 연결되면 info에 표시해주고
                                    Q.append((nr, nc))          # 큐에 넣어주고
                                    cnt += data[nr][nc]         # 인구수와 인덱스 각각 누적해주기
                                    modify.append((nr, nc))

                    if len(modify) > 1:                         # 하나의 시작지점에서 가능한 모든 연결지점을 봤는데, 연결지점이 있다면
                        modi.append(modify)                     # modi에 인덱스리스트를 넣어주고, cnts에 누적합을 넣어준다.
                        cnts.append(cnt)

        if modi:                                                # modi가 존재한다면, 연결지점들이 있다면 data의 값을 수정해주고
            for i in range(len(modi)):
                for j, k in modi[i]:
                    data[j][k] = cnts[i] // len(modi[i])
            answer += 1                                         # 하루가 지났고, 다음날로 가야한다 -> while True를 통해
        else:                                                   # 연결지점이 없다면 data의 값을 수정하지 않고 바로 지난 날을 리턴
            return answer

import sys
# sys.stdin = open('input.txt')
#
# T = int(input())
# for tc in range(1, T + 1):

N, L, R = map(int, sys.stdin.readline().split())
data = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
print(country(data))
