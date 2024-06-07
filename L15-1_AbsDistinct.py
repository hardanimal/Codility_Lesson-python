# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # Implement your solution here
    list_A=[]
    for elem in A:
        list_A.append(abs(elem))
    return len(list(set(list_A)))
        


A = [-5,-3,-1,0,3,6]
print(solution(A))