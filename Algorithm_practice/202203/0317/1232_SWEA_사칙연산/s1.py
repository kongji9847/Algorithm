# 후위 연산하기 -> 가장 말단에서 시작해야 되기 때문에!
def post_order(node):
    if node:
        post_order(tree[node][1])
        post_order(tree[node][2])

        # 연산자가 나오면 필요한 연산을 해서 현재 노드에 저장해주기
        L = tree[node][1]
        R = tree[node][2]
        if tree[node][0] == '+':
            tree[node][0] = (tree[L][0] + tree[R][0])
        elif tree[node][0] == '-':
            tree[node][0] = (tree[L][0] - tree[R][0])
        elif tree[node][0] == '/':
            tree[node][0] = (tree[L][0] / tree[R][0])
        elif tree[node][0] == '*':
            tree[node][0] = (tree[L][0] * tree[R][0])

import sys
sys.stdin = open('input.txt')

T = 10
for tc in range(1, T+1):
    V = int(input())
    tree = [[0, 0, 0] for _ in range(V+1)]

    for _ in range(V):
        info = input().split()
        indx = int(info[0])
        if info[1] not in ['+', '-', '*', '/']:
            tree[indx][0] = int(info[1])
        else:
            tree[indx][0] = info[1]
            tree[indx][1] = int(info[2])
            tree[indx][2] = int(info[3])

    post_order(1)
    print(f'#{tc}', int(tree[1][0]))
