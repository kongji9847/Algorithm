# dfs - 재귀로 구현 : 중간에 불가능하거나 빨강이 구멍에 들어간 경우 return을 해주었다.
# -> 이 때, return 전에 변경한 배열 되돌려 놓기
# 왔다 갔다 할 필요 없음 -> 상 하 상 하 이런거 필요없음

# import sys
# sys.stdin = open('input.txt')

delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]
position = [(2, 3), (2, 3), (0, 1), (0, 1)]             # 다음에 굴릴 방향 인덱스 ex) 지금 0번 방향이면 다음은 2번이나 3번

# 2. d 방향으로 red, blue 공 옮기기
def solution(try_cnt, d, rr, rc, br, bc):
    global min_cnt
    # 3. 가지치기
    if try_cnt >= min_cnt:
        return

    # 1. 진행
    data[rr][rc] = '.'          # 이동해야 하므로 현재 위치의 red, blue 자리 비워주기
    data[br][bc] = '.'

    nrr, nrc, nbr, nbc = rr, rc, br, bc

    # 1-1. red, blue공 d방향으로 한칸씩 이동시키기
    while True:                 # 불가능한 경우는 return 문을 만나서 종료시켜줬고, 가능한 경우는 break 문으로 빠져 나왔다.
        nrr += delta[d][0]
        nrc += delta[d][1]
        nbr += delta[d][0]
        nbc += delta[d][1]

        # 1-2. 빨강공이 먼저 벽과 동일한 위치로 이동했을 때,
        if data[nrr][nrc] == '#':
            nrr -= delta[d][0]
            nrc -= delta[d][1]
            data[nrr][nrc] = 'R'                        # 벽의 바로 전 칸이 빨강공의 최종 위치

            nbr -= delta[d][0]                          # 파란 공도 이동하기 전 칸으로 다시 이동
            nbc -= delta[d][1]
            # if문이자 반복문 -> 파랑공이 더 갈 수 있을 때까지 이동(벽이나 빨강공과 만나기 전까지 이동)
            while not(data[nbr][nbc] == '#' or data[nbr][nbc] == 'R'):
                nbr += delta[d][0]
                nbc += delta[d][1]

                if data[nbr][nbc] == 'O':               # 파랑공이 구멍에 들어가면 바로 return해서 함수 종료
                    data[nrr][nrc] = '.'                # 빨강공, 파랑공의 최종 위치를 함수의 시행 전으로 돌려 준다.
                    data[rr][rc] = 'R'
                    data[br][bc] = 'B'
                    return

            nbr -= delta[d][0]                          # 파랑공이 구멍에 들어가지 않고 벽을 만나 멈춘 경우
            nbc -= delta[d][1]                          # 파랑공의 최종 위치 정해주고
            data[nbr][nbc] = 'B'
            break                                       # break으로 while True 문 종료

        # 1-3 파랑공이 먼저 벽과 만났을 때
        elif data[nbr][nbc] == '#':
            nbr -= delta[d][0]
            nbc -= delta[d][1]
            data[nbr][nbc] = 'B'                        # 파랑공 최종위치 정해주고

            # 빨강공 더 이동할 수 있을 때까지 이동 시켜준다.
            nrr -= delta[d][0]
            nrc -= delta[d][1]
            while not (data[nrr][nrc] == '#' or data[nrr][nrc] == 'B'):
                nrr += delta[d][0]
                nrc += delta[d][1]

                if data[nrr][nrc] == 'O':                   # 빨강공이 구멍에 들어갔다면
                    min_cnt = min(min_cnt, try_cnt+1)       # 최소 시행 갱신
                    data[nbr][nbc] = '.'                    # 함수 종료 해야하므로 함수 시행 전으로 돌려 놓는다
                    data[rr][rc] = 'R'                      # 다음 경우의 수를 확인할 때 영향 없도록
                    data[br][bc] = 'B'
                    return

            nrr -= delta[d][0]                              # 모든 공이 멈췄다면 빨강공 최종위치 정해주고
            nrc -= delta[d][1]                              # break
            data[nrr][nrc] = 'R'
            break

        # 1-4. 빨강공이 먼저 구멍에 들어갔다면
        elif data[nrr][nrc] == 'O':
            while not (data[nbr][nbc] == '#' or data[nbr][nbc] == 'R'):     # 파랑공도 구멍에 들어갈 수 있는지 확인한다.
                nbr += delta[d][0]
                nbc += delta[d][1]

                if data[nbr][nbc] == 'O':                       # 파랑공 구멍에 들어갈 수 있다면 불가능한 함수므로 함수 종료
                    data[rr][rc] = 'R'                          # 빨강 파랑 원 위치 돌려놓기(함수 시행전으로)
                    data[br][bc] = 'B'
                    return

            min_cnt = min(min_cnt, try_cnt + 1)                 # 파랑공은 구멍에 들어가지 않았다면
            data[rr][rc] = 'R'                                  # 빨강, 파랑 함수 시행 전으로 돌려 놓고 함수 종료
            data[br][bc] = 'B'
            return

        # 1-5. 파랑공이 먼저 구멍에 들어갔다면 함수 종료
        elif data[nbr][nbc] == 'O':
            data[rr][rc] = 'R'
            data[br][bc] = 'B'
            return

    # 2. break문이 작동한 경우, 다음 방향 확인하기 -> 함수 시행한 결과가 data에 저장되어 있음 -> 그걸 다음 함수에서 활용해야 함
    solution(try_cnt+1, position[d][0], nrr, nrc, nbr, nbc)
    # return 문을 만나 종료된 함수가 돌아옴 -> return 문을 만나면 함수 시행 전 배열로 돌려 놓게 해둠 -> 같은 레벨의 다른 방향으로 이동
    solution(try_cnt + 1, position[d][1], nrr, nrc, nbr, nbc)
    # 위의 재귀함수가 return 문을 만나 종료되었다면
    data[nrr][nrc] = '.'        # 재귀 함수 호출 전, main 함수의 시행 전으로 바꿔놓기
    data[nbr][nbc] = '.'
    data[rr][rc] = 'R'
    data[br][bc] = 'B'

# T = int(input())
# for tc in range(1, T+1):

# 1. input 받기
N, M = map(int, input().split())
data = [list(input()) for _ in range(N)]
min_cnt = 11
for r in range(1, N-1):
    for c in range(1, M-1):
        if data[r][c] == '.':
            continue
        elif data[r][c] == 'R':
            red_r, red_c = r, c
        elif data[r][c] == 'B':
            blue_r, blue_c = r, c


solution(0, 0, red_r, red_c, blue_r, blue_c)

solution(0, 1, red_r, red_c, blue_r, blue_c)

solution(0, 2, red_r, red_c, blue_r, blue_c)

solution(0, 3, red_r, red_c, blue_r, blue_c)


if min_cnt == 11:
    print(-1)

else:
    print(min_cnt)
