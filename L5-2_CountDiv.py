# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, B, K):
    # Implement your solution here
    left = A//K if A%K!=0 else A//K-1
    right = B//K
    return right - left


A = 0
B = 2000000000
K = 1
print(solution(A, B, K))