#ifndef _CRT_SECURE_NO_WARNINGS
#define _CRT_SECURE_NO_WARNINGS
#endif

#include <iostream>;
//#include <vector>;
using namespace std;

//1. �迭 ���̰� 10���� �Ѿ�� ������ ����
// ������ ���� ��, �ڵ����� 0���� �ʱ�ȭ
int arr[10000] = { 4, 2, 4, 1, 5, 6 };
int arr_cnt = 6;
int brr[10000];


//void print(vector<int> arr)
void print(int arr[], int arr_cnt) {
    for (int i = 0; i < arr_cnt; i++) {
        cout << arr[i] << " ";
    }
    cout << "\n";
}

//vector<int> getPlusOne(vector<int> arr)
void getPlusOne(int brr[], int arr[], int arr_cnt) {

    for (int i = 0; i < arr_cnt; i++) {
        brr[i] = arr[i] + 1;
    }
}

//void setPlus(vector<int>& arr, int num)
void setPlus(int arr[], int arr_cnt, int num) {
    for (int i = 0; i < arr_cnt; i++) {
        arr[i] += num;
    }
}

int main() {
    //1. �迭 ���� -> �����̳� ������
    //vector<int> arr = {4, 2, 4, 1, 5, 6};

    //2.
    //arr.push_back(3);
    arr[arr_cnt++] = 3;			//arr_cnt�� 3�� �־��� �ڿ� arr_cnt += 1

    //arr.push_back(2);
    arr[arr_cnt++] = 2;

    //arr.pop_back();
    arr[--arr_cnt] = 0;			//arr_cnt-=1�� �� �Ŀ� arr_cnt�� 0���� ���Ҵ�

    //3.
    print(arr, arr_cnt);

    getPlusOne(brr, arr, arr_cnt);
    print(brr, arr_cnt);

    setPlus(arr, arr_cnt, 10);
    print(arr, arr_cnt);
}