# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # Implement your solution here
    maxEndingPrevious=A[0]
    maxEndingHere=A[0]
    maxSoFar=A[0]

    for i in range(1,len(A)):
        maxEndingHere = max(A[i], maxEndingPrevious+A[i])
        maxEndingPrevious=maxEndingHere
        maxSoFar=max(maxSoFar, maxEndingHere)
    return maxSoFar


A = [3,2,-6,4,0]
print(solution(A))