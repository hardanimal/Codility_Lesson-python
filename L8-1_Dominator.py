# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # Implement your solution here
    candidate=0
    counter=0
    for i in range(len(A)):
        if counter==0: candidate=i
        if A[i]==A[candidate]:
            counter+=1
        else:
            counter-=1

    counter=0
    for i in range(len(A)):
        if A[i]==A[candidate]: counter+=1

    return candidate if counter>len(A)/2 else -1


A = [3,4,3,2,3,-1,3,3]
A=[]
print(solution(A))