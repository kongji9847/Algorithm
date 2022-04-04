import sys
sys.stdin = open('input.txt')

from collections import deque
# 1. 16진수를 10진수로
def hexadecimal_to_dec(number):
    ans = 0
    for i in range(len(number)-1, -1, -1):
        if number[i] in '0123456789':
            ans += int(number[i])*(16**(len(number)-1-i))
        else:
            ans += (ord(number[i]) - ord('A') + 10)*(16**(len(number)-1-i))
    return ans

# 2. 비밀번호 찾기
def solution(N, K):
    nums = set()                            # 중복 방지 위해 set에 넣어주기
    M = N//4                                # M = 회전수, 비밀번호 자리수
    for _ in range(M):
        for i in range(0, N, M):            # 각 변 하나씩 숫자 확인
            ans = ''
            for j in range(M):
                ans += numbers[i+j]
            num = hexadecimal_to_dec(ans)
            nums.add(num)

        rot = numbers.popleft()             # 1회전 하기 -> Q의 특성 사용(deque 사용)
        numbers.append(rot)
    nums = list(nums)                       # 모든 회전이 끝난 후, 얻은 숫자 set을 list로 변경해 내림차순으로 sort하기
    nums.sort(reverse=True)
    return nums[K-1]


T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    numbers = deque(input())
    print(f'#{tc}', solution(N, K))