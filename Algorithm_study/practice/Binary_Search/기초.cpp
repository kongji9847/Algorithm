#include <iostream>

using namespace std;

int arr[8] = { 0, 3, 4, 6, 7, 9, 11, 17 };

int binary_search(int finding) {
	int s = 0;
	int e = 8;			// e = arr.size()
	int ans;

	// s�� e�� ���ٴ� ���� s = e = mid �̹Ƿ� ���� ���������� ���� �� 
	// -> ���Ŀ� s�� e�� �������� while���� ������.
	while (s <= e) {
		int mid = (s + e) / 2;

		if (arr[mid] == finding) {
			ans = mid;
			return ans;
		}

		// ã�� ���� mid���� ���ʿ� �� ������ 
		// -> ���� �������� mid ������ ����ش�.
		else if (arr[mid] > finding) {
			e = mid - 1;
		}

		// ã�� ���� mid ���� �����ʿ� �� ������
		// ���� ������ mid ���������� �̵���Ų��.
		else if (arr[mid] < finding) {
			s = mid + 1;
		}
	}

	// while���� �������Դٴ� ���� ã�� ���Ͽ��ٴ� ��
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