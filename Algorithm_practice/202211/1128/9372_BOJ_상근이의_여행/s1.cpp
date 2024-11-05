// MST(�ּҽ���Ʈ��) Ư¡ �̿�
// MST�� ������ ������ N-1�̴�.

#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <vector>
#include <cstring>
using namespace std;

vector<int> roads[1001];
int visited[1001];


void input(int M) {
	// ������ �ʱ�ȭ
	for (int i = 0; i < 1001; i++) {
		roads[i] = {};
	}
	memset(visited, 0, sizeof(visited));

	// input ������ �ޱ�
	for (int m = 0; m < M; m++) {
		int node1, node2;
		cin >> node1 >> node2;

		roads[node1].push_back(node2);
		roads[node2].push_back(node1);
	}
}


int main() {
	ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);

	freopen_s(new FILE*, "input.txt", "r", stdin);

	int T;
	cin >> T;
	for (int tc = 1; tc <= T; tc++) {
		int N, M;
		cin >> N >> M;

		input(M);
		cout << N - 1 << "\n";
		
	}

	return 0;
}