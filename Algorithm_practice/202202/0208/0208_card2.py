import sys
from collections import deque
cards = deque(range(1, int(sys.stdin.readline().strip())+1))

while len(cards) > 1:
    cards.popleft()
    n = cards.popleft()
    cards.append(n)

print(cards[0])