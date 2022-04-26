import sys
sys.stdin = open('input.txt')

# 2. data의 r번째 행 or 열에서 활주로를 건설할 수 있는지 확인
def solution(r, data):
    global ans
    visited = [0] * N                   # 경사로를 둘 수 있는지 확인
    ans += 1                            # 우선 활주로 건설 가능하다고 가정

    # 2-1. 현재 블럭의 왼쪽 블럭과 비교해서 높이가 높으면 1, 높이가 낮으면 -1
    now = data[r][0]
    for c in range(1, N):
        # 2-2. 왼쪽 > 오른쪽 -> 오른쪽 블럭에 경사로를 두어야 한다.
        if data[r][c] == now - 1:
            visited[c] = 1                                                                          # 높이가 낮아진 시작점에 바로 경사로를 넣을 수 있다.
            for j in range(1, X):                                                                   # X 길이의 경사로를 둘 수 있는 곳인지 확인한다.
                if 0 <= c + j < N and data[r][c + j] == data[r][c] and not visited[c + j]:          # 인덱스범위에 있고, 경사로 둘 수 있고, 이미 다른 경사로를 둔 곳이 아니라면
                    visited[c + j] = 1                                                              # 경사로를 두었다고 표시
                else:
                    ans -= 1
                    return
        # 2-3. 왼쪽 < 오른쪽 -> 왼쪽 블럭에 경사로를 두어야한다.
        elif data[r][c] == now + 1:
            # 높이가 높아진 지점의 왼쪽 블럭에 경사로를 두어야 하므로 range의 범위는 1~X이다.
            for j in range(1, X + 1):
                if 0 <= c - j < N and data[r][c - j] == data[r][c] - 1 and not visited[c - j]:
                    visited[c - j] = 1
                else:
                    ans -= 1
                    return
        # 2-4. 경사가 2만큼 차이 -> 경사로 설치 불가
        elif abs(data[r][c] - now) > 1:
            ans -= 1
            return
        now = data[r][c]

# 1. 입력받기
T = int(input())
for tc in range(1, T + 1):
    N, X = map(int, input().split())
    # 1-1. 행 기준 2차원 arr
    data = [list(map(int, input().split())) for _ in range(N)]
    # 1-2. 열 기준 2차원 arr
    col_data = list(zip(*data))

    ans = 0
    for r in range(N):
        solution(r, data)
        solution(r, col_data)
    print(f'#{tc}', ans)