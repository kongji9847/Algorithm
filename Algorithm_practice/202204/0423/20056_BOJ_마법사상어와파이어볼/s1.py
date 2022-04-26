# import sys
# sys.stdin = open('input.txt')

delta = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]

# 2. 시행 과정을 나타내는 함수
def solution(K, data):
    # 2-1. K번 시행
    for _ in range(K):
        new_data = [[[] for _ in range(N)] for _ in range(N)]                       # 이동한 파이어볼을 담을 배열
        over_2 = set()                                                              # 2개가 넘는 파이어볼을 가진 칸의 위치 넣는 set

        # 2-2. 파이어볼 이동하기
        for r in range(N):
            for c in range(N):
                if data[r][c]:
                    for i in range(len(data[r][c])):                                # 한 칸에 파이어볼이 여러개라면 각 파이어볼을 이동시키기
                        direction = data[r][c][i][2]
                        speed = data[r][c][i][1]
                        nr = (r + delta[direction][0]*speed + N*1000) % N           # -1 은 N 인덱스를 나타내므로 주기 N으로 나타내기
                        nc = (c + delta[direction][1]*speed + N*1000) % N

                        new_data[nr][nc].append(data[r][c][i])                      # 새로운 배열에 이동한 파이어볼 넣기

                        if len(new_data[nr][nc]) >= 2:                              # 해당 배열에 파이어볼이 2개 이상이라면
                            over_2.add((nr, nc))                                    # over_2 set에 넣어주기


        # 2-3. 이동이 끝난 후 2개 이상의 파이어볼 처리
        for rr, cc in over_2:                                                       # 2개 이상의 파이어볼이 있는 칸을 차례로 돌면서
            merge_fireball = [[0, 0, 0], [0, 0, 2], [0, 0, 4], [0, 0, 6]]           # 4개로 나뉠 파이어볼의 방향을 미리 지정하고(우선 모두 짝수, 홀수인 상태로 가정)
            ball_numbers = len(new_data[rr][cc])
            mass_sum = 0
            speed_sum = 0
            flag = new_data[rr][cc][0][2] % 2                                       # 방향델타의 짝 홀 판단하기 위해서

            for j in range(ball_numbers):                                           # 같은 칸 안에 있는 파이어볼의 질량 합, 속도 합, 방향 짝 홀 판단
                mass_sum += new_data[rr][cc][j][0]
                speed_sum += new_data[rr][cc][j][1]
                if new_data[rr][cc][j][2] % 2 != flag:                              # 방향이 이전 파이어볼과 다르면 merge_fireball의 방향을 바꾼다.
                    merge_fireball = [[0, 0, 1], [0, 0, 3], [0, 0, 5], [0, 0, 7]]

            if mass_sum//5 == 0:                                                    # 질량이 없어지면 해당 칸 파이어볼 없애기
                new_data[rr][cc] = []
            else:                                                                   # 그렇지 않다면
                for k in range(4):                                                  # 파이어볼의 질량, 속도 나눠서 4개로 만들기
                    merge_fireball[k][0] = mass_sum//5
                    merge_fireball[k][1] = speed_sum//ball_numbers

                new_data[rr][cc] = merge_fireball                                   # merge_fireball을 new_data에 적용하기

        # 2-4. 다음 시행을 위해 data를 new_data로 갱신해주기
        data = new_data

    # 2-5. 시행이 모두 끝난 후 각 파이어볼의 질량 합 구하고 출력하기
    ans = 0
    for sr in range(N):
        for sc in range(N):
            if data[sr][sc]:
                for i in range(len(data[sr][sc])):
                    ans += data[sr][sc][i][0]
    print(ans)


# T = int(input())
# for tc in range(1, T+1):

# 1. input 받기
N, M, K = map(int, input().split())
data = [[[] for _ in range(N)] for _ in range(N)]
for _ in range(M):
    r, c, m, s, d = map(int, input().split())
    data[r-1][c-1].append((m, s, d))

# 결과값 내기
solution(K, data)