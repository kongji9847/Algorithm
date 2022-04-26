import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M, K, A, B = map(int, input().split())
    reception = list(map(int, input().split()))
    repair = list(map(int, input().split()))
    clients = list(map(int, input().split()))

    reception_desk = [0] * N
    repair_desk = [0] * M
    waiting = []

    t = 0
    cnt = 0
    while cnt < K:                                                              # 모든 고객이 정비에 들릴 때까지 반복 -> 시간의 흐름에 따라
        # 1. 도착 -> 접수
        for i in range(K):
            if type(clients[i]) == int and clients[i] <= t:                     # 고객이 해당 시간 안에 도착했으면 접수처에 보낸다.
                if 0 in reception_desk:
                    reception_indx = reception_desk.index(0)
                    # 접수처에서 흐른 시간, 고객 번호
                    reception_desk[reception_indx] = [0, i]                     # 접수처에 가서 시간 증가했다는 것을 표현해야 하므로 0으로 표기
                    clients[i] = [reception_indx + 1]

        # 2. 접수 -> 정비 전 대기
        for j in range(N):
            if reception_desk[j]:
                reception_desk[j][0] += 1                                       # 접수처에서 시간이 흐른다. -> 새로운 고객의 시간은 0에서 1이 된다.

                if reception_desk[j][0] == reception[j]:                        # 시간 흐름 표시 후, 접수 완료가 되면 대기줄로 보낸다.
                    # 현재 시각, 접수처 번호, 고객 번호 -> 우선 순위에 따라
                    waiting.append([t, j, reception_desk[j][1]])
                    reception_desk[j] = 0

        # 3. 정비소(새로운 고객이 들어 오지 않은 정비소 -> 새로운 고객은 접수처에서 시간을 보냈으므로 시간 카운팅에 포함하지 않는다.)
        for k in range(M):
            if repair_desk[k]:                                                  # 정비소에서 시간이 흐른다.
                repair_desk[k][0] += 1

                if repair_desk[k][0] == repair[k]:                              # 정비가 끝난 고객은 나간다.
                    repair_desk[k] = 0

        # 4. 대기줄 -> 정비
        if waiting and 0 in repair_desk:                                        # 정비소의 남는 자리에 대기 고객들을 넣는다.
            num = min(len(waiting), repair_desk.count(0))
            for l in range(num):
                repair_indx = repair_desk.index(0)
                client = waiting.pop(0)[-1]
                repair_desk[repair_indx] = [0, client]                          # 대기 고객들은 접수처에서 시간을 보냈으므로 시간이 흘렀다고 표현하지는 않는다. -> 정비처의 자리만 채워 준다.
                clients[client].append(repair_indx + 1)
                cnt += 1

        t += 1

    # 답 내기
    ans = 0
    for c in range(K):
        if clients[c] == [A, B]:
            ans += c + 1

    if ans == 0:
        print(f'#{tc}', -1)
    else:
        print(f'#{tc}', ans)
