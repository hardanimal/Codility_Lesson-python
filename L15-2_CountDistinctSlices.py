# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(M, A):
    # Implement your solution here
    seen=[False]*(M+1)

    leftEnd=0
    rightEnd=0
    numSlice=0

    while leftEnd<len(A) and rightEnd<len(A):
        if seen[A[rightEnd]]==False:
            numSlice=numSlice+(rightEnd-leftEnd+1)
            if numSlice>=1000000000:
                return 1000000000
            seen[A[rightEnd]]=True
            rightEnd+=1
        else:
            seen[A[leftEnd]]=False
            leftEnd+=1
    return numSlice


M=6
A = 3,4,5,5,2
print(solution(M, A))