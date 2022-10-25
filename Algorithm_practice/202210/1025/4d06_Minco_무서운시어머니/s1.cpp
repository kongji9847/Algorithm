// 상하좌우로 움직일 수 있는 2차원 배열에서의 다익스트라

#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <queue>
#include <cstring>

using namespace std;

int sr, sc;
int N;
int MAP[1'000][1'000];
int dist[1'000][1'000];
int visited[1'000][1'000];

struct Node {
	int tired;
	int row, col;
};

struct cmp {
	bool operator()(Node left, Node right) {
		if (left.tired > right.tired) {
			return true;
		}
		if (left.tired < right.tired) {
			return false;
		}
		return false;
	}
};


priority_queue<Node, vector<Node>, cmp> minheap;

int dr[] = { -1, 1, 0, 0 };
int dc[] = { 0, 0, -1, 1 };

void input() {
	cin >> sr >> sc;
	cin >> N;

	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			cin >> MAP[i][j];
			dist[i][j] = 1e9;
			visited[i][j] = 0;
		}
	}


}



int main() {
	ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);

	//freopen_s(new FILE*, "input.txt", "r", stdin);
	input();

	dist[sr][sc] = MAP[sr][sc];
	minheap.push({ MAP[sr][sc], sr, sc });

	while (!minheap.empty()) {
		Node now = minheap.top();
		minheap.pop();
		if (visited[now.row][now.col] == 1) { continue; }
		visited[now.row][now.col] = 1;

		for (int d = 0; d < 4; d++) {
			int nr = now.row + dr[d];
			int nc = now.col + dc[d];

			if (0 <= nr and nr < N and 0 <= nc and nc < N) {
				if (MAP[nr][nc] != -1) {
					dist[nr][nc] = min(dist[nr][nc], dist[now.row][now.col] + MAP[nr][nc]);
					minheap.push({ dist[nr][nc], nr, nc });
				}
			}
		}
	}

	int maxVal = 0;


	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			if (dist[i][j] != 1e9) {
				maxVal = max(maxVal, dist[i][j]);
			}
		}
	}

	cout << maxVal;

	return 0;
}