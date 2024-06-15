# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(K, A):
    # Implement your solution here
    N=len(A)
    cnt=0
    sum_A=0

    for i in range(N):
        sum_A+=A[i]
        if sum_A>=K:
            cnt+=1
            sum_A=0
    return cnt


K = 4
A = [1,2,3,4,1,1,3]
print(solution(K, A))