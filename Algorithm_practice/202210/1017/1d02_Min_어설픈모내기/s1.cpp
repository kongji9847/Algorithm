/*
�Է¹��� �迭�� 1000111101 �̷� ������ ������� �־����ٸ�, 
string �� �̿��Ͽ� �迭�� �Է¹ޱ�
*/

#include<iostream>
#include<string>

using namespace std;

void func() {
	int H, W;
	cin >> H >> W;
	string str;

	for (int row = 0; row < H; row++) {
		cin >> str;									// �� ���ڿ��� �Է¹ޱ�

		int tmp = 0;

		// ���ڿ��� �ȿ� �ִ� ���ڸ� �迭ó�� �ε����� Ȯ���ϱ�
		for (int col = 0; col < W; col++) {
			if (str[col] == '1') {
				tmp += 1;
			}
		}

		cout << tmp << "\n";
	}
}

int main() {
	ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);

	func();

	return 0;
}