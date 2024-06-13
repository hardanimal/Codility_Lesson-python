# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # Implement your solution here
    if len(A)==0: return 1
    if len(A)==1:
        return 2 if A[0]==1 else 1
    B=sorted(A)
    start=B[0]
    if start!=1: return 1
    for x in B:
        if x!=start: return start
        start+=1
    return start


A=[2,3,1,5]
print(solution(A))