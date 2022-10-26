/*
2 ~ N-1 의 신호변경을 반영한 dijstra 돌리기 1에서 시작
K에서 시작한 dijstra 돌리기

시간초과 ---> 현재의 minVal과 비교한 백트레킹 필수!!!!!!
*/


#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <queue>
#include <cstring>

using namespace std;

struct Edge {
	int node;
	int cost;
};

struct cmp {
	bool operator()(Edge left, Edge right) {
		if (left.cost > right.cost) {
			return true;
		}
		if (left.cost < right.cost) {
			return false;
		}
		return false;
	}
};


int N, M, K;
priority_queue<Edge, vector<Edge>, cmp> minheap;
vector<Edge> adjList[40'001];

// 메인 다익스트라 도구
int dist[40'001];
int visited[40'001];

// 서브 다익스트라 도구
int visited2[40'001];
int dist2[40'001];

int minVal = 1e9;



void input() {
	cin >> N >> M >> K;

	// 배열 초기화
	memset(visited, 0, sizeof(visited));
	for (int i = 0; i <= N; i++) {
		dist[i] = 1e9;
	}


	// 인접리스트 만들기
	for (int i = 0; i < M; i++) {
		int a, b, c;
		cin >> a >> b >> c;
		adjList[a].push_back({ b, c });
		adjList[b].push_back({ a, c });
	}
}



// 서브 다익스트라 -> 임의의 숫자 k에서 start_time에 출발해서 N으로 가는 가장 최소 시간
int dijstra(int start, int start_time) {

	// 배열 초기화
	memset(visited2, 0, sizeof(visited2));
	for (int i = start + 1; i <= N; i++) {
		dist2[i] = 1e9;
	}
	priority_queue<Edge, vector<Edge>, cmp> minheap2;


	// 다익스트라 시작
	minheap2.push({ start, start_time });
	dist2[start] = start_time;


	while (!minheap2.empty()) {
		Edge now = minheap2.top();
		minheap2.pop();

		if (visited2[now.node] == 1) { continue; }

		if (minVal < now.cost) { return -1; }			// 백트레킹: 이미 minVal을 넘는 순간 의미 없다. -> 시간초과 막아줌!!!

		if (now.node == N) {
			return dist2[N];
		}

		visited2[now.node] = 1;


		for (int i = 0; i < adjList[now.node].size(); i++) {
			Edge next = adjList[now.node][i];

			// 대기 상황 고려 -> 그 now 노드에서 next로 대기 없이 갈 수 있는지 확인
			int X = (now.cost) / K;
			int new_cost;

			if (X % 2 == 1) {
				new_cost = K - ((now.cost) % K) + (next.cost + now.cost);
			}

			else {
				new_cost = (next.cost + now.cost);
			}

			if (dist2[next.node] > new_cost) {
				minheap2.push({ next.node, new_cost });
				dist2[next.node] = new_cost;
			}
		}
	}

	return dist2[N];
}





int main() {
	ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);


	//freopen_s(new FILE*, "input.txt", "r", stdin);
	input();


	// 주 다익스트라 1에서 시작 -> 대기시간이 발생한 경우, 티켓을 사용했을 때 안했을 때 따져보기
	minheap.push({ 1, 0 });
	dist[1] = 0;

	while (!minheap.empty()) {
		Edge now = minheap.top();
		minheap.pop();
		if (visited[now.node] == 1) { continue; }

		// 현재 가장 작은 누적값이 minVal보다 크다면 나머지는 보지 않아도 된다.
		if (now.cost > minVal) {
			break;
		}

		visited[now.node] = 1;


		for (int i = 0; i < adjList[now.node].size(); i++) {
			Edge next = adjList[now.node][i];


			int X = (now.cost) / K;
			int new_cost;

			// 대기시간이 발생할 때
			if (X % 2 == 1) {
				// 대기시간 있는 경우
				new_cost = K - ((now.cost) % K) + (next.cost + now.cost);
				if (dist[next.node] > new_cost) {
					minheap.push({ next.node, new_cost });
					dist[next.node] = new_cost;
				}

				// 대기시간 없다고 가정한 경우
				if (dist[next.node] > next.cost + now.cost and minVal > next.cost + now.cost) {
					int ans = dijstra(next.node, next.cost + now.cost);

					if (ans != -1) {
						minVal = min(minVal, ans);
					}
				}
			}

			// 대기 시간 없을 때
			else {
				new_cost = (next.cost + now.cost);
				if (dist[next.node] > new_cost) {
					minheap.push({ next.node, new_cost });
					dist[next.node] = new_cost;
				}
			}
		}
	}


	minVal = min(minVal, dist[N]);

	cout << minVal << "\n";

	return 0;

}