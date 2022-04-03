"""
1. 기본 정보
MST의 최솟값의 합 구하기

2. 입력 정보
첫 째 줄에 마지막 노드 번호 V(0번 부터 시작)와 간선의 개수 E
다음 줄부터 E개의 줄에 걸쳐 간선의 양 끝 노드(start, end)와 가중치(w)

프림
 - 정점 중심 (임의의 정점을 잡고 시작)
 - 정점과 인접하는 정점 중에서 최소 비용의 간선이 존재하는 정점 선택
 - 계속 가중치가 최소인 정점을 연결해가며 최종적으로 연결된 배열의 합

heap 활용하면 최솟값을 찾는 과정 생략 가능
 - min_heap을 구하면 root는 항상 최소 가중치 위치
 - heap_pop을 할 때마다 root에 있는 최소 가중치 반환
"""
# 2. 최소 힙 구조 이용해서 prim 함수 만들기
import heapq
def prim():
    # 1. 최소 힙구조 만들고, 0번 노드에서 시작하기
    ans = 0
    heap = []
    heapq.heappush(heap, (0, 0))                    # (0 : 가중치, 0 : 노드 번호)

    # 2. heap에 추가된 모든 노드를 확인할 때까지 반복
    while heap:
        w, v = heapq.heappop(heap)                  # heap에서 현재 루트(최소값)를 뽑고
        if not visited[v]:                          # 이미 MST에 포함되어 있는지 확인한다.
            visited[v] = 1                          # MST에 포함되어 있지 않다면 포함 표시를 하고
            ans += w                                # 가중치를 누적합 해준다.

            for vv, ww in graph[v]:                 # 최근에 MST에 추가한 v번 노드와 인접한 노드들을 확인한다.
                if not visited[vv]:                 # MST에 포함되어 있지 않다면 heap에 포함시켜준다.
                    heapq.heappush(heap, (ww, vv))

    return ans


# 1. input 받기
import sys
sys.stdin = open('input.txt')

V, E = map(int, input().split())                    # 0부터 V번 까지의 V+1 개의 노드
graph = [[] for _ in range(V+1)]                    # 인접 리스트 만들기
for _ in range(E):
    v1, v2, w = map(int, input().split())
    graph[v1].append((v2, w))
    graph[v2].append((v1, w))

visited = [0]*(V+1)                                 # MST에 포함 여부 체크
print(prim())