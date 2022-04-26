import sys
sys.stdin = open('input.txt')

def rotate_arr(level):





T = int(input())
for tc in range(1, T+1):
    N, Q = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(2**N)]
    levels = list(map(int, input().split()))