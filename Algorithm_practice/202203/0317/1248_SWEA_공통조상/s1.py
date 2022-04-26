# 2. node의 모든 조상을 찾아주는 함수
def find_p(node):
    stack = []
    while tree[node][2]:
        stack.append(tree[node][2])
        node = tree[node][2]
    return stack

# 3. 전위 탐색으로 하위 노드를 세어주는 함수
def pre_order(node):
    global cnt
    if node:
        cnt += 1
        pre_order(tree[node][0])
        pre_order(tree[node][1])

# 1. input 받기
import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    V, E, N1, N2 = map(int, input().split())
    tree = [[0, 0, 0] for _ in range(V+1)]
    data = list(map(int, input().split()))
    # tree 만들기 [왼쪽 자식, 오른쪽 자식, 부모]
    for i in range(E):
        if tree[data[i*2]][0] == 0:
            tree[data[i*2]][0] = data[i*2+1]
        else:
            tree[data[i * 2]][1] = data[i*2+1]
        tree[data[i*2+1]][2] = data[i*2]

    # 4. 결과 내기
    N1_parents = find_p(N1)
    N2_parents = find_p(N2)
    # 제일 최초로 나온 공통 조상 찾고 하위 노드 개수 세기
    for element in N1_parents:
        if element in N2_parents:
            cnt = 0
            pre_order(element)
            print(f'#{tc}', element, cnt)
            break