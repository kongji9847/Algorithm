/*
입력받을 배열이 1000111101 이런 식으로 공백없이 주어졌다면, 
string 을 이용하여 배열로 입력받기
*/

#include<iostream>
#include<string>

using namespace std;

void func() {
	int H, W;
	cin >> H >> W;
	string str;

	for (int row = 0; row < H; row++) {
		cin >> str;									// 각 문자열을 입력받기

		int tmp = 0;

		// 문자열에 안에 있는 숫자를 배열처럼 인덱스로 확인하기
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