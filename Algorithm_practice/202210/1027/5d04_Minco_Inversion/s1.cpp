// ���׸�Ʈ Ʈ�� - sum tree
// ���� ���� ������� tree�� 1�� ���� update �����ְ�, cnt�� ����� ���� ã��
// O(2*N*logN)

// tree�� ����!
// ������ ������ ���� ������ ������ �ڿ� �ִ� ������ �� �� ��� �ִ��� �� �� �ִ�.
// sort �Ͽ� ������� �����ϴ� ���� �߿��ϴ�!


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


// ������Ʈ�Ϸ��� �ε����� ������ ���ԵǾ� �ִٸ� �����Ѵ�.
void update_tree(int start, int end, int update_idx, long long value, int node) {
	if (update_idx < start || end < update_idx) { return; }

	// ���� -> �ڽ��� �����ϰ� �ڽĵ� Ȯ�����ش�.
	tree[node] += value;				// ����
	if (start == end) { return; }		// �ڽ��� ���� ���� ���Ÿ� ���ְ� ������.
	int mid = (start + end) / 2;
	update_tree(start, mid, update_idx, value, node * 2);
	update_tree(mid + 1, end, update_idx, value, node * 2 + 1);
}




// ������ ã��
int arr_sum(int start, int end, int left, int right, int node) {
	// 1. �������� ��� ���
	if (end < left || right < start) {
		return 0;
	}

	// 2. ���� �ȿ� �ִ� ���
	if (left <= start && end <= right) {
		return tree[node];
	}

	// 3. �������� ������ ũ�ų�, ������ ������ ���� �� -> �ڽĳ��� ���� ����ȭ�Ѵ�.
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

		// ���� ������ ���� ���� ���� �� �ڿ� �ִٸ� ���� �����ְ�
		cnt += arr_sum(0, N - 1, now.index + 1, N - 1, 1);

		// ���� ���� ��ġ�� tree�� �ݿ����ش�.
		update_tree(0, N - 1, now.index, 1, 1);
	}

	cout << cnt;

	return 0;
}