// dat 사용하여 탐색 - N이 크므로 3중 이상의 for문 돌리면 시간초과 난다.

#include<iostream>
#include<string>

using namespace std;


// 땅 입력받기
int MAP[1000][1000];

int H, W;

int blackList[1000][1000];
int bH, bW;

int dat[100001];

void input() {
	cin >> H >> W;

	for (int r = 0; r < H; r++) {
		for (int c = 0; c < W; c++) {
			cin >> MAP[r][c];
		}
	}

	cin >> bH >> bW;
	for (int r = 0; r < bH; r++) {
		for (int c = 0; c < bW; c++) {
			cin >> blackList[r][c];
			dat[blackList[r][c]] = 1;
		}
	}
}


int isSame(int target) {
	if (dat[target] == 1) {
		return 1;
	}
	return 0;
}

int main() {

	ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	input();

	int cnt = 0;

	for (int r = 0; r < H; r++) {
		for (int c = 0; c < W; c++) {
			int ret = isSame(MAP[r][c]);
			if (ret == 1) {
				cnt += 1;
			}
		}
	}
	cout << cnt << "\n";
	cout << H * W - cnt;


	return 0;
}