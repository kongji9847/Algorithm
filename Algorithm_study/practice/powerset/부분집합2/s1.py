#1.
# 집합 {1, 2, 3}의 모든 부분집합을 구하시오

arr = [1, 2, 3]   # 구하고자 하는 부분 집합
N = len(arr)      # arr의 길이
sel = [0] * N     # a 리스트 (내가 해당 원소를 뽑았는지 체크하는 리스트)

def powerset(idx):
    if idx == N:        # idx가 요소 전체 길이(N)와 같아 질 때 -> 모든 자리에 대한 선택을 완료 했을 때
        # print(*sel)     # 출력
        print(sel, ':', end=' ')
        for i in range(N):
            if sel[i]:
                print(arr[i], end=' ')
        print()
        return          # 혹은 조건 분기
    sel[idx] = 1        # sel의 idx번째 자리를 1로 바꾸고
    powerset(idx+1)     # idx 자리의 원소를 뽑고 진행
    sel[idx] = 0        # idx 자리의 원소를 뽑지 않고 진행
    powerset(idx+1)     # 더 수행 할 코드가 없으면 해당 함수를 호출한 곳으로 돌아가자

powerset(0)