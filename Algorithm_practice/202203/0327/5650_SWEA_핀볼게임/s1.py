# 모든 빈칸에서 상하좌우 4방향일 때를 전부 고려해주기
import sys
sys.stdin = open('input.txt')

delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]
# 해당 인덱스의 블럭을 만났을 때, 직진을 key, 튕겨나가는 방향은 value -> block[0][0] -> 1번 블럭을 만났고 진행 방향이 상이라면 하로 튕겨져 나간다.
block = [{0:1, 1:3, 2:0, 3:2}, {0:3, 1:0, 2:1, 3:2}, {0:2, 1:0, 2:3, 3:1}, {0:1, 1:2, 2:3, 3:0}, {0:1, 1:0, 2:3, 3:2}]


def game(sr, sc, dr, dc):
    score = 0
    nr, nc = sr, sc
    ndr, ndc = dr, dc
    while True:
        nr += ndr                                                           # 항상 이동 방향이 반영된 새로운 nr, nc로 시작
        nc += ndc
        if nr == -1 or nr == N or nc == -1 or nc == N:                      # 벽과 만나서 통과한 경우 -> 점수 반영, 추후 진행 방향 바꾸기
            score += 1
            ndr *= -1
            ndc *= -1
            continue                                                        # 블랙홀인지, 시작점으로 돌아왔는지 확인할 필요없다. -> 어차피 인덱스 밖이므로

        else:                                                               # 인덱스 안에 포함되어 있다면,
            if 1 <= board[nr][nc] < 6:                                      # block과 만난다면 진행방향 바꿔주고 점수에 반영
                delta_index = delta.index((ndr, ndc))
                (ndr, ndc) = delta[block[board[nr][nc]-1][delta_index]]
                score += 1
            elif board[nr][nc] >= 6:                                        # 웜홀과 만났을 때
                nr, nc = warmhole[(nr, nc)]
                                                                            # 빈칸(0)은 고려하지 않아도 된다. ndr, ndc가 변경없이 그대로 반영
        if board[nr][nc] == -1 or (nr == sr and nc == sc):                  # 새로 이동한 곳이 블랙홀이나 시작점이라면 중지
            break
    return score



T = int(input())
for tc in range(1, T+1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    # 시작지점과 웜홀 딕셔너리 만들어주기
    start = []
    visited = [0, 0, 0, 0, 0]
    warmhole = {}
    for i in range(N):
        for j in range(N):
            if board[i][j] == 0:
                start.append((i, j))
            elif board[i][j] >= 6:
                if visited[board[i][j]-6] == 0:
                    visited[board[i][j]-6] = (i, j)
                else:
                    warmhole[(i, j)] = visited[board[i][j]-6]
                    warmhole[visited[board[i][j]-6]] = (i, j)

    # 모든 좌표, 모든 방향 보면서 최고 점수 갱신하기
    answer = 0
    for sr, sc in start:
        for dr, dc in delta:
            ans = game(sr, sc, dr, dc)
            if ans > answer:
                answer = ans
    print(f'#{tc}', answer)