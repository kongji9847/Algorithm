#include <iostream>

using namespace std;

// 10이 존재하는 인덱스 구간 찾기
int arr[25] = { 1,5,9,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,21,25,127,10000,99999,99999999 };

void binary_search(int finding) {

	// 10이 처음으로 나오는 시작점 구하기 
	// -> 10을 찾는 것이 아니라 시작점을 찾는 것!
	int s = 0;
	int e = 25 - 1;
	int begin_ = 25 - 1;		// 제일 큰 수로 초기화 해준다.

	while (s <= e) {
		int mid = (s + e) / 2;
		
		if (finding == arr[mid]) {
			// 시작지점일 수 있으므로 일단 시작점 갱신
			begin_ = min(begin_, mid);

			// 시작지점은 더 앞에 있을 수도 있으니까 왼쪽으로 구간 당기기
			e = mid - 1;
		}

		else if (finding < arr[mid]) { e = mid - 1; }

		else if (finding > arr[mid]) { s = mid + 1; }
	}

	// 10 이 마지막으로 나오는 구간 찾기;
	s = 0;
	e = 24;
	int end_ = 0;

	while (s <= e) {
		int mid = (s + e) / 2;

		if (finding == arr[mid]) {
			// 끝지점일 수도 있으므로 끝점 갱신
			end_ = max(end_, mid);

			// 끝지점은 더 뒤에 있을 수도 있으니까 오른쪽으로 구간 잡기
			s = mid + 1;
		}

		else if (finding < arr[mid]) { e = mid - 1; }

		else if (finding > arr[mid]) { s = mid + 1; }
	}

	cout << begin_ << " " << end_ << "\n";

}



int main() {
	ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);

	binary_search(10);

	return 0;
}