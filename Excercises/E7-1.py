# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # Implement your solution here
    steps=1
    currPos=A[0]
    while currPos!=-1:
        steps+=1
        currPos=A[currPos]
    return steps


A=[1,4,-1,3,2]
print(solution(A))