// 꽃이 핀 기간이므로, 변화가 있을 때마다 변화량만 저장해두고 마지막에 누적합 사용하여 dat 완성하기

#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <queue>

using namespace std;
int N, M;
int MAP[500][500] = { 0 };
int visited[500][500] = { 0 };
int sr, sc;
int dr[] = { -1, 1, 0, 0 };
int dc[] = { 0, 0, -1, 1 };
int flower_cnt[10'000'000] = { 0 };

struct FlowerLocation {
	int row, col;
	int start;
};

void input() {
	cin >> N >> M;
	for (int n = 0; n < N; n++) {
		for (int m = 0; m < M; m++) {
			cin >> MAP[n][m];
		}
	}
	cin >> sr >> sc;
}


int main() {
	ios::sync_with_stdio(false);
	cout.tie(0);
	cin.tie(0);

	//freopen_s(new FILE*, "input.txt", "r", stdin);
	input();

	queue<FlowerLocation> Q;

	int today = 0;
	Q.push({ sr, sc, 1 });
	visited[sr][sc] = 1;

	while (!Q.empty()) {
		FlowerLocation now = Q.front();
		Q.pop();
		flower_cnt[now.start] += 1;
		flower_cnt[now.start + MAP[now.row][now.col]] -= 1;


		for (int d = 0; d < 4; d++) {
			int nr = now.row + dr[d];
			int nc = now.col + dc[d];

			if (0 <= nr and nr < N and 0 <= nc and nc < M) {
				if (MAP[nr][nc] != 0 and !visited[nr][nc]) {
					visited[nr][nc] = 1;
					Q.push({ nr, nc, now.start + 1 });
				}
			}

		}
	}
	int maxVal = 0;
	int maxDay = 0;

	for (int day = 1; day < 10'000'000; day++) {
		flower_cnt[day] += flower_cnt[day - 1];
		if (maxVal < flower_cnt[day]) {
			maxVal = flower_cnt[day];
			maxDay = day;
		}
	}

	cout << maxDay << "일" << "\n";
	cout << maxVal << "개" << "\n";

	return 0;
}