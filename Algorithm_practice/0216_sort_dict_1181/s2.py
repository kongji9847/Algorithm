import sys
sys.stdin = open('input.txt', 'rt', encoding='utf-8')

T = int(input())
res = []
for _ in range(T):
    res.append(input())
arr = list(set(res))

arr.sort()
num = map(len, arr)
item = list(zip(num, arr))
item.sort()
for element in item:
    print(element[-1])