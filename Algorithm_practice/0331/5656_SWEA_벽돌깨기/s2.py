import sys
sys.stdin = open('input.txt')
from copy import deepcopy

# 3. 상하좌우로 block이 깨지는 경우
delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]
def shoot(width, height, length, blocks):
    # 기준점 block에 체크한다.
    blocks[width][height] = '*'
    should_change.append((height, width))                       # height를 기준으로 배열하므로 height를 앞으로 담기

    for i in range(4):
        nw, nh = width, height
        for j in range(length-1):
            nw += delta[i][0]
            nh += delta[i][1]
            if 0 <= nw < W and 0 <= nh < H:                     # 인덱스를 벗어나지 않는다면,
                if blocks[nw][nh] == 1:                         # 연속 터짐이 아닌 경우, 깨져야하는 block에 *을 체크한다.
                    blocks[nw][nh] = '*'
                    should_change.append((nh, nw))
                elif blocks[nw][nh] != '*' and blocks[nw][nh] != 0:     # 연속 터짐이고 깨짐 표시가 안되어 있는 경우
                    shoot(nw, nh, blocks[nw][nh], blocks)               # 다시 상하좌우로 block이 깨져야 하므로 shoot을 재귀 호출한다.


# 2. dfs로 모든 경우를 보면서 게임 진행하기
# used_chance: 사용한 기회, blocks_popped: 깨진 블럭 누적 개수, blocks: 블럭 배열
def dfs(used_chance, blocks_popped, blocks):
    global max_pop

    # 종료조건
    if total - blocks_popped == 0 or used_chance == N:
        if max_pop < blocks_popped:
            max_pop = blocks_popped
        return

    # 2-1. 진행
    for col in range(W):                                                    # 열 하나씩 탐색
        for row in range(H-1, -1, -1):                                      # 맨 위의 블럭부터 보면서 깨뜨릴 수 있는지 확인 -> 깨뜨릴 수 있다면, 그 밑에 블럭은 보지 않는다.
            if blocks[col][row] != 0:
                new_blocks = deepcopy(blocks)                               # 블럭이 깨지면서 2차원 배열이 깨지니까 copy를 해준다. -> 원본 blocks은 다른 재귀에서도 쓰여야 하므로 보존

                # 2-1-1. 크기 1짜리 block 깨뜨리기 -> 그 위의 블럭이 아래로 내려올 일은 없다.
                if new_blocks[col][row] == 1:
                    new_blocks[col][row] = 0
                    # 다음 기회로 가서 확인하기
                    dfs(used_chance + 1, blocks_popped + 1, new_blocks)

                # 2-1-2. 크기 2 이상의 block 깨뜨리기 -> shoot 함수 써서 깨진 block 표시하기
                else:
                    shoot(col, row, blocks[col][row], new_blocks)
                    more_popping = len(should_change)                                   # shoot으로 인해 깨진 블록 개수
                    should_change.sort()                                                # sort해서 가장 위에 있는 블록이 맨 뒤로 오게 하기 -> pop()해서 뒤로 빼줄 것이므로
                    while should_change:                                                # should_change가 모두 없어질 때까지 block 깨뜨리기
                        height, width = should_change.pop()
                        new_blocks[width].pop(height)
                        new_blocks[width].append(0)
                    # 다음 기회로 가서 이어서 게임 진행하기
                    dfs(used_chance+1, blocks_popped + more_popping, new_blocks)

                # block을 깨뜨렸다면 break해서 다음 block은 보지 않도록 만들기
                break


# 1. 입력받기
T = int(input())
for tc in range(1, T+1):
    N, W, H = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(H)]

    # 1-1. 같은 열끼리 묶어 새로운 2차원 리스트로 나타내주고, 블록의 맨 꼭대기가 오른쪽에 위치하게 하기
    blocks = [zip(*data)]
    blocks = [map(reversed, *blocks)]
    blocks = list(map(list, *blocks))

    # 1-2. 게임 시작 전, 블록의 총 개수 구하기
    total = 0
    for row in range(W):
        for col in range(H):
            if blocks[row][col] != 0:
                total += 1
    # 1-3. block 깨기 시작
    max_pop = 0                                         # 깨뜨린 block의 max값 구하기
    should_change = []                                  # block을 한 개 이상 깨뜨렸을 때, 깨뜨린 블럭의 인덱스를 담을 통
    dfs(0, 0, blocks)
    print(f'#{tc}', total - max_pop)

