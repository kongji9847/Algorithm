// ���׸�Ʈ Ʈ�� 
// -> �迭�� �ʹ� Ŭ ��(N�� �ʹ� ũ�ٸ�) ����Ѵ�.
// ���� ���� ���� ���� ����ϸ� ����.

//#define _CRT_SECURE_NO_WARNINGS
#include <iostream>

using namespace std;

const int maxN = 1'000'000;
int N, M;
long long arr[maxN];
long long tree[4 * maxN];
long long minVal = 1e9;

void input() {
	cin >> N >> M;
	for (int i = 0; i < N; i++) {
		cin >> arr[i];
	}
}


// min - tree ����� -> ��尪 ��ȯ
long long making_tree(int start, int end, int node) {
	// ��������(leaf ��忡 �������� �� -> ���̻� �Ʒ��� ������ �� ����.)
	if (start == end) {
		tree[node] = arr[start];
		return tree[node];
	}

	// ����
	int mid = (start + end) / 2;
	tree[node] = min(making_tree(start, mid, node * 2), making_tree(mid + 1, end, node * 2 + 1));
	return tree[node];
}


// �־��� ����(left, right)���� ���� ���� �� ã��
void min_arr(int start, int end, int left, int right, int node) {
	//1. ��尡 ������ ��� ��� -> �ּҰ��� ������ �� ����.
	if (end < left || start > right) {
		return;
	}
	//2. ��尡 ���� �ȿ� �ִ� ���
	else if (left <= start && end <= right) {
		minVal = min(minVal, tree[node]);
		return;
	}
	//3. ��尡 ������ �����ϰ� �ְų�, ������ ������ �ִ� ���
	else {
		int mid = (start + end) / 2;
		min_arr(start, mid, left, right, node * 2);
		min_arr(mid + 1, end, left, right, node * 2 + 1);
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
		int s, e;
		cin >> s >> e;
		minVal = 1e9;
		min_arr(0, N - 1, s - 1, e - 1, 1);
		cout << minVal << "\n";
	}


	return 0;
}