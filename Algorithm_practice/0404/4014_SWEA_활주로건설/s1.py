import sys
sys.stdin = open('input.txt')

def solution():
    ans = 0
    for r in range(N):
        now = data[r][0]
        check = []
        visited = [0]*N
        for c in range(1, N):
            if data[r][c] == now -1:
                check.append([(r, c), -1])
            elif data[r][c] == now + 1:
                check.append([(r, c), 1])
            now = data[r][c]

        for i in range(len(check)):
            (r, c), pos = check[i]






T = int(input())
for tc in range(1, T+1):
    N, X = map(int, input())
    data = [list(map(int, input().split())) for _ in range(N)]
    #check = [[0]*N for _ in range(2*N)]