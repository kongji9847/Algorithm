# 테케 여러개
import sys
sys.stdin = open('input.txt')

from pprint import pprint

delta = [(0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(N)]
    clouds = [[N-1, 0], [N-1, 1], [N-2, 0], [N-2, 1]]
    for m in range(M):
        direction, speed = map(int, input().split())
        cloud_visited = [[0] * N for _ in range(N)]

        for cloud in clouds:
            cloud[0] = (cloud[0] + delta[direction-1][0] * speed + N * 50) % N
            cloud[1] = (cloud[1] + delta[direction-1][1] * speed + N * 50) % N
            cloud_visited[cloud[0]][cloud[1]] = 1
            data[cloud[0]][cloud[1]] += 1

        #pprint(data)

        rain_box = []
        for cloud in clouds:
            rain_box_cnt = 0
            for d in (1, 3, 5, 7):
                nr = cloud[0] + delta[d][0]
                nc = cloud[1] + delta[d][1]
                if 0 <= nr < N and 0 <= nc < N and data[nr][nc] > 0:
                    rain_box_cnt += 1
            rain_box.append(rain_box_cnt)

        for cloud_index in range(len(clouds)):
            data[clouds[cloud_index][0]][clouds[cloud_index][1]] += rain_box[cloud_index]

        #pprint(data)

        clouds = []
        for r in range(N):
            for c in range(N):
                if data[r][c] >= 2 and not cloud_visited[r][c]:
                    data[r][c] -= 2
                    clouds.append([r, c])

        #pprint(data)

    total = 0
    for row in range(N):
        total += sum(data[row])
    print(total)