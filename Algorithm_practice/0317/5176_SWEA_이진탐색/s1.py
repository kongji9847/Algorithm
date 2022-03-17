# 중위 탐색
def in_order(node):
    global cnt
    # 어차피 1에서 시작하니까 그 위로 올라가진 않는다.
    if node <= N:
        in_order(node * 2)
        tree[node] = cnt
        cnt += 1
        in_order(node * 2 + 1)

import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    tree = [0] * (N + 1)
    cnt = 1
    in_order(1)
    print(f'#{tc}', tree[1], tree[N//2])