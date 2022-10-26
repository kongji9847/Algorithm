#include <iostream>

using namespace std;

// 10�� �����ϴ� �ε��� ���� ã��
int arr[25] = { 1,5,9,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,21,25,127,10000,99999,99999999 };

void binary_search(int finding) {

	// 10�� ó������ ������ ������ ���ϱ� 
	// -> 10�� ã�� ���� �ƴ϶� �������� ã�� ��!
	int s = 0;
	int e = 25 - 1;
	int begin_ = 25 - 1;		// ���� ū ���� �ʱ�ȭ ���ش�.

	while (s <= e) {
		int mid = (s + e) / 2;
		
		if (finding == arr[mid]) {
			// ���������� �� �����Ƿ� �ϴ� ������ ����
			begin_ = min(begin_, mid);

			// ���������� �� �տ� ���� ���� �����ϱ� �������� ���� ����
			e = mid - 1;
		}

		else if (finding < arr[mid]) { e = mid - 1; }

		else if (finding > arr[mid]) { s = mid + 1; }
	}

	// 10 �� ���������� ������ ���� ã��;
	s = 0;
	e = 24;
	int end_ = 0;

	while (s <= e) {
		int mid = (s + e) / 2;

		if (finding == arr[mid]) {
			// �������� ���� �����Ƿ� ���� ����
			end_ = max(end_, mid);

			// �������� �� �ڿ� ���� ���� �����ϱ� ���������� ���� ���
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