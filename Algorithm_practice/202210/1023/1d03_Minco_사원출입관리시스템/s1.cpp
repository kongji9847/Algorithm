#define _CRT_SECURE_NO_WARNINGS
#include<iostream>
#include<cstring>

using namespace std;

int N, TYPE;
int num;
string name;

int company[10000] = {0};
string company_name[10000];

int main() {
	freopen_s(new FILE*, "input.txt", "r", stdin);

	cin >> N;
	
	for (int i = 0; i < N; i++) {
		cin >> TYPE >> num;

		if (TYPE == 1) {
			cin >> name;

			if (company[num] == 0) {
				company[num] = -1;
				company_name[num] = name;
				cout << num << " OK" << "\n";
			}

			else {
				cout << num << " ERROR" << "\n";
			}
		}

		else if (TYPE == 2) {
			if (company[num] == -1) {
				name = company_name[num];
				cout << num << " " << name << " ENTER" << "\n";
				company[num] = 1;
			}
			else if (company[num] == 1) {
				name = company_name[num];
				cout << num << " " << name << " EXIT" << "\n";
				company[num] = -1;
			}
			else if (company[num] == 0) {
				cout << num << " ERROR" << "\n";
			}

		}

	}


	return 0;
}