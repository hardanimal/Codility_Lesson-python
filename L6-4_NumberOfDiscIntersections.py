# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # Implement your solution here
    n=len(A)
    lKth = [0]*n
    rJth = [0]*n

    for i in range(0, n):
        lKth[i] = i-A[i]
        rJth[i] = i+A[i]

    lKth=sorted(lKth)
    rJth=sorted(rJth)

    cnt=0
    j=0
    for i in range(0, n):
        while j<n and rJth[i] >= lKth[j]:
            cnt += j-i
            j+=1

            if cnt>10000000:
                return -1
    return cnt


A = [1,5,2,1,4,0]
print(solution(A))