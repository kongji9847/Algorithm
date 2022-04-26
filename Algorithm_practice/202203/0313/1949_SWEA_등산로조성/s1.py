# dfs 사용해서 상하좌우 움직이기 - (불가능한 지역 갔을 때: 1. 깎아서 가기 or 2. 이미 깎음 사용 -> 멈추기)
# 산을 깎기 때문에 산의 높이 비교는 산을 깎은 데이터를 보고 비교해야 된다.
# 2. 함수만들기
from copy import deepcopy
delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]          # 상하좌우
def course(N, K, my_max):
    # 2-1. 가장 높은 봉우리 찾기
    tops = []
    for r in range(N):
        for c in range(N):
            if data[r][c] == my_max:
                tops.append((r, c))

    # 2-2. top 지점 하나씩 움직이기
    max_road = 0
    for top in tops:
        # 2-3. dfs 사용해서 움직이기 - (불가능한 지역 갔을 때: 1. 깎아서 가기 or 2. 이미 깎음 사용 -> 멈추기)
        visited = [[0] * N for _ in range(N)]
        visited[top[0]][top[1]] = data[top[0]][top[1]]
        stack = [[top, visited, 0, 1]]

        while stack:
            (r, c), visited, shave, cnt = stack.pop()
            # 2-3-1. 상하좌우로 움직이기
            for i in range(4):
                nr = r + delta[i][0]
                nc = c + delta[i][1]

                # 2-3-2. 움직였을 때 인덱스 에러 안나고 가본 곳이면,
                if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc]:
                    # new_visit에 진행상황과 산의 높이 표시해주기
                    new_visit = deepcopy(visited)
                    new_visit[nr][nc] = data[nr][nc]

                    #1) 새로운 산이 더 낮으면 stack에 추가
                    if new_visit[nr][nc] < new_visit[r][c]:
                        stack.append([(nr, nc), new_visit, shave, cnt+1])

                    #2) 깎을 수 있다면 깎아서 new_visit 갱신해주기 -> 새로운 정보 stack에 추가
                    elif not shave and (K >= (new_visit[nr][nc] - (new_visit[r][c]-1))):
                        new_visit[nr][nc] = (data[r][c]-1)
                        stack.append([(nr, nc), new_visit, 1, cnt+1])

                    #3)못 깎는다면 max값 갱신
                    else:
                        if cnt > max_road:
                            max_road = cnt

    return max_road


# 1. input 받기
import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(N)]
    max_num = 0
    for i in range(N):
        if max_num < max(data[i]):
            max_num = max(data[i])
    print(f'#{tc}', course(N, K, max_num))