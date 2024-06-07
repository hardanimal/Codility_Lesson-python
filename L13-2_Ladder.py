# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, B):
    # Implement your solution here
    # for a given N rungs, the number of different ways of climbing is the (N+1)th
    # element in the Fibonacci numbers.
    # we know that the result of a number modulo 2^P is the bit under P, so
    # if we first let the number modulo 2^Q(Q > P) and then modulo 2^P, the
    # result is the same.
    L = len(A)
    fib = [0]*(L + 2)
    result = [0]*(L)
    fib[1] = 1
    fib[2] = 2
    for i in range(3, L+1):
            # make sure the fibonacci number will not exceed the max integer in java 1<<n =
            # 2^n
            fib[i] = (fib[i - 1] + fib[i - 2]) % (1 << 30)
    for i in range(L):
            result[i] = fib[A[i]] % (1 << B[i])
    return result


A = [4,4,5,5,1]
B = [3,2,4,3,1]
print(solution(A, B))