# 리프 노드 개수 세기
import sys
#sys.stdin = open('input.txt')
input = sys.stdin.readline
from collections import deque

# 1. 연결 노드
N, W = map(int, input().split())
data = [[] for _ in range(N+1)]
for _ in range(N-1):
    U, V = map(int, input().split())
    data[U].append(V)
    data[V].append(U)

# 2. 1번 노드부터 자식노드를 탐색하며 트리 구조 만들고 leaf 개수 세기
# -> bfs 활용: 위에서부터 내려가야하니까 dfs가 아닌 bfs를 활용
tree = [[] for _ in range(N+1)]
nodes = deque([1])
leaf = N

while nodes:
    node = nodes.popleft()                          # 노드를 하나씩 확인한다.
    flag = 0
    for element in data[node]:                      # 해당 노드와 연결된 element들을 모두 확인하는데,
        if not tree[element]:                       # 이미 등록된 부모 노드가 아닌 element라면
            tree[node].append(element)              # 트리 구조에 추가해준다.
            nodes.append(element)                   # 추후 자식 노드를 탐색할 노드 리스트(nodes)에도 넣어준다
            flag = 1                                # 해당 노드는 이미 leaf가 아니라는 뜻

    leaf -= flag                                    # if 문을 쓰지 않고도 해결 가능

print(W/leaf)