/*
2 ~ N-1 �� ��ȣ������ �ݿ��� dijstra ������ 1���� ����
K���� ������ dijstra ������

�ð��ʰ� ---> ������ minVal�� ���� ��Ʈ��ŷ �ʼ�!!!!!!
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

// ���� ���ͽ�Ʈ�� ����
int dist[40'001];
int visited[40'001];

// ���� ���ͽ�Ʈ�� ����
int visited2[40'001];
int dist2[40'001];

int minVal = 1e9;



void input() {
	cin >> N >> M >> K;

	// �迭 �ʱ�ȭ
	memset(visited, 0, sizeof(visited));
	for (int i = 0; i <= N; i++) {
		dist[i] = 1e9;
	}


	// ��������Ʈ �����
	for (int i = 0; i < M; i++) {
		int a, b, c;
		cin >> a >> b >> c;
		adjList[a].push_back({ b, c });
		adjList[b].push_back({ a, c });
	}
}



// ���� ���ͽ�Ʈ�� -> ������ ���� k���� start_time�� ����ؼ� N���� ���� ���� �ּ� �ð�
int dijstra(int start, int start_time) {

	// �迭 �ʱ�ȭ
	memset(visited2, 0, sizeof(visited2));
	for (int i = start + 1; i <= N; i++) {
		dist2[i] = 1e9;
	}
	priority_queue<Edge, vector<Edge>, cmp> minheap2;


	// ���ͽ�Ʈ�� ����
	minheap2.push({ start, start_time });
	dist2[start] = start_time;


	while (!minheap2.empty()) {
		Edge now = minheap2.top();
		minheap2.pop();

		if (visited2[now.node] == 1) { continue; }

		if (minVal < now.cost) { return -1; }			// ��Ʈ��ŷ: �̹� minVal�� �Ѵ� ���� �ǹ� ����. -> �ð��ʰ� ������!!!

		if (now.node == N) {
			return dist2[N];
		}

		visited2[now.node] = 1;


		for (int i = 0; i < adjList[now.node].size(); i++) {
			Edge next = adjList[now.node][i];

			// ��� ��Ȳ ��� -> �� now ��忡�� next�� ��� ���� �� �� �ִ��� Ȯ��
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


	// �� ���ͽ�Ʈ�� 1���� ���� -> ���ð��� �߻��� ���, Ƽ���� ������� �� ������ �� ��������
	minheap.push({ 1, 0 });
	dist[1] = 0;

	while (!minheap.empty()) {
		Edge now = minheap.top();
		minheap.pop();
		if (visited[now.node] == 1) { continue; }

		// ���� ���� ���� �������� minVal���� ũ�ٸ� �������� ���� �ʾƵ� �ȴ�.
		if (now.cost > minVal) {
			break;
		}

		visited[now.node] = 1;


		for (int i = 0; i < adjList[now.node].size(); i++) {
			Edge next = adjList[now.node][i];


			int X = (now.cost) / K;
			int new_cost;

			// ���ð��� �߻��� ��
			if (X % 2 == 1) {
				// ���ð� �ִ� ���
				new_cost = K - ((now.cost) % K) + (next.cost + now.cost);
				if (dist[next.node] > new_cost) {
					minheap.push({ next.node, new_cost });
					dist[next.node] = new_cost;
				}

				// ���ð� ���ٰ� ������ ���
				if (dist[next.node] > next.cost + now.cost and minVal > next.cost + now.cost) {
					int ans = dijstra(next.node, next.cost + now.cost);

					if (ans != -1) {
						minVal = min(minVal, ans);
					}
				}
			}

			// ��� �ð� ���� ��
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