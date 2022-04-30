# 주의! 완전 이진 트리가 아니다.
# import sys
# sys.stdin = open('input.txt')
from collections import deque

# T = int(input())
# for tc in range(1, T+1):
N = int(input())
tree = list(map(int, input().split()))

# 1. 각 노드의 자식 노드를 담기 -> tree[자식] = 부모 -> my_children[부모].append(자식)
my_childeren = [[] for _ in range(N)]
for child in range(N):
    if tree[child] != -1:               # child 노드의 부모노드는 없다.
        my_childeren[tree[child]].append(child)

# 2. 주어진 노드를 삭제하기
erase_node = int(input())
# Q에 삭제할 자식 노드들 저장
Q = deque([erase_node])
while Q:
    parent = Q.popleft()
    for child in my_childeren[parent]:
        Q.append(child)
    my_childeren[parent] = [-1]     # 모든 자식 노드를 삭제했으면 해당 노드 [-1]로 만들기

# 3. 리프 노드 카운트
cnt = 0
for node in range(N):
    if not my_childeren[node]:      # 원래 리프 노드였던 노드
        cnt += 1
    elif my_childeren[node] == [erase_node]:        # 원래 리프노드는 아니었지만 자식 노드로 erase_node 하나만을 가져 리프 노드가 된 케이스
        cnt += 1
print(cnt)