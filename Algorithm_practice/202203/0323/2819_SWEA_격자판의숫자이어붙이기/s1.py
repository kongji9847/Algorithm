# 7단계만 가면되고, Q를 두개 만들어 현재 단계와 다음단계의 영역을 구분해준다.

from collections import deque
delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]
def bfs(sr, sc):
    #cnt = 0 #: dfs와 연산량 비교 위해
    Q = deque([((sr, sc), str(data[sr][sc]))])

    for k in range(7):                                                          # 7번만 가면 된다.
        newQ = set()                                                            # 다음 단계의 노드를 담을 통 초기화
        while Q:                                                                # 현재 단계의 노드가 모두 사라질 때까지
            v, number = Q.popleft()
            if k == 6:                                                          # 종료조건
                answer.append(number)

            for i in range(4):
                nr = v[0] + delta[i][0]
                nc = v[1] + delta[i][1]
                if 0 <= nr < 4 and 0 <= nc < 4:
                    newQ.add(((nr, nc), number+str(data[nr][nc])))              # newQ에 다음단계를 담아준다.
                    #cnt += 1

        Q = deque(newQ)                                                                # 비워진 Q를 newQ로 채워준다.
    #print(cnt)


import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    data = [list(map(int, input().split())) for _ in range(4)]
    answer = []
    for r in range(4):
        for c in range(4):
            bfs(r, c)
    print(f'#{tc}', len(set(answer)))
