# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # Implement your solution here
    if len(A)<2: fib=[0]*2
    else: fib=[0]*(len(A)+1)
    fib[0] = 1
    fib[1] = 2
    fs = 2
    while(fib[fs - 1] <= len(A)):
        fib[fs] = fib[fs - 1] + fib[fs - 2]
        fs+=1

    result = -1
    for i in range(len(A)+1):
        if (i == len(A) or A[i] == 1):
            min_v = 2**31
            # O(log(n)) because it goes through Fibonacci numbers before n
            # And the number of them = O(log(n))
            for j in range(fs):
                if fib[j]>i+1: break
                start = i - fib[j]
                if (start == -1):
                    min_v = 1
                elif (A[start] > 0):
                    if (A[start] + 1 < min_v):
                        min_v = A[start] + 1
            if (i < len(A)):
                if (min_v == 2**31):
                    A[i] = 0
                else:
                    A[i] = min_v
            else:
                if (min_v != 2**31):
                    result = min_v

    return result


A = [0,0,0,1,1,0,1,0,0,0,0]
print(solution(A))