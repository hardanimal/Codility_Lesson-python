# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, K):
    # Implement your solution here
    if len(A)==0: return []
    K=K%len(A)
    return A[-K:]+A[:-K]


A = [3, 8, 9, 7, 6]
K = 3
print(solution(A,K))