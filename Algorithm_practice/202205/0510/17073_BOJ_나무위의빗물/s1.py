# 리프 노드 개수 세기
import sys
#sys.stdin = open('input.txt')
input = sys.stdin.readline
from collections import deque

N, W = map(int, input().split())
data = [[] for _ in range(N+1)]
tree = [[] for _ in range(N+1)]
for _ in range(N-1):
    U, V = map(int, input().split())
    data[U].append(V)
    data[V].append(U)


nodes = deque([1])
while nodes:
    node = nodes.popleft()
    for element in data[node]:
        if not tree[element]:
            tree[node].append(element)
            nodes.append(element)

leaf = 0
for i in range(1, N+1):
    if not tree[i]:
        leaf += 1

print(W/leaf)