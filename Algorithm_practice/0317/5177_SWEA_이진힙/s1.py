def heap_push(value):
    global pointer
    pointer += 1
    tree[pointer] = value

    child = pointer
    parent = child // 2

    while tree[child] < tree[parent]:
        tree[parent], tree[child] = tree[child], tree[parent]

        child = parent
        parent = child // 2


import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    nums = list(map(int, input().split()))
    tree = [0] * (len(nums) + 1)

    # 새로운 원소 추가하면서 이진힙 만들기
    pointer = 0
    for num in nums:
        heap_push(num)

    # 노드 합 저장하기
    total = 0
    while pointer >= 1:
        total += tree[pointer//2]
        pointer //= 2

    print(f'#{tc}', total)