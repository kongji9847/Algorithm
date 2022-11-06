// 다음 tc를 위해 꼭 큐 비우기!
/*
***세그먼트 트리 사용****

0. 사각형을 높이 순서대로 pq에 넣기
1. 기준 사각형을 중심으로 왼쪽범위와 오른쪽 범위에 기준보다 작은 사각형의 id 찾기(segment Tree)
2. 기준 사각형의 위치를 leftTree, rightTree에 넣어주기 -> leftTree는 가장 오른쪽 id값 / rightTree는 가장 왼쪽 id값

=> 작은 높이 순서대로 해야 다음 사각형이 멈출 구간이 보인다.
*/

#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <queue>
#include <cstring>
#include <algorithm>

using namespace std;

const long long maxN = 100000;
long long N;

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
		return false;
	}
};

priority_queue<Edge, vector<Edge>, cmp> minheap;
queue<Edge> sameheap;

long long leftTree[maxN * 4];
long long rightTree[maxN * 4];

long long maxA;

void input() {
	while (!sameheap.empty()) {
		sameheap.pop();
	}
	long long H;
	for (long long i = 0; i < maxN*4; i++) {
		leftTree[i] = 0;
		rightTree[i] = N;
	}

	for (long long i = 0; i < N; i++) {
		cin >> H;
		minheap.push({ H, i });
	}

	maxA = 0;
}

void update_leftTree(long long start, long long end, long long update_id, long long node) {
	if (update_id < start || update_id > end) {
		return;
	}

	leftTree[node] = max(leftTree[node], update_id+1);
	
	if (start == end) {
		return;
	}

	long long mid = (start + end) / 2;
	update_leftTree(start, mid, update_id, node*2);
	update_leftTree(mid + 1, end, update_id, node * 2 + 1);
}

void update_rightTree(long long start, long long end, long long update_id, long long node) {
	if (update_id < start || update_id > end) {
		return;
	}

	rightTree[node] = min(rightTree[node], update_id);
	if (start == end) {
		return;
	}
	long long mid = (start + end) / 2;
	update_rightTree(start, mid, update_id, node * 2);
	update_rightTree(mid + 1, end, update_id, node * 2 + 1);
}

long long search_leftTree(long long start, long long end, long long left, long long right, long long node) {
	if (left > right) {
		return 0;
	}
	
	if (end < left || start > right) {
		return 0;
	}

	if (left <= start && end <= right) {
		return leftTree[node];
	}

	long long mid = (start + end) / 2;
	long long leftBig = search_leftTree(start, mid, left, right, node * 2);
	long long rightBig = search_leftTree(mid+1, end, left, right, node * 2+1);
	return max(leftBig, rightBig);
}

long long search_rightTree(long long start, long long end, long long left, long long right, long long node) {
	if (left > right) {
		return N;
	}

	if (end < left || start > right) {
		return N;
	}

	if (left <= start && end <= right) {
		return rightTree[node];
	}

	long long mid = (start + end) / 2;
	long long leftsmall = search_rightTree(start, mid, left, right, node * 2);
	long long rightsmall = search_rightTree(mid + 1, end, left, right, node * 2 + 1);
	return min(leftsmall, rightsmall);
}




int main() {
	ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);

	freopen_s(new FILE*, "input.txt", "r", stdin);

	while (true) {
		cin >> N;
		if (N == 0) { break; }
		input();
		long long flag = minheap.top().h;


		while (!minheap.empty()) {
			Edge now = minheap.top();
			minheap.pop();

			if (now.h == flag) {
				long long leftEdge = search_leftTree(0, N - 1, 0, now.id, 1);
				long long rightEdge = search_rightTree(0, N - 1, now.id + 1, N - 1, 1);
				long long nowA = now.h * (rightEdge - (leftEdge));
				maxA = max(maxA, nowA);

				sameheap.push(now);
			}

			else {
				while (!sameheap.empty()) {
					Edge here = sameheap.front();
					sameheap.pop();
					update_leftTree(0, N - 1, here.id, 1);
					update_rightTree(0, N - 1, here.id, 1);
				}

				long long leftEdge = search_leftTree(0, N - 1, 0, now.id, 1);
				long long rightEdge = search_rightTree(0, N - 1, now.id + 1, N - 1, 1);
				long long nowA = now.h * (rightEdge - (leftEdge));
				maxA = max(maxA, nowA);

				flag = now.h;
				sameheap.push(now);
			}
		}
		cout << maxA << "\n";
	}
	return 0;
}