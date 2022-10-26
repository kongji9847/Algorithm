# B형 대비 (C++)

## 0. Pro 빈출 알고리즘

> 1. **Segment Tree** 
> 2. **Dijkstra** 
> 3. **Priority Queue**
> 4. **Union Find**
> 5. **MST**





## 1. 시간복잡도

```
O(N) : N이 1억(100,000,000)일 때, 1초 걸린다.
O(N^2) : N이 10,000일 때, 1초가 걸린다.
O(N^3) : N이 1000일 때, 10초가 걸린다.
O(NlogN) :

BFS의 시간복잡도는 O(노드개수)
```





## 2. C++ 시작

### 2.1. Build Test

```c++
#include<iostream>
using namespace std; 

int main()
{
    // cin, cout 속도를 빠르게 해준다.
  	ios::sync_with_stdio(false); 
	cin.tie(0); 
	cout.tie(0); 

	cout << "Hi" << "\n";
    
	return 0; 
}
```

- `cin`, `cout`은 그대로 쓰면 속도가 느리므로, 위의 명령어를 추가해준다.
- 이때, `cout`에서 `endl`을 쓰지 않고 `"\n"`을 써야한다.



### 2.2. 파일 입출력

```c++
#define _CRT_SECURE_NO_WARNINGS			// 일부 버전에 안전성의 문제로 warning을 발생시키므로
#include <iostream>

using namespace std;

int main() {
	ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);

	freopen_s(new FILE*, "input.txt", "r", stdin);
}
```

- `input`은 `리소스 파일`에 `"input.txt"`로 저장하고 사용한다.
- 추가해준 코드 2줄은 답안 제출시 주석 처리 해야한다.



### 2.3. 디버그 단축키

```
// 단축키
break point 
vs : F9 (라인에 커서 위치한 채로)

// 디버그
vs: F5

// step over (한 줄을 실행한다. 함수를 한번에 실행 후, 다음으로 넘어간다.) 
vs : F10

// resume (디버그로 한 줄 한 줄 실행시키는 트레이스 모드를 그만두고 다음 브레이크 포인트를 만날 때까지 실행한다.)
vs : F5

// terminate
vs : shift + F5

// step into (함수 내부로 들어간다.) 
vs : F11
eclipse : F5

// step return (함수 리턴 시키기)
vs : shift + F11 
```





## 3. C++ 문법 Tip!







## 4. Binary Search

### 4.1. 기초 코드(중복X)

```c++
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
```



### 4.2. 중복된 수의 구간 찾기

```c++
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
```















## 99. Tips!

### 99.1. DAT(Direct Address Table)

```c++
// 배열 안에 있는 숫자 세주기

#include<iostream>
#include<string> // string class 

using namespace std; 

int main()
{
	ios::sync_with_stdio(false); 
	cin.tie(0); 
	cout.tie(0); 
    
	int arr[] = { 3,2,1,7,3,7,2,1,1,1 };
	int cnt[10] = { 0 }; 
	
	for (int i = 0; i < 10; i++) {
		int val = arr[i];
		cnt[val] ++; 
	}
	for (int num = 1; num <= 9; num++) {
		cout << num << ":" << cnt[num] << "개" << "\n";
	}
	return 0; 
}
```

- 각각의 숫자 개수를 찾을 때마다 배열을 돌지말고, 배열을 한번만 돌면서 `dat` 배열에 숫자 개수를 더해주면서 갱신한다.
- for문을 여러번 돌리지 않아도 되어 시간이 단축된다.



### 99.2. 우선순위에 따라 정렬하기







--------

### 99.99. 문제 Tip

#### 99.99.1. 만들 수 있는 모든 직사각형

```
a--------d
|        |
|        |
b--------c

a와 c만 구하면 된다.
```
