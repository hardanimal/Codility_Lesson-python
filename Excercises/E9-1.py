# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N):
    # Implement your solution here
    str_N=bin(N)
    max_gap=0
    start_count=False
    count=0
    for c in str_N[2:]:
        if c=='1':
            max_gap=max(max_gap, count)
            if start_count==False:
                start_count=True
            else:
                count=0
        else:
            count+=1
    return max_gap


N = 1041
print(solution(N))