#include <iostream>

using namespace std;

int arr[8] = { 0, 3, 4, 6, 7, 9, 11, 17 };

int binary_search(int finding) {
	int s = 0;
	int e = 8;			// e = arr.size()
	int ans;

	// s가 e와 같다는 것은 s = e = mid 이므로 제일 마지막까지 가본 것 
	// -> 이후에 s와 e는 엇갈려서 while문이 끝난다.
	while (s <= e) {
		int mid = (s + e) / 2;

		if (arr[mid] == finding) {
			ans = mid;
			return ans;
		}

		// 찾는 것이 mid보다 왼쪽에 가 있으면 
		// -> 다음 끝지점을 mid 앞으로 당겨준다.
		else if (arr[mid] > finding) {
			e = mid - 1;
		}

		// 찾는 것이 mid 보다 오른쪽에 가 있으면
		// 다음 구간을 mid 오른쪽으로 이동시킨다.
		else if (arr[mid] < finding) {
			s = mid + 1;
		}
	}

	// while문을 빠져나왔다는 것은 찾지 못하였다는 뜻
	return -1;
}



int main() {
	ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);

	cout << binary_search(4) << "\n";		// 2
	cout << binary_search(19) << "\n";		// -1


	return 0;
}