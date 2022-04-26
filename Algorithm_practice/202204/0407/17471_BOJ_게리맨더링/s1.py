# 서로 인접한 노드라고 해서 같은 구역은 아니다. -> 1 - 2 - 3 이면 1-2 / 1-3 / 1-2-3 이럴 수 있다.
import sys
sys.stdin = open('input1.txt')

# 0. 서로소 집합 관련 함수 만들기
def find_set(roots, x):
    while x != roots[x]:
        x = roots[x]
    return x
def make_union(roots, x, y):
    roots[find_set(roots, y)] = find_set(roots, x)


# 5. 같은 구역이 모두 연결되어 있는지 체크하는 함수
def check(numbers, region1, region2, cnt):
    # 5-1. 모든 구역이 1구역이나 2구역 하나로만 되어 있을 때
    if cnt == total or cnt == 0:
        return False
    else:
        roots = list(range(N + 1))
        # 5-2. 모든 노드를 돌면서 1구역, 2구역을 make_union으로 구분하기
        for i in range(1, N+1):
            if numbers[i] == 1:                             # 1구역
                for element in graph[i]:
                    if numbers[element] == 1:
                        make_union(roots, i, element)
            else:                                           # 2구역
                for element in graph[i]:
                    if numbers[element] == 0:
                        make_union(roots, i, element)

        # 5-3. 조합이 구역1과 구역2로 나눠져 있는지 확인하기
        # find_set을 했을 때, 같은 구역은 모두 같은 root여야 한다.
        ans = set()
        for r1 in region1:
            ans.add(find_set(roots, r1))
        if len(ans) > 1:
            return False

        ans = set()
        for r2 in region2:
            ans.add(find_set(roots, r2))
        if len(ans) > 1:
            return False
    return True


# 4. 부분집합 생성하면서 조건에 만족하는지 확인, 만족한다면 최솟값 갱신
def dfs(i, numbers, cnt, region1, region2):
    global min_ans
    global half_count
    # 4-3. 나름의 가지치기
    if half_count >= (2**N)//2:
        return
    # 4-2. 종료조건: 모든 숫자를 다 보았을 때 -> 최솟값 갱신
    if i == N+1:
        #print(numbers)
        half_count += 1
        if check(numbers, region1, region2, cnt):
            min_ans = min(abs(cnt - (total-cnt)), min_ans)
        return
    # 4-1. 진행 - 포함한다/안한다
    numbers[i] = 1
    dfs(i+1, numbers, cnt+people_N[i-1], region1+[i], region2)
    numbers[i] = 0
    dfs(i+1, numbers, cnt, region1, region2+[i])



# T = int(input())
# for tc in range(1, T+1):

# 1. input 받기
N = int(input())
people_N = list(map(int, input().split()))
total = sum(people_N)

# 2. graph 입력하면서 섬의 개수 세기 -> find_set, make_union 함수 사용해서 서로소 만들기
# 섬이 3개 이상이면 -1 출력
roots = list(range(N+1))
graph = [[]*(N+1) for _ in range(N+1)]          # 인접 리스트 형태로 만들기
for i in range(1, N+1):
    M, *adj = map(int, input().split())
    for element in adj:
        graph[i].append(element)
        make_union(roots, i, element)
        #print(numbers1)
ans = set()
for j in range(1, N+1):
    ans.add(find_set(roots, j))
if len(ans) > 2:
    print(-1)

# 3. 인접한 영역이 2개 이하이므로 2개의 구역으로 나눌 수 있다.
else:
    min_ans = 987654321
    numbers = [0]*(N+1)                         # 각 인덱스에 해당하는 숫자가 1구역인지 0구역인지 표시하는 배열
    numbers[0] = 2
    half_count = 0                              # 부분집합을 만드는 경우의 수를 절반만 할 것임 -> 어차피 나머지 절반은 반전되었으니까. (1100 == 0011)
    region1 = []
    region2 = []
    dfs(1, numbers, 0, region1, region2)

    if min_ans == 987654321:
        print(-1)
    else:
        print(min_ans)