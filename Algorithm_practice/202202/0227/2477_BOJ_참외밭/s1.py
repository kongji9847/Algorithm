import sys
sys.stdin = open('input.txt')
# 밭의 모양에 따라 두번씩 가는 방향이 다르다 -> ex) ㄱ자는 3, 1을 두번 돈다
N = int(input())
arr = [tuple(map(int, input().split())) for _ in range(6)]

# 두번 가는 곳 세주기
counts = [0, 0, 0, 0]
for element in arr:
    if element[0] == 1:
        counts[0] += 1
    elif element[0] == 2:
        counts[1] += 1
    elif element[0] == 3:
        counts[2] += 1
    else:
        counts[3] += 1

# 임의의 점부터 반시계 방향으로 돌기 때문에 반복되는 수열 구조 -> 어디에서 시작하던 인덱스 에러가 나지 않게 원형 순환 구조 만들기
circle = arr + arr
#print(circle)

# 경우 나누기
if counts[0] == counts[2] == 2:             # 3, 1 -> 423(13)1
    for i in range(12):
        if circle[i][0] == 4:
            ans = (circle[i][-1] * circle[i+1][-1]) - (circle[i+3][-1] * circle[i+4][-1])
            print(ans*N)
            break

elif counts[0] == counts[3] == 2:           # 4, 1 -> (41)4231
    for i in range(12):
        if circle[i][0] == 2:
            ans = (circle[i][-1] * circle[i+1][-1]) - (circle[i+3][-1] * circle[i+4][-1])
            print(ans*N)
            break

elif counts[1] == counts[3] == 2:           # 2, 4 -> 4(24)231
    for i in range(12):
        if circle[i][0] == 3:
            ans = (circle[i][-1] * circle[i+1][-1]) - (circle[i+3][-1] * circle[i+4][-1])
            print(ans*N)
            break

else:                                       # 2, 3 -> (2)3142(3)
    for i in range(12):
        if circle[i][0] == 1:
            ans = (circle[i][-1] * circle[i+1][-1]) - (circle[i+3][-1] * circle[i+4][-1])
            print(ans*N)
            break
