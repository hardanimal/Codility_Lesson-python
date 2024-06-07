# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # Implement your solution here
    if len(A)<3: return 0
    B=sorted(A)
    rtn=0
    for i in range(len(B)):
        k=i+1
        for j in range(k, len(B)):
            while (k<len(B) and B[i]+B[j]>B[k]):
                k+=1
            rtn += k-j-1
    return rtn


A = [10, 2, 5, 1, 8, 12]
print(solution(A))