# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, B):
    # Implement your solution here
    l=0
    s=[]
    for i in range(len(A)):
        if B[i]==0:
            while len(s)>0:
                if s[-1]<A[i]: s.pop()
                else: break
            else:
                l+=1
        else:
            s.append(A[i])
    return l+len(s)


A = [4,3,2,1,5]
B = [0,1,0,0,0]
print(solution(A,B))