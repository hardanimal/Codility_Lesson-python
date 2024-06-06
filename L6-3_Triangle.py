# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # Implement your solution here
    B=sorted(A)
    rtn=0
    for idx in range(len(B)-2):
        if B[idx]+B[idx+1]>B[idx+2]: rtn=1;break
    return rtn


A=[10, 50, 5, 1]
print(solution(A))