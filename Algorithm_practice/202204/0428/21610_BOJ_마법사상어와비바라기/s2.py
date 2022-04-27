# 백준 제출용

delta = [(0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]

# 1. input 받기
N, M = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(N)]      # 각 배열에 위치하는 바구니에 담긴 물의 양
clouds = [[N-1, 0], [N-1, 1], [N-2, 0], [N-2, 1]]               # 초기 구름 위치 모음

# 2. 마법을 M번 반복
for m in range(M):
    direction, speed = map(int, input().split())
    cloud_visited = [[0] * N for _ in range(N)]                 # 구름이 지나간 자리

    # 2-1. 구름을 하나씩 이동시키고, 구름의 방문 표시한다. 구름을 이동시킨 후 바구니에 물을 +1씩 증가시킨다.
    for cloud in clouds:
        cloud[0] = (cloud[0] + delta[direction-1][0] * speed + N * 50) % N          # 인덱스가 N을 주기로 반복되므로
        cloud[1] = (cloud[1] + delta[direction-1][1] * speed + N * 50) % N
        cloud_visited[cloud[0]][cloud[1]] = 1
        data[cloud[0]][cloud[1]] += 1

    # 2-2. 비가 내린 자리의 대각선 바구니 확인하고 비의 양 추가해주기
    for cloud in clouds:                                                # 여기서 clouds는 비가 내린 바구니 인덱스를 뜻한다.
        for d in (1, 3, 5, 7):                                          # 대각선 방향만 확인하기
            nr = cloud[0] + delta[d][0]
            nc = cloud[1] + delta[d][1]
            if 0 <= nr < N and 0 <= nc < N and data[nr][nc] > 0:        # 인덱스 에러 나지 않고, 빗물이 있다면
                data[cloud[0]][cloud[1]] += 1                           # 비가 온 바구니에 빗물 추가

    # 2-3. 새로 생긴 구름 clouds에 담고, 바구니 안의 비의 양 줄이기
    clouds = []
    for r in range(N):
        for c in range(N):
            if data[r][c] >= 2 and not cloud_visited[r][c]:
                data[r][c] -= 2
                clouds.append([r, c])

# 3. 마법이 끝나고 모든 비의 양 더해서 반환
total = 0
for row in range(N):
    total += sum(data[row])
print(total)