# 색칠 가능한 모든 경우를 다 살펴본다.
import sys
sys.stdin = open('input.txt')

def Russia(N, M, arr):
    # W, B, R 순으로 색칠하려고 할 때, 색칠해야하는 칸 수
    stack = [[M, M, M] for _ in range(N)]
    for r in range(N):
        for c in range(M):
            if arr[r][c] == 'W':
                stack[r][0] -= 1
            elif arr[r][c] == 'B':
                stack[r][1] -= 1
            elif arr[r][c] == 'R':
                stack[r][2] -= 1

    min_sum = N*M                       # 색칠가능한 최대 칸의 개수를 최소로 설정
    for nb in range(1, N-1):            # 파란색이 한 줄일 때, 파란색으로 색칠할 행 선택하기
        cnt = stack[nb][1]
        for nw in range(1, nb):         # 흰색, 빨강색은 파란색을 기준으로 색칠하기
            cnt += stack[nw][0]
        for nr in range(nb+1, N-1):
            cnt += stack[nr][2]
        if min_sum > cnt:               # 다른 경우로 가기 전에 최소값인지 확인하기
            min_sum = cnt

    for nbs in range(1, N-1):                       # 파란색이 2줄 이상일 때, 파란색의 시작 행 고르기
        for nbe in range(nbs+1, N-1):               # 파란색의 끝 행 고르기
            cnt = 0                                 # 새로운 경우를 시작할 때 cnt 초기화
            for b in range(nbs, nbe+1):             # 파란색으로 색칠하는 칸 수
                cnt += stack[b][1]
            for ww in range(1, nbs):                # 하얀색
                cnt += stack[ww][0]
            for rr in range(nbe+1, N-1):            # 빨강색
                cnt += stack[rr][2]
            if min_sum > cnt:
                min_sum = cnt

    return min_sum + stack[0][0] + stack[-1][2]     # 맨 첫 줄과 맨 끝 줄은 각각 하얀색, 빨간색으로 색칠한다.

T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    arry = [input() for _ in range(n)]
    print('#{} {}'.format(tc, Russia(n, m, arry)))