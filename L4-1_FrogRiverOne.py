# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(X, A):
    # Implement your solution here
    arr=[False]*(len(A)+1)
    count=0
    for i in range(len(A)):
        if A[i]>X or A[i]>len(A): continue
        if arr[A[i]]==False:
            count+=1
            arr[A[i]]=True
        if count>=X: return i
    return -1


A=[1,3,1,4,2,3,5,4]
X=5
print(solution(X,A))