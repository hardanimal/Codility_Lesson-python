# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N, A):
    # Implement your solution here
    rtn=[0]*N
    max_value=0
    level=0
    for i in range(len(A)):
        if A[i]<=N:
            if rtn[A[i]-1]<level:
                rtn[A[i]-1]=level+1
            else:
                rtn[A[i]-1]+=1
            max_value=max(max_value, rtn[A[i]-1])
        else:
            level=max_value
    for i in range(N):
        if rtn[i]<level:
            rtn[i]=level
    return rtn


N = 5
A = [3,4,4,6,1,4,4]
print(solution(N,A))