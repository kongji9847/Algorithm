delta = [(0, -1), (1, 0), (0, 1), (-1, 0)]
magic_delta = [(0, 0), (-1, 0), (1, 0), (0, -1), (0, 1)]

# 3-3. 구슬 폭발하는 함수
def bomb():
    global marble_data
    # 1) 연속된 터뜨릴수 있는 구슬은 계속 확인하며 터뜨리기
    while True:
        now_marble = 0                  # 구슬 번호가 바뀌었는지 확인하는 checker
        cnt = 1                         # 현재 연속된 구슬 개수
        new_marble_data = []            # 파괴되고 남은 구슬을 담을 공간
        flag = 0                        # 더이상 터뜨릴 만한 구슬이 있는지 확인하기

        # 2) 모든 구슬을 확인하며 연속된 구슬이 4개 이상일 때 구슬 제거하기
        for i in range(len(marble_data)):

            # 그 전 구슬번호와 현재 확인한 구슬번호가 같은지 확인하기
            if now_marble != marble_data[i]:                        # 구슬 번호가 바뀌었다면
                if cnt >= 4:                                        # 그 전에 연속된 구슬의 개수가 4이상인지 체크하고
                    flag = 1                                        # 구슬에 변화가 있으므로 flag 체크
                    for _ in range(cnt):                            # 연속된 구슬 모두 폭발시키기
                        marbles[new_marble_data.pop()-1] += 1       # 폭발시킨 구슬 개수 카운팅하기

                now_marble = marble_data[i]                         # 이제 현재의 구슬이 checker가 된다.
                cnt = 1                                             # 연속된 구슬 개수 초기화
                new_marble_data.append(marble_data[i])              # 새로운 구슬을 담을 공간에 현재 구슬 담기

            else:                                                   # 구슬 체커와 구슬 번호가 동일하다면
                cnt += 1                                            # 연속된 구슬의 개수 갱신
                new_marble_data.append(marble_data[i])              # 새로운 구슬 담기

        marble_data = new_marble_data           # 한 cycle이 끝나고 기존의 marble_data를 새로운 구슬들을 담을 통으로 바꾸기

        # 3) 더이상 폭발시킬 구슬이 없다면
        if flag == 0:
            if cnt >= 4:                        # [1, 1, 2, 2, 2, 2]와 같이 마지막에서 연속인 구슬이 여러개가 나온다면
                for _ in range(cnt):            # 마지막 처리해주기
                    marbles[new_marble_data.pop() - 1] += 1
            return                               # while True문 중지

# 3-4. 연속된 그룹들을 확인하고 새로운 구슬 생성하기
def last_magic():
    # 1) 연속된 그룹 정보 확인
    groups = [0]                                # 인덱스 맞추기 위해 0을 dummy로 집어 넣기
    now_marble = 0                              # 연속된 번호 확인하기 위한 체커
    for i in range(len(marble_data)):           # 구슬들을 하나씩 확인하면서
        if now_marble != marble_data[i]:        # 구슬의 연속이 끊겼을 때
            groups.append([marble_data[i], 1])  # group에 새로운 구슬 그룹 정보 집어넣고
            now_marble = marble_data[i]
        else:                                   # 구슬이 계속 연속되었다면 구슬 개수 갱신
            groups[-1][1] += 1

    # 2) 그룹 정보를 확인하면서 새로운 구슬 배열 만들기 -> 2차원 배열에 저장하기(tonado사용해서)
    for j in range(1, len(groups)):
        if j * 2 > N**2:
            break
        firstr = tonado[j*2 - 1][0]
        firstc = tonado[j * 2 - 1][1]
        secondr = tonado[j * 2][0]
        secondc = tonado[j * 2][1]

        data[firstr][firstc] = groups[j][1]
        data[secondr][secondc] = groups[j][0]




# T = int(input())
# for tc in range(1, T+1):

# 1. input 받기
N, M = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(N)]
marbles = [0, 0, 0]


# 2. 토네이도 인덱스 만들기
# tonado => 구슬이 이동하는 방향을 알려주는 네비게이터
sr = sc = tr = tc = N//2                    # 상어의 위치 = 시작 지점
tonado = [(tr, tc)]
direction = 0
standard_length = 2
now_length = 0

while not (tr == 0 and tc == 0):
    tr += delta[direction][0]
    tc += delta[direction][1]
    now_length += 1
    tonado.append((tr, tc))

    if now_length == standard_length//2 or now_length == standard_length:
        direction = (direction + 1) % 4
        if now_length == standard_length:
            now_length = 0
            standard_length += 2


# 3. 마법을 반복해서 시전
for _ in range(M):
    # 3-1. 얼음 던져서 구슬 파괴하기
    magic_direction, magic_speed = map(int, input().split())
    for speed in range(1, magic_speed+1):
        nr = sr + magic_delta[magic_direction][0] * speed
        nc = sc + magic_delta[magic_direction][1] * speed
        data[nr][nc] = 0

    # 3-2. 파괴된 구슬의 자리를 다음 구슬을 이동시켜 채우기
    marble_data = []
    for i in range(1, N ** 2):
        r = tonado[i][0]
        c = tonado[i][1]
        if data[r][c]:
            marble_data.append(data[r][c])

    # 3-3. 연속된 그룹의 구슬 폭파시키기
    bomb()

    # 3-4. 새로운 구슬 생성 -> data에 담기 -> 이 data는 다음 마법에서 사용된다.
    data = [[0] * N for _ in range(N)]
    last_magic()

# 4. 마법이 끝난 후 폭파된 구슬 계산해서 출력
print(marbles[0] + 2* marbles[1] + 3*marbles[2])
