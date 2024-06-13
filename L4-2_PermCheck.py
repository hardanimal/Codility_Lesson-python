# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # Implement your solution here
    B=sorted(A)
    for i in range(1, len(B)+1):
        if i != B[i-1]: return 0
    return 1


A=[4,1,3]
print(solution(A))