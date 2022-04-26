import sys
sys.stdin = open('input.txt')

from itertools import combinations, permutations
from collections import deque

N = int(input())
data = [list(map(int, input().split())) for _ in range(N)]
arr = deque(combinations(range(N), N//2))
ans = []

for i in range(len(arr)//2):
    star = arr.pop()
    star_power = 0
    for r, c in permutations(star, 2):
        star_power += data[r][c]

    link_power = 0
    link = arr.popleft()
    for r, c in permutations(link, 2):
        link_power += data[r][c]

    ans.append(abs(star_power - link_power))

print(min(ans))
