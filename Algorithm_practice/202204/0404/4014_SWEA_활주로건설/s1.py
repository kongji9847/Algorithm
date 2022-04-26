import sys
sys.stdin = open('input.txt')

def solution(data):
    ans = 0
    for r in range(N):
        check = []
        visited = [0]*N
        flag = 1

        now = data[r][0]
        for c in range(1, N):
            if data[r][c] == now - 1:
                check.append([(r, c), -1])
            elif data[r][c] == now + 1:
                check.append([(r, c), 1])
            elif abs(data[r][c] - now) > 1:
                flag = 0
                break
            now = data[r][c]

        if flag == 0:
            continue

        ans += 1
        for i in range(len(check)):
            (r, c), pos = check[i]
            # 왼쪽에 있는 블록보다 오른쪽에 있는 블록이 낮아 오른쪽에 경사로를 만들어야 할 때
            if pos == -1:
                visited[c] = 1
                for j in range(1, X):
                    if 0 <= c+j < N and data[r][c+j] == data[r][c] and not visited[c+j]:
                        visited[c+j] = 1
                    else:
                        flag = 0
                        break
            # 왼쪽에 있는 블록보다 오른쪽에 있는 블록이 높아 왼쪽에 경사로를 만들어야 할 때
            elif pos == 1:
                for j in range(1, X+1):
                    if 0 <= c-j < N and data[r][c-j] == data[r][c] - 1 and not visited[c-j]:
                        visited[c-j] = 1
                    else:
                        flag = 0
                        break
            if flag == 0:
                row.pop()
                ans -= 1
                break

    #print(row)
    return ans




T = int(input())
for tc in range(1, T+1):
    N, X = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(N)]
    col_data = list(zip(*data))
    print(f'#{tc}', solution(data)+solution(col_data))