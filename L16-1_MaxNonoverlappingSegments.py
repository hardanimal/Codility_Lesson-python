# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, B):
    # Implement your solution here
    N=len(A)
    if N<=1: return N

    cnt=1
    prev_end=B[0]

    for curr in range(1, N):
        if (A[curr]>prev_end):
            cnt+=1
            prev_end=B[curr]
    return cnt


A = [1,3,7,9,9]
B = [5,6,8,9,10]
print(solution(A, B))