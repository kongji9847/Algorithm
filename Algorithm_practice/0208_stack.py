import sys
result = []
for _ in range(int(sys.stdin.readline().strip())):
    ans = sys.stdin.readline().strip().split(' ')
    if ans[0]=='push':
        result.append(int(ans[-1]))
    
    elif ans[0]=='top':
        if not result:
            print(-1)
        else: print(result[-1])
    
    elif ans[0] =='size':
        print(len(result))
    
    elif ans[0] =='empty':
        if not result:
            print(1)
        else: print(0)

    elif ans[0] == 'pop':
        if not result:
            print(-1)
        else: print(result.pop())
