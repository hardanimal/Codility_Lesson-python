# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # Implement your solution here
    map_A={}
    for elem in A:
        if not map_A.get(elem):
            map_A[elem]=1
        else:
            map_A.pop(elem)
    return list(map_A)[0]


A = [9,3,9,3,9,7,9]
print(solution(A))