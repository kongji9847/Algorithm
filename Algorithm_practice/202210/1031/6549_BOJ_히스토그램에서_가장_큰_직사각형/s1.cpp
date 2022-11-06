#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <queue>
#include <algorithm>
#include <cstring>

using namespace std;

struct Edge {
	long long h;
	long long id;
};

struct cmp {
	bool operator()(Edge left, Edge right) {
		if (left.h > right.h) {
			return true;
		}
		if (left.h < right.h) {
			return false;
		}
		if (left.id > right.id) {
			return true;
		}
		if (left.id < right.id) {
			return false;
		}
		return false;
	}
};


const long long maxN = 100000;
long long N = 100000;
priority_queue<Edge, vector<Edge>, cmp> minheap;
queue<Edge> samething;
long long tree[maxN * 4];
long long arr[maxN];
long long maxA = 0;


void input() {
	for (int i = 0; i < maxN * 4; i++) {
		tree[i] = N;
	}

	maxA = 0;
	tree[1] = N;

	cin >> N;
	
	for (long long i = 0; i < N; i++) {
		cin >> arr[i];
		minheap.push({ arr[i], i });
	}
}


void updating_tree(long long start, long long end, long long update_id, long long node) {
	if (update_id < start || update_id > end) {
		return;
	}

	tree[node] = min(tree[node], update_id);
	if (start == end) {
		return;
	}
	long long mid = (start + end)/2;
	updating_tree(start, mid, update_id, node * 2);
	updating_tree(mid + 1, end, update_id, node * 2 + 1);
	return;
}


long long searching_tree(long long start, long long end, long long left, long long right, long long node) {
	if (start > right || end < left) {
		return 1e9;
	}

	if (left <= start && end <= right) {
		return tree[node];
	}

	long long mid = (start + end) / 2;

	tree[node] =
		min(searching_tree(start, mid, left, right, node * 2),
			searching_tree(mid + 1, end, left, right, node * 2 + 1));
		return tree[node];
}




int main() {
	ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);

	freopen_s(new FILE*, "input.txt", "r", stdin);


	while (N != 0) {
		input();
		long long beforeEdge = minheap.top().h;
		while (!minheap.empty()) {
			Edge now = minheap.top();
			minheap.pop();

			if (beforeEdge == now.h) {
				samething.push(now);
				long long bottom = searching_tree(0, N - 1, now.id + 1, N - 1, 1);
				long long A = (bottom - now.id)*now.h;
				maxA = max(maxA, A);
			}

			else {
				beforeEdge = now.h;
				while (!samething.empty()) {
					Edge here = samething.front();
					samething.pop();
					updating_tree(0, N - 1, here.id, 1);
				}
				samething.push(now);
				long long bottom = searching_tree(0, N - 1, now.id + 1, N - 1, 1);
				long long A = (bottom - now.id) * now.h;
				maxA = max(maxA, A);
			}
		}
		cout << maxA << "\n";
	}

}