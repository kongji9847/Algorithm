#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <iostream>
using namespace std;

// Cyclic �������� Queue ���� => �־��� capacity �ȿ��� push, pop�� �ݺ��� �� �ֵ���
class Queue {
public:
    // Queue�� capacity ���
    // static const => Ŭ������ ��� �ν��Ͻ��� �����ϴ� ���
    static int const MAX_N = 100;

    // �迭�� Queue ���� ����
    // �ʱ�ȭ
    int front = 0;
    int rear = 0;
    int queue[MAX_N] = {0};

    void queueInit(void)
    {
        front = 0;
        rear = 0;
    }

    // �� �� �ε����� �� �� �ε����� �����ϸ� ����ִ� ť
    int queueIsEmpty(void)
    {
        return (front == rear);
    }

    // queue�� MAX_N - 1�� ��ŭ ��Ұ� ����ִ��� Ȯ��
    int queueIsFull(void)
    {
        // rear�� front�� ������ ������ N-1�� �Ǿ�� �� => cyclic Queue
        // Example) MAX_SIZE�� 5�� ��� => 0123_ : full / _1234 : full / 0_234 full :
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
        // queue�� �� �ִ��� Ȯ��
        // ���� front=0�̰�, rear�� MAX_N-1 (������ ������ �ε���)��� Full �� ���.
        // �ᱹ �ش� Q�� �� �� �ִ� ����� ������ MAX_N-1����.
        if (queueIsFull())
        {
            printf("queue is full!");
            return 0;
        }
        // rear �ε��� �ڸ� (��� �ִ� ����)�� value�� �ְ�
        queue[rear] = value;
        // rear�� ��ĭ �ڷ� ������.
        rear++;
        // rear�� �� ������ ���ٸ� rear�� �ٽ� ó������ ������.
        if (rear == MAX_N)
        {
            rear = 0;
        }

        return 1;
    }

    // queue.pop()
    // ��ȯ���� ��� value�� ������
    int queueDequeue(int* value)
    {
        // queue�� ����� �ִ��� Ȯ��
        if (queueIsEmpty())
        {
            printf("queue is empty!");
            return 0;
        }
        // �� �տ��� ���� ������ value�� �Ҵ��Ѵ�.
        *value = queue[front];                          // �����Ͱ� ����Ű�� �ּ��� �޸𸮿� ��ȯ �� �Ҵ�
        // �� �� �ε����� �ڷ� �� ĭ ������.
        front++;
        // �� �� �ε����� �ڷ� ������ �� ���¶��, �ٽ� �� ������ �����´�.
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
    // &ret = ret�� �ּҰ��� �ش��ϴ� �޸𸮿� ��ȯ�� ���� => ret�� data ����
    q.queueDequeue(&ret);
    cout << ret;
}