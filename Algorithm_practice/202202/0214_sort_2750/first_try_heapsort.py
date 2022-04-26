# import sys
# sys.stdin = open('input.txt')
from collections import deque
ans = deque()

def heapsort(arr):
    N = len(arr)                                                # 최대 힙 만들기 -> 각각의 트리 높이에 삽입 정렬을 통해
    for i in range(1, N):                                       # 부모 노드와 비교를 할 것이기 때문에 인덱스 1부터!
        while i > 0:                                            # 인덱스 0에 닿을 때까지 반복
            parent = (i-1)//2                                   # 자식 노드가 3, 4라면 부모 노드는 1
            if arr[i] > arr[parent]:
                arr[i], arr[parent] = arr[parent], arr[i]
            i = parent
    # print(arr)

# 마지막 노드가 홀수면 안돌아간다.
# 마지막 노드의 인덱스가 13(first)이면: second:14 == len(arr):14
    for _ in range(N):                                          # arr안의 모든 수(N개)를 차례로 빼서 덱에 저장한다.
        arr[0], arr[-1] = arr[-1], arr[0]                       # root 노드와 가장 끝에 있는 자손 노드 교환
        ans.appendleft(arr.pop())                               # 가장 끝에 있는 자식 노드(최댓값) 빼서 덱에 저장
        parent = 0                                              # 루트 노드 0부터 건드린 자손 순으로 차례로 내려온다.
        first, second = 1, 2
        while second < len(arr):                                # 가장 마지막 자식이 마지막 인덱스 크기보다 크면 안된다.
            max_child = first                                   # 자식 중 가장 큰 자식 찾기
            if arr[max_child] < arr[second]:
                max_child = second
            if arr[parent] < arr[max_child]:                    # 가장 큰 자식과 부모 비교하기
                arr[parent], arr[max_child] = arr[max_child], arr[parent]

            parent = max_child                                  # 가장 큰 자식이 부모보다 크던 작던 부모는 내려와서 while문을 탈출해야하므로
            first, second = (parent + 1)*2 - 1, (parent + 1)*2  # 부모를 가장 큰 자식으로 바꾸고 그에 따른 자식도 지정해준다.
        # print(arr)
    return ans


# a = heapsort([68, 5, 44, 17, 63, 29, 78, 49, 66, 45, 29])
# print(a)