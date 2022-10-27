// 세그먼트 트리 - 재귀
//#define _CRT_SECURE_NO_WARNINGS

# include <iostream>
# include <vector>

using namespace std;

const int maxN = 1'000'000;
int N, Q;
long long arr[maxN];
long long tree[4 * maxN] = { 0 };

void input() {
	cin >> N >> Q;
	for (int i = 0; i < N; i++) {
		cin >> arr[i];
	}
}


// 1. 구간 합 트리 만들기 -> 루트 노드부터 시작하기
// 루트 노드의 인덱스는 1부터 시작, arr(구간)의 인덱스는 0부터 시작
long long making_tree(int start_arr, int end_arr, int node) {
	// 종료조건 -> 더이상 쪼갤 수 없을 때 => start == end == mid => 리프 노드에 도달했을 때
	if (start_arr == end_arr) {
		tree[node] = arr[start_arr];
		return tree[node];
	}

	// 진행 -> 주어진 구간의 반을 쪼개서 왼쪽 자식노드, 오른쪽 자식노드 더하기
	int mid_arr = (start_arr + end_arr) / 2;

	tree[node] = making_tree(start_arr, mid_arr, node * 2) + making_tree(mid_arr + 1, end_arr, node * 2 + 1);
	return tree[node];
}



// 2. 구간 합 구하기 -> 노드의 start_arr, end_arr가 left - right 범위 안에 있을 때만 합을 구해준다.
// return 값을 누적하여 계산
long long arr_sum(int start_arr, int end_arr, int left, int right, int node) {
	// 조건 1. -> 노드가 left, right 범위에서 모두 벗어나 있을 때
	if (left > end_arr || right < start_arr) {
		return 0;
	}

	// 조건 2. -> 노드가 left, right 안에 포함되어 있을 때 -> 위에서부터 내려가므로 겹칠 일 없다.
	if (left <= start_arr && end_arr <= right) {
		return tree[node];
	}

	// 조건 3. -> 노드가 left, right에 걸쳐져 있을 때 or 노드의 범위가 left, right를 포함할 때 
	// -> 두 개로 나뉜 자식 노드에서 가능한 노드 값을 찾아서 더하기
	int mid = (start_arr + end_arr) / 2;
	return arr_sum(start_arr, mid, left, right, node * 2) + arr_sum(mid + 1, end_arr, left, right, node * 2 + 1);
}


// 3. update 하기 -> 해당 원소를 포함하고 있는 모든 노드 수정하기
// 위에서 아래로 내려가면서 갱신한다.
// start_arr, end_arr 노드가 가진 구간, update_arr 변경할 구간의 인덱스, delta 변화량, node 현재 노드의 tree 인덱스
void arr_update(int start_arr, int end_arr, int update_arr, long long d, int node) {
	// 종료 조건 -> 노드의 start, end 범위에서 업데이트할 원소가 모두 벗어나 있을 때
	if (update_arr > end_arr || update_arr < start_arr) {
		return;
	}

	// 노드의 범위 안에 업데이트할 원소가 포함되어 있을 때
	else {
		// 1) 자신의 값 갱신
		tree[node] += d;

		// 2) 값을 갱신한 후 자식이 있는지 확인 -> leaf node인지 확인
		if (start_arr == end_arr) { return; }

		// 3) 자식 노드로 내려가면서 update
		int mid = (start_arr + end_arr) / 2;
		arr_update(start_arr, mid, update_arr, d, node * 2);
		arr_update(mid + 1, end_arr, update_arr, d, node * 2 + 1);
	}

}


int main() {
	ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);

	//freopen_s(new FILE*, "input.txt", "r", stdin);

	input();
	making_tree(0, N - 1, 1);

	for (int q = 0; q < Q; q++) {
		int type, a;
		long long b;
		cin >> type >> a >> b;

		if (type == 1) {
			long long original = arr[a - 1];
			arr[a - 1] = b;
			arr_update(0, N - 1, a - 1, b - original, 1);
		}

		else if (type == 2) {
			cout << arr_sum(0, N - 1, a - 1, b - 1, 1) << "\n";
		}
	}
	return 0;
}