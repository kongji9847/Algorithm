import sys
sys.stdin = open('input.txt')

# 2. prim's algorithm
def prim():
    # 간선 개수 = 노드 개수 - 1 : 모든 V+1 개의 노드에 최소 비용이 부여되려면 V번 반복하면 된다.
    # 1번 시행 -> 2개의 노드에 최솟값이 갱신된다.
    for _ in range(V):
        min_value = 987654321               # 새로운 노드를 MST에 추가하기 전에 최솟값을 초기화한다.
        min_indx = 0                        # min_indx 값 초기화

        # 1. 아직 방문하지 않은 노드 중 최소 비용의 노드 선택해서 방문 표시하기
        for i in range(V+1):
            if not visited[i] and values[i] < min_value:
                min_value = values[i]
                min_indx = i
        visited[min_indx] = 1

        # 2. 직전에 선택한 최소 비용 노드로부터 연결된 정점 가중치 갱신
        for j in range(V+1):
            if not visited[j] and graph[min_indx][j] < values[j]:
                values[j] = graph[min_indx][j]
    print(values)
    return sum(values)

# 1. 입력 받기 - graph, visited, values(최소비용 넣는 배열) 만들기
V, E = map(int, input().split())
graph = [[987654321]*(V+1) for _ in range(V+1)]                 # graph에 노드 간 연결 및 연결 비용 구하기
                                                                # 0으로 초기화하면 최솟값이 0으로 나와서 안된다. -> 임의의 큰 값으로 설정하기
for _ in range(E):
    v1, v2, w = map(int, input().split())
    graph[v1][v2] = w
    graph[v2][v1] = w
visited = [0] * (V+1)                                           # 방문 표시
values = [987654321]*(V+1)                                      # 최소 비용 갱신
values[0] = 0

print(prim())