# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # Implement your solution here
    B=sorted(A)
    if B[1]<0 and B[-2]>0: return max(B[0]*B[1]*B[-1], B[-1]*B[-2]*B[-3])
    return (B[-1]*B[-2]*B[-3])


A= [-3,1,2,-2,5,6]
print(solution(A))