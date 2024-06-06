# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # Implement your solution here
    map_A={}
    for elem in A:
        if not map_A.get(elem): map_A[elem]=1
        else: map_A[elem]+=1
    return(len(map_A.keys()))


A = [2,1,1,2,3,1]
print(solution(A))