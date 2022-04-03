"""
1. 기본 정보
MST의 최솟값의 합 구하기

2. 입력 정보
첫 째 줄에 마지막 노드 번호 V(0번 부터 시작)와 간선의 개수 E
다음 줄부터 E개의 줄에 걸쳐 간선의 양 끝 노드(start, end)와 가중치(w)

크루스칼
 - 간선 중심
 - 간선을 오름차순 정렬 & 간선 개수만큼 선택
 - union & find 활용하여 사이클 생성 방지
"""

# 2. 집합 함수 - kruskal에서 노드끼리 서로 어떤 경로로든 MST안에서 연결되어 있음을 표현하기 위해 사용한다.
# 2-1. 루트 찾기
def find_set(x):
    while x != nodes[x]:
        x = nodes[x]
    return x

# 2-2. 두 집합 합치기: y의 루트값을 x의 루트값으로 바꾸기
def union(x, y):
    nodes[find_set(y)] = find_set(x)


# 3. kruskal
def kruskal():
    ans = 0
    edge_cnt = 0                            # MST에 들어간 간선의 개수 count
    now_indx = 0                            # 현재 edges의 인덱스

    while edge_cnt < V:                     # 노드의 개수 : V+1, 간선의 개수 : V -> 간선의 개수가 V가 되면 중지
        w, v1, v2 = edges[now_indx]         # 현재 최소 가중치를 가진 간선 확인
        if find_set(v1) != find_set(v2):    # 간선이 MST에서 서로 연결되어 있지 않다면
            ans += w                        # 경로에 포함을 해준다.
            edge_cnt += 1
            union(v1, v2)                   # v1, v2가 MST에 들어가 서로 연결되었음을 표시
        now_indx += 1                       # 다음 인덱스 보기

    return ans


# 1. 입력 받기 & 오름차순으로 간선 가중치 정렬하기
import sys
sys.stdin = open('input.txt')
V, E = map(int, input().split())
edges = []
for _ in range(E):
    v1, v2, w = map(int, input().split())
    edges.append((w, v1, v2))
edges.sort()                                        # 가중치 기준, 오름차순으로 정렬
nodes = [i for i in range(V+1)]                     # 집합 만들기

print(kruskal())