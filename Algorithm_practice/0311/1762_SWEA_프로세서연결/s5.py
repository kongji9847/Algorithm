# 중복 순열(dfs 활용) 방법 사용해서 다 돌기 (-> N의 개수가 작으므로 가능하다.)
# stack과 while문을 이용해서 재귀함수처럼 사용하기 -> stack에 필요한 정보를 전부 넣어서 다니기(함수처럼)
# 시간 초과 있으므로 백트래킹 사용하기
from copy import deepcopy

delta = [(-1, 0), (1, 0), (0, 1), (0, -1)]
# data: 코어가 담긴 arr / cores: 코어 인덱스 모음
def connect(data, cores):
    # [현재 자리수, 전선길이, 코어수, 배열 상태]
    stack = [[0, 0, 0, data]]                                           # dfs에 사용할 stack 준비 -> 첫번째 코어부터 시작하기 위해 초기값을 넣어준다.
    ans = []                                                            # 결과값을 낼 통
    while stack:                                                        # stack에 더 이상 남은 값이 없어질 때까지
        v = stack.pop()                                                 # 가장 최근에 쌓인 요소를 stack에서 뽑는다.

        #3. 종료 조건
        if v[0] == len(cores):                                  # 뽑은 요소의 코어 자리가 코어의 총 개수를 넘어가면 결과값 처리를 해주고 continue 해주어서 다음 stack 요소를 본다.
            if not ans:                                         # 모든 자리수를 돌은 최초라면 ans에 넣어주고
                ans = v[1:3]
            else:                                               # 이미 ans에 기존의 값이 존재하면 1.코어의 개수 2.전선의 길이를 따져서 ans를 갱신한다.
                if ans[1] < v[2]:
                    ans = v[1:3]
                elif ans[1] == v[2] and ans[0] > v[1]:
                    ans = v[1:3]
            continue                                            # 아래 코드는 보지 않고 다음 stack 요소로 넘어간다.

        #2. 재귀 한창 진행 중
        r, c = cores[v[0]][0], cores[v[0]][1]                   # r, c에 해당 순서의 core 인덱스를 저장한다.
        for i in range(4, -1, -1):                              # 가장 최근에 삽입된 요소가 먼저 빠져나오므로 상하좌우가 없는 요소는 가장 나중에 빠져 나오도록 한다.
            arr = deepcopy(v[-1])                               # 해당 방향으로 가기 전에, arr를 복사한다. -> 2차원이므로 deepcopy 필요하다.
            flag = 1                                            # 가다가 중간에 끊기는지 아닌지를 체크하는 plag
            
            # 2-1. 해당 코어를 넣는 경우
            if i != 4:                                          # 이동이 가능한 core라면,
                nr, nc = r, c
                cnt = 0
                while 0 < nr < N-1 and 0 < nc < N-1:            # 인덱스 에러 나지 않게 (nr, nc가 최종적으로 끝에 닿을 수 있게) 반복하면서 이동한다.
                    nr += delta[i][0]
                    nc += delta[i][1]
                    if arr[nr][nc] == 0:                        # 갈 수 있으면 1로 표시해준다.
                        arr[nr][nc] = 1
                        cnt += 1
                    elif arr[nr][nc] != 0:                      # 막히면 plag에 체크를 해주고 이동을 멈춘다.
                        flag = 0
                        break

                if flag:                                                # 이동이 끝나고 plag가 살아있다면 전원에 도착한 것!
                    stack.append([v[0]+1, v[1]+cnt, v[2]+1, arr])       # stack에 해당 정보를 재귀함수를 호출하는 것처럼 삽입한다.
            
            # 2-2. 해당 코어를 넣지 않는 경우 -> 백트래킹
            else:
                if ans and ans[1] == len(cores):                        # ans가 존재하면서, 기존 ans에 입력된 core수가 core의 총 개수와 동일하다면
                    continue                                            # 해당 경우는 stack에 넣지 않아 추후 발생할 많은 경우의 수를 줄인다.
                else:
                    stack.append([v[0] + 1, v[1], v[2], arr])           # 그렇지 않다면 재귀함수에 자리수만 한칸 올려서 추가하기

    return ans[0]

#1. input 입력 받기
import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]

    # 코어에 해당하는 index 추출하기 -> 가장자리에 있는 core는 안 봄
    cores = []
    for r in range(1, N-1):
        for c in range(1, N-1):
            if data[r][c] == 1:
                data[r][c] = 2
                cores.append([r, c])
    print(f'#{tc}', connect(data, cores))