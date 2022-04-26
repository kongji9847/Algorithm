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