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
