/*
'나'는 탈출구까지 무조건 최단 거리로 가야한다.
유령을 피해 '나'가 왔다 갔다하며 지난 턴에 갔던 곳으로 다시 갈 수 없다.
turn이 늘어날 수록 유령이 갈 수 있는 곳은 많아진다. 동선이 길수록 잡힐 수 밖에 없게 된다.

시간초과 해결
이전 turn에 갈 수 있던 곳은 지금 turn에는 들릴수 없다.
최단 거리를 가려고 할 때, 해당 칸은 n번째 턴에서만 갈 수 있다.
*/


#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <string>
#include <cstring>
#include <queue>

using namespace std;

int dr[] = { -1, 1, 0, 0 };
int dc[] = { 0, 0, -1, 1 };

int T;
int N, M;
string MAP[100];

int sr, sc;
int monster_cnt;
int isMonster[100][100];
int isMe[100][100];

struct Location {
	int row, col;
	int distance;
};

queue<Location> myQ;
queue<Location> monsterQ;


void input() {
	// 큐 비우기
	myQ = queue<Location>();
	monsterQ = queue<Location>();

	memset(isMonster, 0, sizeof(isMonster));
	memset(isMe, 0, sizeof(isMe));

	cin >> N >> M;

	for (int n = 0; n < N; n++) {
		cin >> MAP[n];

		for (int m = 0; m < M; m++) {
			if (MAP[n][m] == 'S') {
				sr = n;
				sc = m;
				myQ.push({ n, m, 0 });
			}

			else if (MAP[n][m] == 'C') {
				monsterQ.push({ n, m, 0 });
			}
		}
	}
}

void isMonsterHere(int now_distance) {

	// 몬스터가 없는 경우
	if (monsterQ.empty()) {
		return;
	}

	while (!monsterQ.empty()) {
		Location monster = monsterQ.front();
		if (monster.distance != now_distance) {
			break;
		}

		monsterQ.pop();

		for (int d = 0; d < 4; d++) {
			int mr = monster.row + dr[d];
			int mc = monster.col + dc[d];
			if (0 <= mr and mr < N and 0 <= mc and mc < M and MAP[mr][mc] != '#' and isMonster[mr][mc] != now_distance + 1) {
				monsterQ.push({ mr, mc, now_distance + 1 });
				isMonster[mr][mc] = now_distance + 1;
			}
		}
	}
}

int bfs(int tc) {
	int dist = -1;
	while (!myQ.empty()) {

		Location now = myQ.front();
		myQ.pop();

		// 턴이 바뀔때, monster 먼저 이동
		if (now.distance != dist) {
			isMonsterHere(now.distance);
			dist = now.distance;
		}

		// 턴을 진행하며 4개의 방향 보기
		for (int d = 0; d < 4; d++) {
			int nr = now.row + dr[d];
			int nc = now.col + dc[d];

			if (0 <= nr and nr < N and 0 <= nc and nc < M) {
				if (MAP[nr][nc] == '.' or MAP[nr][nc] == 'C') {
					if (isMonster[nr][nc] != (now.distance + 1) and isMe[nr][nc] == 0) {
						isMe[nr][nc] = now.distance + 1;
						myQ.push({ nr, nc, now.distance + 1 });
					}
				}

				else if (MAP[nr][nc] == 'E') {
					if (isMonster[nr][nc] != (now.distance + 1)) {
						cout << "#" << tc << " " << now.distance + 1 << "\n";
						return 1;
					}
				}
			}
		}
	}

	cout << "#" << tc << " " << -1 << "\n";
	return 0;
}

int main() {
	ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);

	//freopen_s(new FILE*, "input.txt", "r", stdin);
	cin >> T;

	for (int tc = 1; tc <= T; tc++) {
		input();
		bfs(tc);
		/*
		if (tc == 10) {
			break;
		}
		*/
	}

	return 0;
}