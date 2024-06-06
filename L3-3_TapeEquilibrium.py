# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # Implement your solution here
    leftSum=A[0]
    rightSum=0
    for i in range(1, len(A)):
        rightSum+=A[i]
    min_gap = abs(leftSum-rightSum)
    for i in range(1, len(A)-1):
        leftSum+=A[i]
        rightSum-=A[i]
        min_gap=min(min_gap, abs(leftSum-rightSum))
    return min_gap


A = [3,1,2,4,3]
print(solution(A))