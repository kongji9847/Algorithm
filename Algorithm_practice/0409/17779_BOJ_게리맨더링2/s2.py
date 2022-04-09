# import sys
# sys.stdin = open('input.txt')

# 4. 해당 사각형 조합에서 지역별 인구 수 구하기
delta = [(1, -1), (1, 1), (-1, 1), (-1, -1)]
def count_people(x, y, d1, d2):
    # 4-1. visited 배열에 5구역 만들어서 1, 2, 3, 4 구역이 침범하지 않도록 하기
    visited = [[0]*(N) for _ in range(N)]
    # 4-1-1. 경계선 표시
    visited[x][y] = 5
    nr, nc = x, y
    for i in range(4):
        if i == 0 or i == 2:
            j = d1
        elif i == 1 or i == 3:
            j = d2
        while j:
            nr += delta[i][0]
            nc += delta[i][1]
            visited[nr][nc] = 5
            j -= 1
    # 4-1-2. 사각형 안의 구역 표시
    for row in range(x+1, x+d1+d2):
        col = visited[row].index(5)
        col += 1
        while visited[row][col] != 5:
            visited[row][col] = 5
            col += 1

    # 4-2. 각 구역별 인구수 구하기 -> 인덱스 범위 설정
    people_dict = {1: 0, 2: 0, 3: 0, 4: 0, 5: total}
    for rr in range(N):
        for cc in range(N):
            if 0 <= rr < x+d1 and 0 <= cc <= y and not visited[rr][cc]:
                people_dict[1] += data[rr][cc]
                people_dict[5] -= data[rr][cc]

            elif 0 <= rr <= x+d2 and y < cc <= N-1 and not visited[rr][cc]:
                people_dict[2] += data[rr][cc]
                people_dict[5] -= data[rr][cc]

            elif x+d1 <= rr <= N-1 and 0 <= cc < y-d1+d2 and not visited[rr][cc]:
                people_dict[3] += data[rr][cc]
                people_dict[5] -= data[rr][cc]

            elif x+d2 < rr <= N-1 and y-d1+d2 <= cc <= N-1 and not visited[rr][cc]:
                people_dict[4] += data[rr][cc]
                people_dict[5] -= data[rr][cc]

    ans = max(people_dict.values()) - min(people_dict.values())
    return ans

# 3. 가능한 평행사변형 조합 구하기
def dfs(sr, sc, d1, d2, dr):
    global min_cnt
    # 3-2. 종료조건 -> 사각형을 절반 만큼 만들었을 때 사각형이 가능한지 확인하고 종료(마지막 모서리가 배열 안에 존재하는 지 확인)
    if dr == 2:
        r_edge = sr + delta[2][0] * d1
        c_edge = sc + delta[2][1] * d1
        # 1. 사각형이 불가능한 경우 바로 return
        if not (0 <= r_edge < N and 0 <= c_edge < N):
            return
        # 2. 가능한 경우 -> min_cnt를 갱신해주고 return
        else:
            ans = count_people(r, c, d1, d2)
            min_cnt = min(ans, min_cnt)
        return

    # 3-1. 진행 -> 직진 or 방향바꾸기
    for d in range(dr, dr+2):
        nr = sr + delta[d][0]
        nc = sc + delta[d][1]
        if 0 <= nr < N and 0 <= nc < N:
            if d == 0:
                dfs(nr, nc, d1+1, d2, d)
            elif d == 1:
                dfs(nr, nc, d1, d2+1, d)
            elif d == 2:
                dfs(sr, sc, d1, d2, d)

# 1. input 받기
N = int(input())
data = [list(map(int, input().split())) for _ in range(N)]
total = 0
for i in range(N):
    total += sum(data[i])
min_cnt = 987654321

# 2. 가능한 모든 원소를 기준점으로 해서 사각형 만들기
for r in range(N-2):
    for c in range(1, N-1):
        dfs(r+1, c-1, 1, 0, 0)
print(min_cnt)
