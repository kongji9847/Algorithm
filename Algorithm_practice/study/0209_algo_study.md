# 0209 study

## 1. Stack

### [백준 10828: 스택](https://www.acmicpc.net/problem/10828)

```python
import sys
#input = sys.stdin.readline

result = []
for _ in range(int(sys.stdin.readline().strip())):
    # ans = sys.stdin.readline().split()
    ans = sys.stdin.readline().strip().split(' ')
    if ans[0]=='push':
        result.append(int(ans[-1]))
    
    elif ans[0]=='top':
        if not result:
            print(-1)
        else: print(result[-1])
    
    elif ans[0] =='size':
        print(len(result))
    
    elif ans[0] =='empty':
        if not result:
            print(1)
        else: print(0)

    elif ans[0] == 'pop':
        if not result:
            print(-1)
        else: print(result.pop())
```

- 새로 알게 된 것:  `sys.stdin.readline().strip().split(' ')`
- sys.stdin.readline().split() 으로 할 것!! split(' ')을 하면 readline()의 \n 도 함께 출력된다.



## 2. Queue

### [백준 18258: 큐2](https://www.acmicpc.net/problem/18258)

```python
import sys
from collections import deque

que = deque()
for _ in range(int(sys.stdin.readline().strip())):
    ans = sys.stdin.readline().strip().split(' ')
    if ans[0]=='push':
        que.append(int(ans[-1]))
    
    elif ans[0] == 'pop':
        if not que:
            print(-1)
        else: print(que.popleft())

    elif ans[0] =='size':
        print(len(que))

    elif ans[0] =='empty':
        if not que:
            print(1)
        else: print(0)
    
    elif ans[0]=='front':
        if not que:
            print(-1)
        else: print(que[0])

    elif ans[0]=='back':
        if not que:
            print(-1)
        else: print(que[-1])
```

- 참조: [queue 파이썬 공식 문서](https://docs.python.org/3/library/queue.html#module-queue)



### [프로그래머스 큐 관련 문제](https://programmers.co.kr/learn/courses/30/lessons/42586?language=python3)

```python
def solution(progresses, speeds):
    days = []
    for i in range(len(progresses)):
        count = 1
        while progresses[i] < 100:
            progresses[i] += speeds[i]
            count += 1
        days.append(count)
    
    stand = days[0]
    answer = [1]
    for day in range(1, len(days)):
        if days[day] <= stand:
            answer[-1] =  answer[-1] + 1
        else:
            stand = days[day]
            answer.append(1)
            
    return answer
```



## 3. Deque

### [백준 10866: 덱](https://www.acmicpc.net/problem/10866)

```python
import sys
from collections import deque

que = deque()
for _ in range(int(sys.stdin.readline().strip())):
    ans = sys.stdin.readline().strip().split(' ')
    if ans[0]=='push_front':
        que.appendleft(int(ans[-1]))

    elif ans[0]=='push_back':
        que.append(int(ans[-1]))
    
    elif ans[0] == 'pop_front':
        if not que:
            print(-1)
        else: print(que.popleft())

    elif ans[0] == 'pop_back':
        if not que:
            print(-1)
        else: print(que.pop())

    elif ans[0] =='size':
        print(len(que))

    elif ans[0] =='empty':
        if not que:
            print(1)
        else: print(0)
    
    elif ans[0]=='front':
        if not que:
            print(-1)
        else: print(que[0])

    elif ans[0]=='back':
        if not que:
            print(-1)
        else: print(que[-1])
```

- 참조: [deque 파이썬 공식 문서](https://docs.python.org/3/library/collections.html#collections.deque)



### [백준 17608: 막대기](https://www.acmicpc.net/problem/17608)

```python
import sys
from collections import deque
data = deque()
for _ in range(int(sys.stdin.readline().strip())):
    data.appendleft(int(sys.stdin.readline().strip()))

high = data[0]
count = 1
for i in range(1, len(data)):
    if high < data[i]:
        count += 1
        high = data[i]

print(count)
```



### [백준 2164: 카드2](https://www.acmicpc.net/problem/2164)

```python
import sys
from collections import deque
cards = deque(range(1, int(sys.stdin.readline().strip())+1))

while len(cards) > 1:
    cards.popleft()
    n = cards.popleft()
    cards.append(n)

print(cards[0])
```
