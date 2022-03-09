import sys
sys.stdin = open('input.txt')

for tc in range(4):
    arr = list(map(int, input().split()))
    arr_r = []

    for i in range(2):
        if arr[6+i] < arr[0+i] or arr[2+i] < arr[4+i]:                  # 만나지 않는 경우
            arr_r.append('-')
        elif arr[6+i] == arr[0+i] or arr[2+i] == arr[4+i]:              # 점에서 만나는 경우
            arr_r.append('o')
        else:                                                           # 나머지 -> 선끼리 만난다.
            arr_r.append('--')

# 결과값 내기
    if '-' in arr_r:                        # 만나지 않는 것이 하나라도 있으면 d 출력
        print('d')
    elif 'o' in arr_r:                      # 한 점에서 만나고
        if '--' in arr_r:                   # 겹치는 선분이 있으면 b 출력 -> 점 - 선
            print('b')
        else:                               # 한 점에서 만나고 겹치는 선분 없다면 c 출력 -> 점-점
            print('c')
    else:                                   # 나머지는 모두 선과 선이 만나 면이 된다.
        print('a')