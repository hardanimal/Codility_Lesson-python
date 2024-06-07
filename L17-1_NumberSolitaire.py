# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # Implement your solution here
    dp = [0]*len(A)
    dp[0]=A[0]

    for i in range(1, len(A)):
        max_A = -2**31

        for die in range(1, 7):
            if (i-die)>=0:
                max_A=max(dp[i-die]+A[i], max_A)
        dp[i]=max_A
    return dp[len(A)-1]


A = [1,-2,0,9,-1,-2]
print(solution(A))