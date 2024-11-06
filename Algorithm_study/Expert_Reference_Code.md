# Library Converting 용 Reference Code

> 출처 : SWEA 구글 검색 > 회원가입, 로그인 > 메뉴> Code > Reference Code



## 1. Stack

```cpp
#include <stdio.h>
 
#define MAX_N 100
 
int top;
int stack[MAX_N];
 
void stackInit(void)
{
    top = 0;
}
 
int stackIsEmpty(void)
{
    return (top == 0);
}
 
int stackIsFull(void)
{
    return (top == MAX_N);
}
 
int stackPush(int value)
{
    if (stackIsFull())
    {
        printf("stack overflow!");
        return 0;
    }
    stack[top] = value;
    top++;
 
    return 1;
}
 
int stackPop(int *value)
{
    if (stackIsEmpty())
    {
        printf("stack is empty!");
        return 0;
    }
    top--;
    *value = stack[top];
 
    return 1;
}
 
int main(int argc, char* argv[])
{
    int T, N;
 
    scanf("%d", &T);
 
    for (int test_case = 1; test_case <= T; test_case++)
    {
        scanf("%d", &N);
        stackInit();
        for (int i = 0; i < N; i++) 
        {
            int value;
            scanf("%d", &value);
            stackPush(value);
        }
 
        printf("#%d ", test_case);
 
        while (!stackIsEmpty())
        {
            int value;
            if (stackPop(&value) == 1)
            {
                printf("%d ", value);
            }
        }
        printf("\n");
    }
    return 0;
}
```



## 2. Queue

```cpp
#include <stdio.h>
 
#define MAX_N 100
 
int front;
int rear;
int queue[MAX_N];
 
void queueInit(void)
{
    front = 0;
    rear = 0;
}
 
int queueIsEmpty(void)
{
    return (front == rear);
}
 
int queueIsFull(void)
{
    if ((rear + 1) % MAX_N == front)
    {
        return 1;
    }
    else
    {
        return 0;
    }
}
 
int queueEnqueue(int value)
{
    if (queueIsFull())
    {
        printf("queue is full!");
        return 0;
    }
    queue[rear] = value;
    rear++;
    if (rear == MAX_N)
    {
        rear = 0;
    }
 
    return 1;
}
 
int queueDequeue(int *value)
{
    if (queueIsEmpty())
    {
        printf("queue is empty!");
        return 0;
    }
    *value = queue[front];
    front++;
    if (front == MAX_N)
    {
        front = 0;
    }
    return 1;
}
 
int main(int argc, char* argv[])
{
    int T;
    int N;
 
    scanf("%d", &T);
 
    for (int test_case = 1; test_case <= T; test_case++)
    {
        scanf("%d", &N);
 
        queueInit();
        for (int i = 0; i < N; i++)
        {
            int value;
            scanf("%d", &value);
            queueEnqueue(value);
            printf("setValue");
        }
 
        printf("#%d ", test_case);
 
        while (!queueIsEmpty())
        {
            int value;
            if (queueDequeue(&value) == 1)
            {
                printf("%d ", value);
            }
        }
        printf("\n");
    }
    return 0;
}
```



## 3.Priority Queue

```cpp
#include <stdio.h>
 
#define MAX_SIZE 100
 
int heap[MAX_SIZE];
int heapSize = 0;
 
void heapInit(void)
{
    heapSize = 0;
}
 
int heapPush(int value)
{
    if (heapSize + 1 > MAX_SIZE)
    {
        printf("queue is full!");
        return 0;
    }
 
    heap[heapSize] = value;
 
    int current = heapSize;
    while (current > 0 && heap[current] < heap[(current - 1) / 2]) 
    {
        int temp = heap[(current - 1) / 2];
        heap[(current - 1) / 2] = heap[current];
        heap[current] = temp;
        current = (current - 1) / 2;
    }
 
    heapSize = heapSize + 1;
 
    return 1;
}
 
int heapPop(int *value)
{
    if (heapSize <= 0)
    {
        return -1;
    }
 
    *value = heap[0];
    heapSize = heapSize - 1;
 
    heap[0] = heap[heapSize];
 
    int current = 0;
    while (current * 2 + 1 < heapSize)
    {
        int child;
        if (current * 2 + 2 == heapSize)
        {
            child = current * 2 + 1;
        }
        else
        {
            child = heap[current * 2 + 1] < heap[current * 2 + 2] ? current * 2 + 1 : current * 2 + 2;
        }
 
        if (heap[current] < heap[child])
        {
            break;
        }
 
        int temp = heap[current];
        heap[current] = heap[child];
        heap[child] = temp;
 
        current = child;
    }
    return 1;
}
 
int main(int argc, char* argv[])
{
    int T, N;
 
    scanf("%d", &T);
 
    for (int test_case = 1; test_case <= T; test_case++)
    {
        scanf("%d", &N);
         
        heapInit();
         
        for (int i = 0; i < N; i++)
        {
            int value;
            scanf("%d", &value);
            heapPush(value);
        }
 
        printf("#%d ", test_case);
 
        for (int i = 0; i < N; i++)
        {
            int value;
            heapPop(&value);
            printf("%d ", value);
        }
        printf("\n");
    }
    return 0;
}
```



## 4. Hash

```cpp
#include <stdio.h>
#include <string.h>
#include <memory.h>
 
#define MAX_KEY 64
#define MAX_DATA 128
#define MAX_TABLE 4096
 
typedef struct
{
    char key[MAX_KEY + 1];
    char data[MAX_DATA + 1];
}Hash;
Hash tb[MAX_TABLE];
 
unsigned long hash(const char *str)
{
    unsigned long hash = 5381;
    int c;
 
    while (c = *str++)
    {
        hash = (((hash << 5) + hash) + c) % MAX_TABLE;
    }
 
    return hash % MAX_TABLE;
}
 
int find(const char *key, char *data)
{
    unsigned long h = hash(key);
    int cnt = MAX_TABLE;
 
    while (tb[h].key[0] != 0 && cnt--)
    {
        if (strcmp(tb[h].key, key) == 0)
        {
            strcpy(data, tb[h].data);
            return 1;
        }
        h = (h + 1) % MAX_TABLE;
    }
    return 0;
}
 
int add(const char *key, char *data)
{
    unsigned long h = hash(key);
 
    while (tb[h].key[0] != 0)
    {
        if (strcmp(tb[h].key, key) == 0)
        {
            return 0;
        }
 
        h = (h + 1) % MAX_TABLE;
    }
    strcpy(tb[h].key, key);
    strcpy(tb[h].data, data);
    return 1;
}
 
 
int main(int argc, char* argv[])
{
    int T, N, Q;
 
    scanf("%d", &T);
 
    for (int test_case = 1; test_case <= T; test_case++)
    {
        memset(tb, 0, sizeof(tb));
        scanf("%d", &N);
        char k[MAX_KEY + 1];
        char d[MAX_DATA + 1];
 
        for (int i = 0; i < N; i++)
        {
            scanf("%s %s\n", &k, &d);
            add(k, d);
        }
 
        printf("#%d\n", test_case);
 
        scanf("%d", &Q);
        for (int i = 0; i < Q; i++)
        {
            char k[MAX_KEY + 1];
            char d[MAX_DATA + 1];
 
            scanf("%s\n", &k);
 
            if (find(k, d))
            {
                printf("%s\n", d);
            }
            else
            {
                printf("not find\n");
            }
        }
    }
    return 0;
}
```



## 5. Quick Sort

```cpp
#include <stdio.h>
 
#define MAX_NUM 100
 
int input[MAX_NUM];
int num;
 
void quickSort(int first, int last)
{
    int pivot;
    int i;
    int j;
    int temp;
     
    if (first < last)
    {
        pivot = first;
        i = first;
        j = last;
 
        while (i < j)
        {
            while (input[i] <= input[pivot] && i < last)
            {
                i++;
            }
            while (input[j] > input[pivot])
            {
                j--;
            }
            if (i < j)
            {
                temp = input[i];
                input[i] = input[j];
                input[j] = temp;
            }
        }
 
        temp = input[pivot];
        input[pivot] = input[j];
        input[j] = temp;
 
        quickSort(first, j - 1);
        quickSort(j + 1, last);
    }
}
 
void printResult(void)
{
    int i;
 
    for (i = 0; i < num; ++i)
    {
        printf("%d ", input[i]);
    }
    printf("\n");
}
 
int main(void)
{
    int T;
    int test_case;
    int i;
 
    scanf("%d", &T);
 
    for (test_case = 1; test_case <= T; test_case++)
    {
        scanf("%d", &num);
        for (i = 0; i < num; i++)
        {
            scanf("%d", &input[i]);
        }
        quickSort(0, num - 1);
        printf("#%d ", test_case);
        printResult();
    }
 
    return 0;
}
```

