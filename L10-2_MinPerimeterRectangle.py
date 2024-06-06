# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N):
    # Implement your solution here
    step=0
    max_a=0
    max_b=0
    while step*step<N:
        step+=1
        if N%step==0:
            max_a=step
            max_b=N//step
    if step*step==N:
        max_a=max_b=step
    return 2*(max_a+max_b)


N=48
print(solution(N))