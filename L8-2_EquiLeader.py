# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # Implement your solution here
    if len(A)==1: return 0

    value = A[0]
    size=0
    for i in range(len(A)):
        if size==0:
            size+=1
            value = A[i]
        else:
            if A[i]==value:
                size+=1
            else:
                size-=1

    candidate = -1
    count = 0
    if size>0:
        candidate = value

    for i in range(len(A)):
        if A[i]==candidate:
            count+=1

    if count<=len(A)/2:
        return 0

    leader = candidate
    equiCount = 0
    leaderCount = 0
    for i in range(len(A)):
        if A[i] == leader:
            leaderCount+=1

        if leaderCount>(i+1)/2  and (count-leaderCount)>(len(A)-i-1)/2:
            equiCount+=1

    return equiCount


A = 4,3,4,4,4,2
print(solution(A))