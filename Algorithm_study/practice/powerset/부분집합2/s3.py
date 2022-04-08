#2-2. 다른 형태
# 집합 {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}의 부분 집합의 요소 중 합이 10이 되는 부분집합을 구하시오.
def power_set(arr, index, curr):
    if index == len(arr):
        if sum(curr) == 10:
            print(*curr)
        return

    power_set(arr, index+1, curr+[arr[index]])
    power_set(arr, index+1, curr)

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
power_set(arr, 0, [])