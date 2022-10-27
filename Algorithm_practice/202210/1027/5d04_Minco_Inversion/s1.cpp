// 세그먼트 트리 - sum tree
// 값이 작은 순서대로 tree에 1을 더해 update 시켜주고, cnt를 사용해 개수 찾기
// O(2*N*logN)

// tree의 역할!
// 현재의 수보다 작은 수들이 나보다 뒤에 있는 구간에 몇 개 들어 있는지 알 수 있다.
// sort 하여 순서대로 진행하는 것이 중요하다!


//#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <queue>
#include <vector>

using namespace std;

struct Node {
	long long value;
	int index;
};

struct cmp {
	bool operator()(Node left, Node right) {
		if (left.value > right.value) {
			return true;
		}
		if (left.value < right.value) {
			return false;
		}
		return false;
	}
};


const int maxN = 1'000'000;
int N;
long long tree[maxN * 4] = { 0 };
priority_queue<Node, vector<Node>, cmp> minheap;
long long cnt = 0;


void input() {
	cin >> N;
	for (int i = 0; i < N; i++) {
		long long a;
		cin >> a;
		minheap.push({ a, i });
	}
}


// 업데이트하려는 인덱스가 범위에 포함되어 있다면 진행한다.
void update_tree(int start, int end, int update_idx, long long value, int node) {
	if (update_idx < start || end < update_idx) { return; }

	// 진행 -> 자신을 갱신하고 자식도 확인해준다.
	tree[node] += value;				// 갱신
	if (start == end) { return; }		// 자식이 없는 노드는 갱신만 해주고 끝낸다.
	int mid = (start + end) / 2;
	update_tree(start, mid, update_idx, value, node * 2);
	update_tree(mid + 1, end, update_idx, value, node * 2 + 1);
}




// 구간합 찾기
int arr_sum(int start, int end, int left, int right, int node) {
	// 1. 구간에서 벗어난 경우
	if (end < left || right < start) {
		return 0;
	}

	// 2. 구간 안에 있는 경우
	if (left <= start && end <= right) {
		return tree[node];
	}

	// 3. 구간보다 범위가 크거나, 구간에 걸쳐져 있을 때 -> 자식노드로 가서 세분화한다.
	int mid = (start + end) / 2;
	return arr_sum(start, mid, left, right, node * 2) + arr_sum(mid + 1, end, left, right, node * 2 + 1);
}


int main() {
	ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);

	//freopen_s(new FILE*, "input.txt", "r", stdin);
	input();

	while (!minheap.empty()) {
		Node now = minheap.top();
		minheap.pop();

		// 현재 값보다 작은 수가 현재 값 뒤에 있다면 누적 더해주고
		cnt += arr_sum(0, N - 1, now.index + 1, N - 1, 1);

		// 현재 값의 위치를 tree에 반영해준다.
		update_tree(0, N - 1, now.index, 1, 1);
	}

	cout << cnt;

	return 0;
}