// ���׸�Ʈ Ʈ�� - ���
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


// 1. ���� �� Ʈ�� ����� -> ��Ʈ ������ �����ϱ�
// ��Ʈ ����� �ε����� 1���� ����, arr(����)�� �ε����� 0���� ����
long long making_tree(int start_arr, int end_arr, int node) {
	// �������� -> ���̻� �ɰ� �� ���� �� => start == end == mid => ���� ��忡 �������� ��
	if (start_arr == end_arr) {
		tree[node] = arr[start_arr];
		return tree[node];
	}

	// ���� -> �־��� ������ ���� �ɰ��� ���� �ڽĳ��, ������ �ڽĳ�� ���ϱ�
	int mid_arr = (start_arr + end_arr) / 2;

	tree[node] = making_tree(start_arr, mid_arr, node * 2) + making_tree(mid_arr + 1, end_arr, node * 2 + 1);
	return tree[node];
}



// 2. ���� �� ���ϱ� -> ����� start_arr, end_arr�� left - right ���� �ȿ� ���� ���� ���� �����ش�.
// return ���� �����Ͽ� ���
long long arr_sum(int start_arr, int end_arr, int left, int right, int node) {
	// ���� 1. -> ��尡 left, right �������� ��� ��� ���� ��
	if (left > end_arr || right < start_arr) {
		return 0;
	}

	// ���� 2. -> ��尡 left, right �ȿ� ���ԵǾ� ���� �� -> ���������� �������Ƿ� ��ĥ �� ����.
	if (left <= start_arr && end_arr <= right) {
		return tree[node];
	}

	// ���� 3. -> ��尡 left, right�� ������ ���� �� or ����� ������ left, right�� ������ �� 
	// -> �� ���� ���� �ڽ� ��忡�� ������ ��� ���� ã�Ƽ� ���ϱ�
	int mid = (start_arr + end_arr) / 2;
	return arr_sum(start_arr, mid, left, right, node * 2) + arr_sum(mid + 1, end_arr, left, right, node * 2 + 1);
}


// 3. update �ϱ� -> �ش� ���Ҹ� �����ϰ� �ִ� ��� ��� �����ϱ�
// ������ �Ʒ��� �������鼭 �����Ѵ�.
// start_arr, end_arr ��尡 ���� ����, update_arr ������ ������ �ε���, delta ��ȭ��, node ���� ����� tree �ε���
void arr_update(int start_arr, int end_arr, int update_arr, long long d, int node) {
	// ���� ���� -> ����� start, end �������� ������Ʈ�� ���Ұ� ��� ��� ���� ��
	if (update_arr > end_arr || update_arr < start_arr) {
		return;
	}

	// ����� ���� �ȿ� ������Ʈ�� ���Ұ� ���ԵǾ� ���� ��
	else {
		// 1) �ڽ��� �� ����
		tree[node] += d;

		// 2) ���� ������ �� �ڽ��� �ִ��� Ȯ�� -> leaf node���� Ȯ��
		if (start_arr == end_arr) { return; }

		// 3) �ڽ� ���� �������鼭 update
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