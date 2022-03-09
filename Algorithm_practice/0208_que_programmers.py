def solution(progresses, speeds):
    days = []
    for i in range(len(progresses)):
        count = 1
        while progresses[i] < 100:
            progresses[i] += speeds[i]
            count += 1
        days.append(count)
    
    stand = days[0]
    answer = [1]
    for day in range(1, len(days)):
        if days[day] <= stand:
            answer[-1] =  answer[-1] + 1
        else:
            stand = days[day]
            answer.append(1)
            
    return answer