# Expert 대비 (C++)

> ### Introduction
>
> - Expert 시험은 정해진 답이 없다. => 휴리스틱
>
> - 최적화의 최적화를 하여 높은 점수를 내면 랭킹대로 합격자가 정해진다.
>
>   
>
> - 라이브러리 사용 금지
>
> - 시간 제한은 10초
>
> - stack 제한은 2MB
>
> ### Expert 빈출 알고리즘
>
> - Greedy



## 1. Expert 풀이 방법

### 1) [문제 이해] `Pro`, `Adv`와 같이 쉬운 문제 설명 만들기

1. `main.cpp` 에 줄마다 주석 달기
   - `main()`, `verify()`, `main-api()` 꼼꼼히 보기(특히 `verify()`)
2. 놓친 부분이 없는지 다시 체크하기
3. 메모장에 줄 글로 문제 풀어쓰기
   - `main.cpp` 안의 변수로 문제 풀어쓰기(다른 용어 쓰지 않기)
   - 추후 최적화 아이디어/디버깅 시 유용하게 쓰인다.

```
1,000,000 x 1,000,000 맵에
M명의 driver (51 ~ 100명) 그리고
K명의 passenger (5,001 ~ 10,000명)이 있다.

각 passenger는 
탑승위치 Coordinates가 주어지고, 
도착위치 Coordinates가 주어진다.

각 driver와 passenger 위치는
분포가 고른 전체 랜덤으로 주어진다.

각 택시들은 passenger를 태우고, 도착위치에 내려주고,
다음 passenger를 태우고, 도착위치를 내려주곤한다.

assign_driver는 특정 택시 dID (driverID)가
어떤 pID(passengerID)들을 태울지
순서대로 배열에 기록하는 정답 API이다.

최대 이동거리를 가진 기사들의
이동거리의 합이 최소가 되도록
택시를 손님에게 배정해야하는 문제이다.

[평가방법]
각 택시별 운행 거리를 구한다.
가장 길게 운행한 택시가 한 TC의 대표 점수가 된다. (TC_SCORE)
각 TC별 대표 점수(TC_SCORE)들의 합이 가장 낮게 나오도록 해야한다.
```



### 2) [설계]

- 준비물 : 종이와 펜
- Worst Case ~ Best Case 의 점수를 대강 예측하여 점수 구간 확인
- 우선 최적화는 고려하지 않고 휴리스틱(평균에 가깝게 어림짐작) 설계
- 필요한 변수 및 함수 설계 (이름, 역할, 인자 등)

```
한 Taxi가 몇명의 승객을 태울까?

승객수가 10,000명
driver : 100명

한 driver가 100명 운전한다.
운행 태우러갈떄 300만 거리 (매번)
승객은 300만 매번
====================
한 driver가 50명 x (50만 + 50만)

600만 x 100 x 5 = 
100만 x 50 = 5000만 x 5 TC = 2.5억점
====================
결론
2.5억점 ~ 30억점
====================
```



### 3) [구현] 휴리스틱

- 2)에서 설계한대로 휴리스틱 구현
- 우선 편한대로 라이브러리 사용해서 구현
- Score 확인



### 4) [설계/구현] 최적화

- 최적화 방법을 구상해보고 구현한다.
- Score를 비교하며 최적화를 반복한다.
- 최적화를 덕지덕지 한다



### 5) 라이브러리 변환

- 실제 구현한 자료 구조로 라이브러리를 변환한다.





## 2. 자료 구조 라이브러리 구현

### 2.1 Vector

#### Vector 라이브러리 사용

```cpp
#include <iostream>;
#include <vector>;
using namespace std;

void print(vector<int> arr) {
	for (int num : arr) {
		cout << num << " ";
	}
	cout << "\n";
}

vector<int> getPlusOne(vector<int> arr) {
	vector<int> result;
	
	for (int num : arr) {
		result.push_back(num + 1);
	}
	return result;
}

void setPlus(vector<int>& arr, int num) {
	for (int i = 0; i < arr.size(); i++) {
		arr[i] += num;
	}
}

int main() {
    vector<int> arr = {4, 2, 4, 1, 5, 6};
    arr.push_back(3);
    arr.push_back(2);
    arr.pop_back();
    print(arr);
    
    vector<int> brr = getPlusOne(arr);
    print(brr);
    
    setPluse(arr, 2);
    print(arr);
}
```



#### Converting

```cpp
#ifndef _CRT_SECURE_NO_WARNINGS
#define _CRT_SECURE_NO_WARNINGS
#endif

#include <iostream>;
//#include <vector>;
using namespace std;

//1. 배열 길이가 10만이 넘어가면 전역에 선언
// 전역에 선언 시, 자동으로 0으로 초기화
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
    //1. 배열 생성 -> 로컬이나 전역에
    //vector<int> arr = {4, 2, 4, 1, 5, 6};

    //2.
    //arr.push_back(3);
    arr[arr_cnt++] = 3;			//arr_cnt에 3을 넣어준 뒤에 arr_cnt += 1

    //arr.push_back(2);
    arr[arr_cnt++] = 2;

    //arr.pop_back();
    arr[--arr_cnt] = 0;			//arr_cnt-=1을 한 후에 arr_cnt에 0으로 재할당

    //3.
    print(arr, arr_cnt);

    getPlusOne(brr, arr, arr_cnt);
    print(brr, arr_cnt);

    setPlus(arr, arr_cnt, 10);
    print(arr, arr_cnt);
}
```



### 2.2 Queue

- 시험 환경에 주어진 Reference Code 활용
  1.  전역에 `class Queue` 생성
  2. 클래스 `public` 설정
  3. `#define`을 `static const int`로 변환
  4. 필드 모두 0으로 초기화

```cpp
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <iostream>
using namespace std;

// Cyclic 형식으로 Queue 구현 => 주어진 capacity 안에서 push, pop을 반복할 수 있도록
class Queue {
public:
    // Queue의 capacity 상수 (but, Q가 담을 수 있는 최대 요소 개수는 MAX_N-1개)
    // static const => 클래스의 모든 인스턴스가 공유하는 상수
    static int const MAX_N = 100;

    // 배열로 Queue 구현 시작
    // 초기화
    int front = 0;
    int rear = 0;
    int queue[MAX_N] = {0};

    void queueInit(void)
    {
        front = 0;
        rear = 0;
    }

    // 맨 앞 인덱스와 맨 뒤 인덱스가 동일하면 비어있는 큐
    int queueIsEmpty(void)
    {
        return (front == rear);
    }

    // queue에 MAX_N - 1개 만큼 요소가 들어있는지 확인
    int queueIsFull(void)
    {
        // rear와 front의 간격이 원으로 N-1이 되어야 함 => cyclic Queue
        // Example) MAX_SIZE가 5인 경우 => 0123_ : full / _1234 : full / 0_234 full :
        if ((rear + 1) % MAX_N == front)
        {
            return 1;
        }
        else
        {
            return 0;
        }
    }

    // queue.push(int value)
    int queueEnqueue(int value)
    {
        // queue가 차 있는지 확인
        // 만약 front=0이고, rear가 MAX_N-1 (가능한 마지막 인덱스)라면 Full 이 뜬다.
        // 결국 해당 Q에 들어갈 수 있는 요소의 개수는 MAX_N-1개다.
        if (queueIsFull())
        {
            printf("queue is full!");
            return 0;
        }
        // rear 인덱스 자리 (비어 있는 상태)에 value를 넣고
        queue[rear] = value;
        // rear를 한칸 뒤로 보낸다.
        rear++;
        // rear가 맨 끝까지 갔다면 rear를 다시 처음으로 보낸다.
        if (rear == MAX_N)
        {
            rear = 0;
        }

        return 1;
    }

    // queue.pop()
    // 반환값을 담는 value는 포인터
    int queueDequeue(int* value)
    {
        // queue가 비어져 있는지 확인
        if (queueIsEmpty())
        {
            printf("queue is empty!");
            return 0;
        }
        // 맨 앞에서 값을 꺼내서 value에 할당한다.
        *value = queue[front];                          // 포인터가 가르키는 주소의 메모리에 반환 값 할당
        // 맨 앞 인덱스를 뒤로 한 칸 보낸다.
        front++;
        // 맨 앞 인덱스가 뒤로 끝까지 간 상태라면, 다시 맨 앞으로 가져온다.
        if (front == MAX_N)
        {
            front = 0;
        }
        return 1;
    }

};


int main() {

    Queue q;

    q.queueEnqueue(2);
    q.queueEnqueue(5);

    int ret = 0;
    // &ret = ret의 주소값에 해당하는 메모리에 반환값 대입 => ret의 data 변경
    q.queueDequeue(&ret);
    cout << ret;
}
```

