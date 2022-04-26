from collections import deque
# 괄호 찾기 탐색과 유사하지만 Q를 사용한다.
def solution(fees, records):
    ans = {}                                        # 여러번 출차하는 차가 있다. -> 리스트 대신 딕셔너리 사용한다.
    Q1 = deque([])
    Q2 = deque([])
    for element in records:                         # records에서 하나씩 뽑아서 확인하기
        car = element.split()
        if car[-1] == 'IN':                         # ( 이면 큐에 넣어준다.
            Q1.append(car)
        else:                                       # ) 이면 해당하는 (를 찾을 때까지 반복문을 돌린다.
            while True:
                car_in = Q1.popleft()               # 저장되어 있는 큐에서 하나씩 빼준다. -> 가장 먼저 온 것 부터 뺀다.
                # 1. 찾으면 분을 계산한다.
                if car[1] == car_in[1]:
                    minute = (int(car[0][:2])*60 + int(car[0][3:5])) - int(car_in[0][:2])*60 - int(car_in[0][3:5])
                    if int(car_in[1]) not in ans.keys():            # 딕셔너리에 있는지 없는지를 따져 해당 차 번호를 key로 하여 minute을 넣는다.
                        ans[int(car_in[1])] = minute
                    else:
                        ans[int(car_in[1])] += minute

                    Q1 = Q2 + Q1                                    # Q1을 다시 Q2와 합쳐 시간 순으로 갱신
                    Q2 = deque([])                                  # Q2 초기화
                    break                                           # while true문 탈출
                # 2. 못찾으면 Q2에 순서대로 넣어준다.
                else:
                    Q2.append(car_in)
    # record를 다 돌리면 out이 없는 친구들이 q1에 남는다.
    while Q1:
        car_out = Q1.popleft()
        minute = (23) * 60 + 59 - int(car_out[0][:2]) * 60 - int(car_out[0][3:5])
        if int(car_out[1]) not in ans.keys():
            ans[int(car_out[1])] = minute
        else:
            ans[int(car_out[1])] += minute
    # 요금 계산 -> 자동차 번호순대로
    answer = []
    for i in sorted(ans.keys()):
        minute = ans[i]
        if (minute - fees[0]) <= 0:
            fee = fees[1]
        else:
            if (minute - fees[0]) % fees[2]:
                ten_min = (minute - fees[0]) // fees[2] + 1
            else:
                ten_min = (minute - fees[0]) // fees[2]
            fee = fees[1] + (ten_min) * fees[3]
        answer.append(fee)
    return answer


fees = [180, 5000, 10, 600]
records = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]

print(solution(fees, records))