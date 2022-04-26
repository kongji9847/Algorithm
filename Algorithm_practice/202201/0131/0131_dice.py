# 첫 번째 주사위에서 모든 것이 결정된다. ->  6가지 경우의 수를 고려하자
# 맞은 편 주사위 인덱스를 찾아주는 함수
def across(indx):
    if not indx % 2:
        return indx + 1
    else:
        return indx - 1

def dices(n):
		# A-F B-D C-E 주사위 배열 바꾸기 
    dice_box = []
    for _ in range(n):
        dice = list(map(int, input().split(' ')))
        new_dice = [dice[0], dice[5], dice[1], dice[3], dice[2], dice[4]]
        dice_box.append(new_dice)

		# 첫번째 주사위에서 바닥에 닿을 면 선택 - 1~6까지 모든 경우를 고려하기(반복문)
    result = []
    for id in range(6):
				# 첫번째 주사위부터 마지막 주사위까지 바닥과 만날 면 찾고, 
        # 각 주사위의 옆면에서 가장 큰 수를 더하는 과정 반복
        max_box = 0
        for i in range(0, n):
            front_id = across(id)
        
            count_dice = dice_box[i][:]
            count_dice.remove(dice_box[i][id])
            count_dice.remove(dice_box[i][front_id])

            max_box += max(count_dice)
						# 마지막 인덱스에 도달했을 때, 위에 쌓을 주사위의 바닥면 찾는 것 중지
            if i == n-1:
                break
            id = dice_box[i+1].index(dice_box[i][front_id])
				# 각 경우의 최댓값들을 리스트로 모으기
        result.append(max_box)
    return max(result)

print(dices(int(input())))