import sys
sys.stdin = open('input.txt')

def find_set(x):
    while x != numbers[x]:
        x = numbers[x]
    return x

def make_union(x, y):
    p[find_set(y)] = find_set(x)


def check(numbers):
    elements1 = []
    cnt1 = 0
    elements2 = []
    cnt2 = 0

    for j in range(1, N+1):
        if numbers[j] == 1:
            elements1.append(j)
            cnt1 += people_N[j+1]
        else:
            elements2.append(j)
            cnt2 += people_N[j-1]

    if cnt1 == total or cnt2 == total:
        return False
    else:
        for element in elements1:





def dfs(i, numbers):
    if i == N+1:
        print(numbers)
        return
    numbers[i] = 1
    dfs(i+1, numbers)
    numbers[i] = 0
    dfs(i+1, numbers)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    people_N = list(map(int, input().split()))
    total = sum(people_N)

    graph = [[]*(N+1) for _ in range(N+1)]
    for i in range(1, N+1):
        M, *adj = map(int, input().split())
        for element in adj:
            graph[i].append(element)
    numbers = [0]*(N+1)
    numbers[0] = 2
    dfs(1, numbers)