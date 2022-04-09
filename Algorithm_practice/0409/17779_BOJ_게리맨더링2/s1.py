# import sys
# sys.stdin = open('input.txt')


delta = [(1, -1), (1, 1), (-1, 1), (-1, -1)]
def check(sr, sc, d1, d2):
    nr = sr + delta[2][0] * d1
    nc = sc + delta[2][1] * d1
    if not (0 <= nr < N and 0 <= nc < N):
        return False
    else:
        nnr = nr + delta[3][0] * d2
        nnc = nc + delta[3][1] * d2
        if nnr == r and nnc == c:
            return True

    return False


def count_people(x, y, d1, d2):
    visited = [[0]*(N) for _ in range(N)]
    visited[x][y] = 5
    nr, nc = x, y
    for i in range(4):
        if i == 0 or i == 2:
            j = d1
            while j:
                nr += delta[i][0]
                nc += delta[i][1]
                visited[nr][nc] = 5
                j -= 1
        if i == 1 or i == 3:
            j = d2
            while j:
                nr += delta[i][0]
                nc += delta[i][1]
                visited[nr][nc] = 5
                j -= 1

    for r in range(N):
        if visited[r].count(5) == 2:
            start = visited[r].index(5)
            start += 1
            while visited[r][start] != 5:
                visited[r][start] = 5
                start += 1

    people_dict = {1:0, 2:0, 3:0, 4:0, 5:total}
    for rr in range(N):
        for cc in range(N):
            if 0 <= rr < x+d1 and 0 <= cc <= y and not visited[rr][cc]:
                people_dict[1] += data[rr][cc]
                people_dict[5] -= data[rr][cc]
                visited[rr][cc] = 1
            elif 0 <= rr <= x+d2 and y < cc <= N-1 and not visited[rr][cc]:
                people_dict[2] += data[rr][cc]
                people_dict[5] -= data[rr][cc]
                visited[rr][cc] = 2
            elif x+d1 <= rr <= N-1 and 0 <= cc < y-d1+d2 and not visited[rr][cc]:
                people_dict[3] += data[rr][cc]
                people_dict[5] -= data[rr][cc]
                visited[rr][cc] = 3
            elif x+d2 < rr <= N-1 and y-d1+d2 <= cc <= N-1 and not visited[rr][cc]:
                people_dict[4] += data[rr][cc]
                people_dict[5] -= data[rr][cc]
                visited[rr][cc] = 4

    ans = max(people_dict.values()) - min(people_dict.values())
    #if x == 2 and y == 4 and d1 == 2 and d2 == 1:
        #print(visited)
    return ans


def dfs(sr, sc, d1, d2, dr):
    global min_cnt
    # 종료조건
    if dr == 2:
        if check(sr, sc, d1, d2):
            ans = count_people(r, c, d1, d2)
            #print(r, c, d1, d2, ans)
            min_cnt = min(ans, min_cnt)
        return
    # 진행
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




# T = int(input())
# for tc in range(1, T+1):

N = int(input())
data = [list(map(int, input().split())) for _ in range(N)]
total = 0
for i in range(N):
    total += sum(data[i])

min_cnt = 987654321
for r in range(N-2):
    for c in range(1, N-1):
        dfs(r+1, c-1, 1, 0, 0)

print(min_cnt)
