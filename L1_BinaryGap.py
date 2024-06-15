# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N):
    # Implement your solution here
    str_n=bin(N)[2:]
    f_count=False
    gap_max=0
    gap_count=0
    for c in str_n:
        if c=='1':
            if not f_count:
                f_count=True
            else:
                gap_max=max(gap_max,gap_count)
                gap_count=0
        else:
            gap_count+=1
    return gap_max


A = 1041
print(solution(A))