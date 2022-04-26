import sys
sys.stdin = open('input.txt')
# 원자의 출발 위치를 보고 원자끼리 만날 수 있는 최대 거리를 유추해서 그만큼만 반복문 돌리기
# 시간은 모든 원자가 동일하게 흘러간다.
# x.5초, x.0초 대에서만 만날 수 있다 -> 2배로 확장하기
# 제한시간 초과 -> 유망하지 않은 것은 세부 반복문 돌리지 않기(백트래킹)

def collision(data):
    sum_e = 0
    delta = [(0, 1), (0, -1), (-1, 0), (1, 0)]      # 상하좌우
    for _ in range(4002):                           # 2001초 동안 돌려도 충돌이 나오지 않는 것은 무한번 돌려도 나올 수 없다. -> 원자끼리 만날 수 있는 최대 거리: 2001
        togo = []                                   # 겹치는 요소가 있는지 확인해 줄 요소
        for element in data:                        # data에서 원소 하나를 뽑아서 1초 흘러감에 따라 이동시켜주기
            d = delta[element[3]]
            element[1] += d[0]
            element[2] += d[1]
            togo.append((element[1], element[2]))   # 이동한 좌표를 togo에 넣어주기 -> 추후 set으로 중복 제거
        if len(set(togo)) == len(data):             # 좌표의 개수가 data의 개수와 같다는 것은 겹치는 좌표가 아무것도 없다는 뜻 -> 아래로 내려가지 않기
            continue

        visited = [0] * len(data)                   # 중복된 요소 체크하기
        for f in range(len(data)-1):                # 이중 반복문으로 서로 같은 원자 찾기
            if visited[f] == 1:                     # 이미 중복된 요소로 판명 나면 다음 숫자로 바로 넘어가기
                continue
            for s in range(f+1, len(data)):
                if visited[s] == 1:
                    continue
                else:
                    if (data[f][1] == data[s][1] and data[f][2] == data[s][2]):         # 중복이라면 visited에 체크
                        visited[f] = 1
                        visited[s] = 1
        new_data = []                           # 중복이 되어 있지 않은 data 담아서 다음 data로 넘겨주기
        for i in range(len(visited)):
            if visited[i] != 1:
                new_data.append(data[i])
            else:
                sum_e += data[i][4]                 # energy 합 구해주기
        if new_data:                                # 중복된 요소가 모두 빠져서 남은 data가 아예 없을 수도 있다.
            data = new_data
        else:                                       # 남은 data 없으면 break
            break
    return sum_e



T = int(input())
for tc in range(1, T+1):
    N = int(input())
    data = []
    for i in range(N):
        x, y, dr, k = map(int, input().split())
        data.append([i, x*2, y*2, dr, k])                           # x.5초 때에서 만나는 것도 있으니까 애초에 두배로 평면 확장해주기
    print(f'#{tc}', collision(data))