import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    # 노드 개수, 리프 노드 개수, 출력할 노드번호
    V, M, L = map(int, input().split())
    tree = [0] * (V+1)

    for i in range(M):
        num, value = map(int, input().split())
        tree[num] = value

    j = V
    while j != L:
        tree[j//2] += tree[j]
        j -= 1

    print(f'#{tc}', tree[j])