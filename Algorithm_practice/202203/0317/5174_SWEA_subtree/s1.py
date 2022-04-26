# 재귀함수 사용, 최대 1000까지여서 가능?
def search(N):
    global cnt
    parent = N

    if tree[parent][0]:
        cnt += 1
        search(tree[parent][0])

        if tree[parent][1]:
            cnt += 1
            search(tree[parent][1])


import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    E, N = map(int, input().split())
    V = E + 1           # 이진 트리이므로
    data = list(map(int, input().split()))
    tree = [[0, 0, 0] for _ in range(V+1)]
    for i in range(E):
        parent = data[i*2]
        child = data[i*2 + 1]
        if tree[parent][0] == 0:
            tree[parent][0] = child
        else:
            tree[parent][1] = child

        tree[child][2] = parent
    cnt = 1
    search(N)
    print(f'#{tc}', cnt)
