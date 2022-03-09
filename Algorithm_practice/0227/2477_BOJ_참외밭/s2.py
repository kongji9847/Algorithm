import sys
sys.stdin = open('input.txt')

N = int(input())
arr = [tuple(map(int, input().split())) for _ in range(6)]
circle = arr + arr

# 3, 1 -> 423(13)1
for i in range(12):
    if circle[i][0] == circle[i+2][0] and circle[i+1][0] == circle[i+3][0]:
        ans = (circle[i+4][-1] * circle[i+5][-1]) - (circle[i+1][-1] * circle[i+2][-1])
        print(ans * N)
        break