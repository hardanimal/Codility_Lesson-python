# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # Implement your solution here
    # main idea:
    # using "dynamic programming" to build up the solution
    # (bottom up)
    if (len(A) == 0): return 0
    if (len(A) == 1): return A[0]

    sum_A = 0
    max_A = A[0]

    for i in range(len(A)):
            A[i] = abs(A[i])
            sum_A += A[i]
            max_A = max(A[i], max_A)

    count = [0]*(max_A + 1)
    for num in (A):
        count[num]+=1

    dp = [-1]*(sum_A + 1)
    dp[0] = 0
    for i in range(max_A+1):
            if (count[i] > 0):
                    for val in range(sum_A+1):
                            if (dp[val] >= 0):
                                    dp[val] = count[i]
                            elif (val >= i and dp[val - i] > 0):
                                    dp[val] = dp[val - i] - 1

    result = sum_A
    for i in range(int(sum_A/2)+1):
            if dp[i] >= 0:
                    result = min(result, sum_A - (2 * i))
    return result


A = [1,5,2,-2]
print(solution(A))