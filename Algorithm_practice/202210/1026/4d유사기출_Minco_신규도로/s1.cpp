// �ּҰ��� ���ŵǾ��� ���� �ּ� ���� �־��ֱ�!! -> ���ŵ��� �ʾ��� ���� ������� -> ���ŵ��� ���� ���� �̹� heap �ȿ� �� �ִ�.

#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <queue>
#include <vector>
#include <cstring>

using namespace std;

int T;
int N, M;
int visited[50001];
int dist1[50001];
int dist2[50001];

struct Edge {
	int node;
	int value;
};

struct cmp {
	bool operator()(Edge left, Edge right) {
		if (left.value > right.value) {
			return true;
		}
		if (left.value < right.value) {
			return false;
		}
		return false;
	}
};

vector<Edge> adjList[50'001];



void input(int tc) {
	cin >> N >> M;

	if (tc >= 2) {
		for (int i = 0; i <= N; i++) {
			adjList[i].clear();
		}
	}

	for (int n = 0; n <= N; n++) {
		dist1[n] = 1e9;
		dist2[n] = 1e9;
	}

	// ��������Ʈ �����
	for (int i = 0; i < M; i++) {
		int a, b, c;
		cin >> a >> b >> c;
		adjList[a].push_back({ b, c });
		adjList[b].push_back({ a, c });
	}
}



void dijstra(int start, int type) {
	memset(visited, 0, sizeof(visited));
	priority_queue<Edge, vector<Edge>, cmp> minheap;

	if (type == 1) {
		minheap.push({ start, 0 });
		dist1[start] = 0;

		while (!minheap.empty()) {
			Edge now = minheap.top();
			minheap.pop();
			if (visited[now.node] == 1) { continue; }
			visited[now.node] = 1;

			for (int i = 0; i < adjList[now.node].size(); i++) {
				Edge next = adjList[now.node][i];
				if (dist1[next.node] > next.value + now.value) {
					dist1[next.node] = next.value + now.value;
					minheap.push({ next.node, dist1[next.node] });
				}
			}
		}
	}

	else {
		minheap.push({ start, 0 });
		dist2[start] = 0;

		while (!minheap.empty()) {
			Edge now = minheap.top();
			minheap.pop();
			if (visited[now.node] == 1) { continue; }
			visited[now.node] = 1;

			for (int i = 0; i < adjList[now.node].size(); i++) {
				Edge next = adjList[now.node][i];
				if (dist2[next.node] > next.value + now.value) {
					dist2[next.node] = next.value + now.value;
					minheap.push({ next.node, dist2[next.node] });
				}
			}
		}
	}

}


int main() {
	ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);

	//freopen_s(new FILE*, "input.txt", "r", stdin);

	cin >> T;
	for (int tc = 1; tc <= T; tc++) {
		input(tc);
		dijstra(1, 1);
		dijstra(N, 2);

		int original = dist1[N];
		int cnt = 0;


		// �뼱�� ������̰�, �ִܰŸ��� ������ �� �ִ� ���� ã���� �����Ƿ�
		// 1 - edge1 - edge2 - N���� �ִܰŸ��� ���ŵǰų�, 1 - edge2 - edge1 - N���� ���ŵȴ�.
		// �� ���� ���ÿ� ���� �� �����Ƿ� -> if if�� �ƴ϶� if else if�� ����Ѵ�. -> �ð��ʰ� �ذ�

		for (int i = 2; i < N; i++) {
			for (int j = i + 1; j < N; j++) {
				if (original > 1 + dist1[i] + dist2[j]) {
					cnt += 1;
				}
				else if (original > 1 + dist1[j] + dist2[i]) {
					cnt += 1;
				}
			}
		}

		cout << "#" << tc << " " << cnt << "\n";
	}


	return 0;
}