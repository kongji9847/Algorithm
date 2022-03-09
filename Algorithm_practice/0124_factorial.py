# N = int(input())
# total = 1
# if N == 0:
#     print(total)
    
# else:
#     for n in range(N, 0, -1):
#         total *= n
#     print(total)

def factorial(N):
    if N == 0:
        return 1
    elif N == 1:
        return 1
    else:
        return N * factorial(N-1)

n = int(input())
print(factorial(n))
    