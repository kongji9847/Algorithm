import sys
sys.stdin = open('input.txt')

for tc in range(4):
    arr = list(map(int, input().split()))
    arr_r = []

    for i in range(2):
        if arr[4+i] < arr[0+i]:
            if arr[6+i] < arr[0+i]:
                arr_r.append('-')
            elif arr[6+i] == arr[0+i]:
                arr_r.append('-o')
            elif arr[0+i] < arr[6+i]:
                arr_r.append('--')

        elif arr[4+i] == arr[0+i]:
            arr_r.append('--')

        elif arr[0+i] < arr[4+i]:
            if arr[2+i] < arr[4+i]:
                arr_r.append('-')
            elif arr[2+i] > arr[4+i]:
                arr_r.append('--')
            elif arr[2+i] == arr[4+i]:
                arr_r.append('-o')

    if '-' in arr_r:
        print('d')

    elif '-o' in arr_r:
        if '--' in arr_r:
            print('b')
        else:
            print('c')
    else:
        print('a')