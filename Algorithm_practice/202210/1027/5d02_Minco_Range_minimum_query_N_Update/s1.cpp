// 세그먼트 트리 -> 배열이 너무 클 때(N이 너무 크다면) 사용한다.
// #define _CRT_SECURE_NO_WARNINGS
#include <iostream>

using namespace std;

const int maxN = 1'000'000;
int N, M;
long long arr[maxN];
long long tree[4 * maxN];
long long minVal = 1e9;

void input() {
	cin >> N;
	for (int i = 0; i < N; i++) {
		cin >> arr[i];
	}
	cin >> M;
}


// min - tree 만들기 -> 노드값 반환
long long making_tree(int start, int end, int node) {
	// 종료조건(leaf 노드에 도달했을 때 -> 더이상 아래로 내려갈 수 없다.)
	if (start == end) {
		tree[node] = arr[start];
		return tree[node];
	}

	// 진행
	int mid = (start + end) / 2;
	tree[node] = min(making_tree(start, mid, node * 2), making_tree(mid + 1, end, node * 2 + 1));
	return tree[node];
}


// 주어진 구간(left, right)에서 가장 작은 수 찾기
void min_arr(int start, int end, int left, int right, int node) {
	//1. 노드가 구간을 벗어난 경우 -> 최소값을 갱신할 수 없다.
	if (end < left || start > right) {
		return;
	}
	//2. 노드가 구간 안에 있는 경우
	else if (left <= start && end <= right) {
		minVal = min(minVal, tree[node]);
		return;
	}
	//3. 노드가 구간을 포함하고 있거나, 구간에 걸쳐져 있는 경우
	else {
		int mid = (start + end) / 2;
		min_arr(start, mid, left, right, node * 2);
		min_arr(mid + 1, end, left, right, node * 2 + 1);
		return;
	}
}


// update_id를 포함하는 노드 변경하기
void update_arr(int start, int end, int update_id, long long value, int node) {
	// 포함하지 않는 경우
	if (update_id < start || update_id > end) {
		return;
	}

	else {
		// 1. leaf 노드라면 -> update 된 본인이라면 중지
		if (start == end) {
			tree[node] = arr[update_id];
			return;
		}

		int mid = (start + end) / 2;
		update_arr(start, mid, update_id, value, node * 2);
		update_arr(mid + 1, end, update_id, value, node * 2 + 1);

		tree[node] = min(tree[node * 2], tree[node * 2 + 1]);

		return;
	}
}



int main() {
	ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);

	//freopen_s(new FILE*, "input.txt", "r", stdin);
	input();
	making_tree(0, N - 1, 1);

	for (int q = 0; q < M; q++) {
		int type;
		cin >> type;

		if (type == 1) {
			int a;
			long long b;
			cin >> a >> b;

			long long original = arr[a - 1];
			arr[a - 1] = b;
			update_arr(0, N - 1, a - 1, b, 1);
		}

		else {
			int s, e;
			cin >> s >> e;
			minVal = 1e9;
			min_arr(0, N - 1, s - 1, e - 1, 1);
			cout << minVal << "\n";
		}
	}


	return 0;
}