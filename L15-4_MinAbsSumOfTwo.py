# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # Implement your solution here
    N=len(A)
    B=sorted(A)
    tail=0
    head=N-1
    minAbsSum = abs(B[tail]+B[head])
    while tail<=head:
        currSum=B[tail]+B[head]
        minAbsSum=min(minAbsSum, abs(currSum))
        if currSum<=0:
            tail+=1
        else:
            head-=1
    return minAbsSum


A = [-8,4,5,-10,3]
# A=[1000000000]
print(solution(A))