# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N):
    # Implement your solution here
    k=1
    l=[]
    while k*k<N:
        if N%k==0:
            l.append(k)
            l.append(N//k)
        k+=1
    if k*k==N:
        l.append(k)
    return len(l)


N=4
print(solution(N))