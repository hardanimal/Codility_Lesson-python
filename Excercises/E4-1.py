# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # Implement your solution here
    map_A={}
    for elem in A:
        if not map_A.get(elem):
            map_A[elem]=1
        else:
            map_A[elem]+=1
    
    for key,value in map_A.items():
        if value==1: return key
    return -1


A=[4,10,5,4,2,10]
print(solution(A))