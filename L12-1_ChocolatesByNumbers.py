# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N, M):
    # Implement your solution here
    def gcdByDivision(A,B):
        if A%B==0: return B
        else: return gcdByDivision(B, A%B)
    
    return N // gcdByDivision(N,M)


N = 10
M = 4
print(solution(N, M))