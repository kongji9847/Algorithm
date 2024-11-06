#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <iostream>
using namespace std;

// Cyclic 형식으로 Queue 구현 => 주어진 capacity 안에서 push, pop을 반복할 수 있도록
class Queue {
public:
    // Queue의 capacity 상수
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