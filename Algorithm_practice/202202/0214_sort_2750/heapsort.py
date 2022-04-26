import sys
# sys.stdin = open('input.txt')
from collections import deque

def heapsort(arr):
    # 최대힙 만들기
    N = len(arr)                                                                # 최대 힙 만들기 -> 각각의 트리 높이에 삽입 정렬을 통해
    for i in range(1, N):                                                       # 부모 노드와 비교를 할 것이기 때문에 인덱스 1부터!
        while i > 0:                                                            # 인덱스 0에 닿을 때까지 반복
            parent = (i - 1) // 2                                               # 자식 노드가 3, 4라면 부모 노드는 1
            if arr[i] > arr[parent]:
                arr[i], arr[parent] = arr[parent], arr[i]
            i = parent
        # print(arr)
    # pop 과정
    ans = deque()
    for _ in range(N):                                                          # arr안의 모든 수(N개)를 차례로 빼서 덱에 저장한다.
        arr[0], arr[-1] = arr[-1], arr[0]                                       # root 노드와 가장 끝에 있는 자손 노드 교환
        num = arr.pop()
        ans.appendleft(num)                                                     # 가장 끝에 있는 자식 노드(최댓값) 빼서 덱에 저장
        parent = 0                                                              # 루트 노드 0부터 건드린 자손 순으로 차례로 내려온다.
        first = 1                                                               # 자식 노드는 우선 무조건 홀수가 포함되어 있다. -> 첫째는 홀수 둘째는 짝수
        while first <= len(arr)-1:                                              # 가장 마지막 자식이 마지막 인덱스 크기보다 크면 안된다.
            second = first + 1                                                  # 둘째 자식 노드 만들어주기
            max_child = first                                                   # 자식 중 가장 큰 자식 찾기(최대 자식은 첫째 자식으로 우선 할당)
            if (second <= len(arr)-1) and arr[max_child] < arr[second]:         # 둘째 자식이 존재하고 첫째보다 둘째가 크다면
                max_child = second
            if arr[parent] < arr[max_child]:                                    # 가장 큰 자식과 부모 비교하기
                arr[parent], arr[max_child] = arr[max_child], arr[parent]

            parent = max_child                                                  # 가장 큰 자식이 부모보다 크던 작던 부모는 내려와서 while문을 탈출해야하므로
            first = (parent + 1) * 2 - 1                                        # 부모를 가장 큰 자식으로 바꾸고 그에 따른 자식도 지정해준다.
        # print(arr)
    return ans

a = heapsort([68, 5, 44, 17, 63, 29, 78, 49, 66, 45, 29])
print(a)

li = []
# for _ in range(int(sys.stdin.readline().strip())):
#     li.append(int(sys.stdin.readline().strip()))
for _ in range(int()):
    li.append(int())
a = heapsort(li)
for element in a:
    print(element)