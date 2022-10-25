// binary search로 중복된 숫자 구간 찾기

#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <algorithm>

using namespace std;

int N;
long long K;
long long nums[1000];

struct Num {
	long long value;
	int id;
};

bool cmp(Num left, Num right) {
	if (left.value < right.value) {
		return true;
	}
	if (left.value > right.value) {
		return false;
	}
	if (left.id < right.id) {
		return true;
	}
	if (left.id > right.id) {
		return false;
	}
	return false;
}

Num vect[1000];

void input() {
	cin >> N >> K;
	for (int i = 0; i < N; i++) {
		cin >> nums[i];
		vect[i] = { nums[i], i };
	}
	sort(vect + 0, vect + N, cmp);
}

int binary_search(long long k, int k_id) {
	// [begin, end)
	// k가 나오는 제일 첫 구간 찾기
	int begin_ = N;
	int s = 0;
	int e = N - 1;

	while (s <= e) {
		int mid = (s + e) / 2;

		if (k == vect[mid].value) {
			begin_ = min(begin_, mid);
			e = mid - 1;
		}

		else if (k < vect[mid].value) {
			e = mid - 1;
		}

		else {
			s = mid + 1;
		}
	}

	// k가 끝나는 지점 찾기
	int end_ = 0;
	s = 0;
	e = N - 1;

	while (s <= e) {
		int mid = (s + e) / 2;

		if (k == vect[mid].value) {
			end_ = max(mid, end_);
			s = mid + 1;
		}

		else if (k > vect[mid].value) {
			s = mid + 1;
		}

		else {
			e = mid - 1;
		}
	}

	int cnt = 0;

	if (end_ >= begin_) {
		for (int i = begin_; i <= end_; i++) {
			if (vect[i].id > k_id) {
				cnt += 1;
			}
		}
		return cnt;
	}

	else {
		return 0;
	}

}



int main() {
	ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);

	//freopen_s(new FILE*, "input.txt", "r", stdin);
	input();

	int ans = 0;

	for (int i = 0; i < N; i++) {
		for (int j = i + 1; j < N; j++) {
			long long hap = nums[i] + nums[j];
			long long finding = K - hap;
			ans += binary_search(finding, j);
		}
	}

	cout << ans << "\n";




	return 0;
}