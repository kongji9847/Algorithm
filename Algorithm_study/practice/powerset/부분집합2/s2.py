#2-1.
# 집합 {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}의 부분 집합의 요소 중 합이 10이 되는 부분집합을 구하시오.

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
N = len(arr)
sel = [0] * N

def powerset(idx):
    # 선택 x
    if idx < N:
        sel[idx] = 1
        powerset(idx+1)
        sel[idx] = 0
        powerset(idx+1)
    # 선택 o
    else:
        total = 0
        for i in range(N):
            if sel[i]:                              # 1로 표시가 되어 있다면
                total += arr[i]                     # 해당 요소(idx)를 total에 누적
        if total == 10:                             # 반복을 다 돌고 그 총합이 10인 경우는
            for i in range(N):                      # 반복 돌면서
                if sel[i]:                          # 선택된 요소를 출력
                    print(arr[i], end=' ')
            print()
            # for idx, num in enumerate(sel, start=1):# 반복을 돌며 1인 경우의 idx 값을 출력
            #     if num == 1:
            #         print(idx, end=' ')
            # print()

powerset(0)