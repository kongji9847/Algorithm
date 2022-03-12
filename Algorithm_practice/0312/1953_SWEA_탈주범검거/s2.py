# bfs에서 L-1 step만 진행한다. -> while Q 대신, for i in range(L-1)
# 2. 사전 준비
delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]      # 상하좌우
# 구조물 타입 번호에 따른 이동 방향
structure = [ [], delta, [delta[0], delta[1]], [delta[2], delta[3]],
              [delta[0], delta[3]], [delta[1], delta[3]],
              [delta[1], delta[2]], [delta[0], delta[2]] ]
# A블럭에서 인접한 B 블록으로 상하좌우 이동하기 위해 B 블록이 갖춰야할 구조물 타입
cango = [[1, 2, 5, 6], [1, 2, 4, 7], [1, 3, 4, 5], [1, 3, 6, 7]]

from collections import deque
def escaping(R, C, L):
    # start 지점을 Q에 넣어준다.
    Q = deque([[R, C]])
    for _ in range(L-1):                                                        # 소요 시간 만큼 반복(시작지점은 이미 Q에 있으니 L-1 만큼만 반복)
        for _ in range(len(Q)):                                                 # Q에 들어 있는 원소 개수 = 다음 단계로 넘어갈 수 있는 블록 수 만큼 반복
            vr, vc = Q.popleft()
            for element in structure[data[vr][vc]]:                             # 현재 지점의 구조물 파악하고 명시된 방향대로 다음 블록으로 이동
                nr = vr + element[0]
                nc = vc + element[1]
                indx = delta.index(element)                                     # 방향이 상하 좌우인지 확인
                if 0 <= nr < N and 0 <= nc < M and data[nr][nc] != 0:           # 다음 블록이 인덱스 에러도 없고, 0으로 막혀있지 않으면
                    if data[nr][nc] in cango[indx]:                             # 다음 블록이 갖춰야할 구조물 타입을 가졌으면 Q에 집어넣는다.
                        Q.append([nr, nc])
            Q.append([vr, vc])                                                  # Q에서 뽑아낸 처음 출발 위치도 포함해준다.

        Q1 = set(tuple(map(tuple, Q)))                                          # 현재 단계에서 갈 수 있는 모든 블록으로 이동한 후, 남은 블록은 중복을 제거하여 Q를 초기화한다.
        Q = deque(Q1)                                                           # -> 불필요한 반복으로 시간을 절약할 수 있다.

    ans = tuple(map(tuple, Q))
    answer = set(ans)
    return len(answer)

# 1. input 값 받기
import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T+1):
    # 행, 열, [R, C]: 맨홀 뚜껑 위치, L: 소요시간
    N, M, R, C, L = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(N)]
    print(f'#{tc}', escaping(R, C, L))

