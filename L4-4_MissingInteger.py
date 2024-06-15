# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # Implement your solution here
    check=set(A)
    for i in range(1, len(A)+1):
        if i not in check: return i
    return i+1


A = [1, 3, 6, 4, 1, 2]
print(solution(A))