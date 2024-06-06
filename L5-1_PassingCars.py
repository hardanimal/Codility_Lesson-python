# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # Implement your solution here
    z_cnt=0
    o_cnt=0
    for i in range(len(A)):
        if A[i]==0: z_cnt+=1
        else: o_cnt+=z_cnt
        if o_cnt>1000000000: o_cnt=-1; break
    return o_cnt


A=[1,0,1,0,1,1,0,0]
print(solution(A))