import copy
import sys
sys.stdin = open('input.txt')
# 세찬

def solution(n,map,core):
    stack = [(0,0,0,copy.deepcopy(map))]
    visit = []
    minlen = 9999
    maxcore = 0
    answer = []


    while stack:
        #idx, sumOfCoreCount, sumOfLine ,map
        idx,coreCount, lineLen, copiedMap = stack.pop()
        answer.append((coreCount,lineLen))
        if idx == len(core):
            continue

        currCoreidx, currCorejdx = core[idx]
        checks = 0

        for i in range(4):
            newCopyMap = copy.deepcopy(copiedMap)

            #right
            if i == 0:
                if 1 not in newCopyMap[currCoreidx][currCorejdx+1:]:
                    for j in range(currCorejdx+1,n):
                        newCopyMap[currCoreidx][j] = 1
                    stack.append((idx+1,coreCount+1,lineLen+n-currCorejdx-1,newCopyMap))
                    checks+=1
            #left
            elif i == 1:
                if 1 not in newCopyMap[currCoreidx][:currCorejdx]:
                    for j in range(0,currCorejdx):
                        newCopyMap[currCoreidx][j] = 1
                    stack.append((idx+1,coreCount+1,lineLen+currCorejdx,newCopyMap))
                    checks+=1
            #up
            elif i == 2:
                checkAboutBlock = True
                for j in range(currCoreidx):
                    if newCopyMap[j][currCorejdx] == 1:
                        checkAboutBlock = False
                        break
                if checkAboutBlock:
                    for j in range(currCoreidx):
                        newCopyMap[j][currCorejdx] = 1
                    stack.append((idx+1,coreCount+1,lineLen + currCoreidx,newCopyMap))

            #down
            else:
                checkAboutBlock = True
                for j in range(currCoreidx+1,n):
                    if newCopyMap[j][currCorejdx] == 1:
                        checkAboutBlock = False
                        break
                    if checkAboutBlock:
                        for j in range(currCoreidx+1,n):
                            newCopyMap[j][currCorejdx] =1
                        stack.append((idx+1,coreCount+1,lineLen+n-currCoreidx-1,newCopyMap))
                        checks+1

            if checks == 0:
                stack.append((idx+1,coreCount,lineLen,newCopyMap))

    answer.sort(key = lambda x:(-x[0],x[1]))
    print(answer)
    return answer[0][1]

def main():
    T = int(input())
    for tc in range(1, T + 1):
        N = int(input())
        arr = [list(map(int, input().split())) for _ in range(N)]
        core = []
        #find core except line
        for i in range(1,N-1):
            for j in range(1,N-1):
                if arr[i][j] == 1:
                    core.append((i,j))

        print(f'#{tc}', solution(N,arr,core))


main()