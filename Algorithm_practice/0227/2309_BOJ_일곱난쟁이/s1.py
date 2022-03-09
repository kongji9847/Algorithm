import sys
sys.stdin = open('input.txt')

arr = [int(input()) for _ in range(9)]
arr.sort()

def search(arr):
    remain = sum(arr) - 100
    for f in range(8):
        if arr[f] < remain:
            remain2 = remain - arr[f]
            for s in range(f+1, 9):
                if arr[s] == remain2:
                    ans = arr[:f] + arr[f+1:s] + arr[s+1:]
                    for element in ans:
                        print(element)
                    return

search(arr)