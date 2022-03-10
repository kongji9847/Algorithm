import sys
sys.stdin = open('input.txt')
# 시간초과
def collision(data):
    sum_e = 0
    delta = [(0, 1), (0, -1), (-1, 0), (1, 0)]      # 상하좌우
    visited = [0] * len(data)
    for _ in range(4002):
        for element in data:
            d = delta[element[3]]
            element[1] += d[0]
            element[2] += d[1]
        for f in range(len(data)-1):
            if visited[f] == 1:
                continue
            for s in range(f+1, len(data)):
                if visited[s] == 1:
                    continue
                else:
                    if (data[f][1] == data[s][1] and data[f][2] == data[s][2]):
                        visited[f] = 1
                        visited[s] = 1
    for i in range(len(visited)):
        if visited[i] == 1:
            sum_e += data[i][4]

    return sum_e



T = int(input())
for tc in range(1, T+1):
    N = int(input())
    data = []
    for i in range(N):
        x, y, dr, k = map(int, input().split())
        data.append([i, x*2, y*2, dr, k])
    print(f'#{tc}', collision(data))