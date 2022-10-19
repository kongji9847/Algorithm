# B형 대비 (C++)

## 0. Pro 빈출 알고리즘

> 1. **Segment Tree** 
> 2. **Dijkstra** 
> 3. **Priority Queue**
> 4. **Union Find**
> 5. **MST**



## 1. Build Test & 디버깅

### 1.1. Build Test

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



### 1.2. 디버그 단축키

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



#### 1.2.1 디버그 연습 코드

```c++
// Break Point와 Step Over 그리고 Trace를 종료하는 단축키를 반복 연습합니다.

#include<iostream>
using namespace std;

int main()
{
//Break Point
	cout << "A" << "\n";
	cout << "B" << "\n";
	cout << "C" << "\n";
	cout << "D" << "\n";
//Break Point, Step Over
	cout << "E" << "\n";
	cout << "F" << "\n";
	cout << "G" << "\n";
	cout << "H" << "\n";
//Finish
	cout << "I" << "\n";
	cout << "J" << "\n";

	return 0;
}
```

```c++
/*
조사식에 변수를 등록합니다.
Break Point, Run to cursor, Step Into 단축키를 연습합니다.
*/

#include<iostream>
using namespace std;

void BTS() {
    cout << "A" << "\n"; 
    cout << "B" << "\n"; 
}
int main()
{
    int x;
 //Break Point
    x = 1;
    x = 2;
    x = 3;
    x = 4;
    x = 5;
    x = 6;
 //Run to cursor, Step Over
    x = 10;
    x = 20;
    x = 30;
    x = 40;
 //Step Into
    BTS();
    x = -1;
    x = -2;
 //Finish Trace
    x = -3;
    return 0; 
}
```

``` c++
// step over와 step into 헷갈리지 않게 연습

#include<iostream>
using namespace std;

void over() {
    for (int i = 0; i < 10; i++) {
        cout << "#";
    }
    cout << "\n"; 
    cout << "OVER" << "\n"; 
}

void into() {
    cout << "INTO" << "\n"; 
}

int main()
{
    //breakpoint
    over(); //over
    into(); //into
    over();
    over();
    over();
    into();
    over();
    into();
    over();
    into();
    over();
    return 0; 
}
```

```c++
#include<iostream>
using namespace std; 


void gogo()
{
    cout << "GOGO"<<endl;
}

void bts()
{
    gogo();
    cout << "BTS Last" << "\n";
}

void abc()
{
    bts();
    gogo();
    cout << "ABC Last" << "\n";
}

int main() {
    gogo();
    abc();
    bts();
    cout << "HOME";
}
```



## 2. 시간복잡도

```
O(N) : N이 1억(100,000,000)일 때, 1초 걸린다.
O(N^2) : N이 10,000일 때, 1초가 걸린다.
O(N^3) : N이 1000일 때, 10초가 걸린다.
O(NlogN) :

BFS의 시간복잡도는 O(노드개수)
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
