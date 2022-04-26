# 새로운 리스트를 만들어서 리스트의 맨 끝 요소와 원래의 리스트 안의 요소를 하나씩 비교하여 추가하기
# return되는 새로운 리스트는 원소끼리 연속하지 않는다가 포인트!!
def lonely(my_list):
    
    # 원래 리스트의 첫번째 요소는 무조건 포함
    ans = [my_list[0]]
    
    # 원래 리스트의 2번째 요소부터 돌려보면서, 
    # 새로 만들어지는 리스트의 끝부분과 같은지 확인 -> 같다면 연속하는 것
    
    for i in range(1, len(my_list)):
        
        if my_list[i] != ans[-1]:
            ans.append(my_list[i])

    return ans

print(lonely([1, 1, 3, 3, 0, 1, 1]))
print(lonely([4, 4, 4, 3, 3]))