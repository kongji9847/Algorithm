# 병합 정렬

# 2. L, R 부분 리스트를 정렬하며 병합하기(Conquer & Combine)
def merge(L, R):
    # 2-1. L과 R의 0번째 인덱스부터 보면서 서로 비교해서 오름차순으로 merge_list에 집어 넣기
    merge_list = []
    L_indx = 0
    R_indx = 0

    # L이나 R 둘 중 하나가 전부 사용될 때까지 반복한다.
    while L_indx < len(L) and R_indx < len(R):
        if L[L_indx] >= R[R_indx]:
            merge_list.append(R[R_indx])
            R_indx += 1
        else:
            merge_list.append(L[L_indx])
            L_indx += 1

    # 2-2. L이나 R 둘 중 하나가 전부 사용되고 남은 것들을 집어 넣기
    if L_indx < len(L):
        merge_list += L[L_indx:]
    elif R_indx < len(R):
        merge_list += R[R_indx:]

    return merge_list


# 1. 분할하기(divide)
def partition(data):
    N = len(data)
    # 1-2. 종료조건 -> 더 이상 쪼갤 것이 없을 때
    if N <= 1:
        return data

    # 1-1. 진행
    L = partition(data[:N//2])
    R = partition(data[N//2:])

    # L과 R이 지정되면 merge하면서 조각을 정렬한다.
    return merge(L, R)                                  # merge한 결과는 아래의 재귀 스택으로 들어간다.

numbers = [0, 55, 22, 33, 2, 1, 10, 26, 42]
print(numbers)               # 정렬 전 [0, 55, 22, 33, 2, 1, 10, 26, 42]
print(partition(numbers))    # 정렬 후 [0, 1, 2, 10, 22, 26, 33, 42, 55]