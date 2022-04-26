# 스위치 함수
def switch(state, idx):
    if state[idx] == 0:
        state[idx] = 1
    elif state[idx] == 1:
        state[idx] = 0

# 남자 switch
def man(state, num):
    for num_m in range(len(state)):
        if not (num_m + 1) % num:
            switch(state, num_m)

# 여자 switch
def woman(state, num):
    # 여자가 고른 숫자가 왼쪽, 오른쪽 중 어디와 가까운지 확인하고 범위 고르기
    repeat = min(len(state)-num, num-1)
    switch(state, num-1)
    # 중심과 한 칸씩 떨어져서 회문인지 확인-> 회문이라면 스위치 해주기
    for k in range(1, repeat+1):
        if state[(num-1)-k] == state[(num-1)+k]:
            switch(state, (num-1)-k)
            switch(state, (num-1)+k)
        # 회문이 아니라면 즉시 반복 종료
        else:
            break

# 위의 함수 이용해서 스위치 상태를 반환하는 함수 만들기
def switch_state(n, state, person, info):

    for indx in range(person):

        if info[indx][0] == 1:
            man(state, info[indx][1])

        elif info[indx][0] == 2:
            woman(state, info[indx][1])
    
    str_state = list(map(str, state))
    ans = ' '.join(str_state)

    # 결과값 내기
    # 20보다 작으면 한 줄만
    if n <= 20:
         return ans
    
    # 20보다 크면 반복문 써서 한 줄씩 띄우기
    answer = ''
    for id in range(1, n//20+1):
        answer = answer + ans[(id-1)*40 : id*40-1] + '\n'
        remain = ans[id*40 : ]
    return (answer + remain).rstrip()

N = int(input())

state_list = list(map(int, input().split(' ')))

person = int(input())

working = []
for i in range(person):
    int_tuple = tuple(map(int, input().split(' ')))
    working.append(int_tuple)

print(switch_state(N, state_list, person, working))