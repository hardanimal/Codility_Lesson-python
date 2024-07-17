# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N):
    # Implement your solution here
    import math
    if N%2!=0: return 0
    cursor=0
    for i in range(math.ceil(math.log2(N))):
        print(i, 2**i, cursor, N%(2**i))
        if N%(2**i)!=0: cursor-=1; break
        cursor+=1
    return cursor


N=24
print(solution(N))