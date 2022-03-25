import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M, K, A, B = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    k = list(map(int, input().split()))

    reception_desk = [0] * N
    repair_desk = [0] * M
    waiting = []

    cnt = 0
    t = 0
    while cnt < K:
        # 3. 대기열 ~ 장비 창구
        waiting.sort()
        for l in range(M):
            if repair_desk[l]:
                if repair_desk[l] == b[l]:
                    repair_desk[l] = 0
                    cnt += 1
                else:
                    repair_desk[l] += 1

        if waiting and 0 in repair_desk:
            for m in range(min(repair_desk.count(0), len(waiting))):
                indx = repair_desk.index(0)
                repair_desk[indx] = 1
                [p1, p2, p3] = waiting.pop(0)
                k[p3].append(indx+1)

        # 2. 접수 창구 ~ 대기열
        for j in range(N):
            if reception_desk[j]:
                if reception_desk[j][0] == a[j]:
                    waiting.append([t, j, reception_desk[j][1]])
                    reception_desk[j] = 0
                else:
                    reception_desk[j][0] += 1

        # 1. 고객 도착 ~ 접수 창구
        for i in range(K):
            if type(k[i]) == int and k[i] <= t:
                if 0 in reception_desk:
                    recept_num = reception_desk.index(0)
                    reception_desk[recept_num] = [1, i]
                    k[i] = [recept_num + 1]

        t += 1

    ans = 0
    for q in range(K):
        if k[q] == [A, B]:
            ans += q+1
    if ans == 0:
        print(f'#{tc}', -1)
    else:
        print(f'#{tc}', ans)


