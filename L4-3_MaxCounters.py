# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N, A):
    # Implement your solution here
    if N==1: return [1]
    max_counter=max(A)
    print(max_counter)
    rtn=[0]*N
    print(rtn)
    max_value=0
    for idx in range(len(A)):
        print(elem, rtn)
        if elem==max_counter:
            rtn=[max_value]*N
        else:
            rtn[elem-1]+=1
            max_value=max(rtn)
    return rtn

def solution2(N, A):
    rtn=[0]*N
    max_value=0
    level=0
    for i in range(len(A)):
        print(i, max_value, level, rtn)
        if A[i]<=N:
            if rtn[A[i]-1]<level:
                rtn[A[i]-1]=level+1
            else:
                rtn[A[i]-1]+=1
            max_value=max(max_value, rtn[A[i]-1])
        else:
            level=max_value
    for i in range(N):
        print(max_value, level, rtn)
        if rtn[i]<level:
            rtn[i]=level
    return rtn

N=5
A=[3,4,4,6,1,4,4]
print(solution2(N,A))