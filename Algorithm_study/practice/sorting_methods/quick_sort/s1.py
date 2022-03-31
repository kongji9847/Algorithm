# 퀵 정렬

# 2. 분할해서 pivot 기준으로 pivot보다 작은 것은 왼쪽으로, pivot보다 큰 것은 오른쪽으로 넣기
def partition(start, end):
    # 2-1. pivot 지정 - 왼쪽 끝으로 지정
    pivot = quick_nums[start]
    low = start + 1
    high = end

    # 2-2. low high 엇갈릴 때까지 반복
    while True:                                                         # low와 high가 엇갈려 있지 않고,
        while low <= high and quick_nums[low] <= pivot:                 # 각 세부 반복문을 돌면서 low는 pivot보다 큰 수가 나올 때까지 오른쪽으로 이동
            low += 1
        while low <= high and quick_nums[high] >= pivot:                # high는 pivot보다 작은 수가 나올 때까지 왼쪽으로 이동
            high -= 1

        # Q) low == high 이유: 엇갈리는 순간을 만들기 위해,
        # Q) quick_nums[low] == pivot 허용한 이유: pivot과 동일한 것들이, low, high로 의미없이 서로 교환되는 것을 막기 위해


        # 2-3. 세부 while 문이 멈추고, 엇갈려 있다면 바깥 while을 빠져 나오고
        if low > high:
            break
        # 엇갈려 있지 않으면 low와 high를 서로 교환해준다. -> 엇갈린 상황에서 low high를 교환해주면 정렬을 한 것들이 망가진다.(10 22 -> 22 10)
        else:
            quick_nums[low], quick_nums[high] = quick_nums[high], quick_nums[low]

    # 2-4. 엇갈린 상태에서 pivot 값과 high 값을 교환(엇갈려 있으므로 high가 low보다 작다 -> high를 pivot과 바꾼다.)
    quick_nums[start], quick_nums[high] = quick_nums[high], quick_nums[start]

    # 2-5. 새로운 pivot의 위치를 반환 -> 이 숫자의 위치는 영구적으로 고정
    return high


# 1. start와 end 사이를 정렬하기
def quick_sort(start, end):
    # 1-1. start와 end가 엇갈리지 않을 때 sort 가능
    # start와 end가 같아도 되지만 어차피 partition 후에 pivot = start = end이 되므로 그 아래 코드에서 걸러진다.)
    if start < end:
        pivot = partition(start, end)
        quick_sort(start, pivot-1)                                  # pivot보다 작은 것들을 sort,
        quick_sort(pivot+1, end)                                    # pivot보다 큰 것들을 sort

quick_nums = [0, 55, 22, 33, 2, 1, 10, 26, 42]
quick_sort(0, len(quick_nums)-1)
print(quick_nums)