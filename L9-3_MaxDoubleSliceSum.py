# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # Implement your solution here
    slice1LocalMax = [0]*(len(A))
    slice2LocalMax = [0]*(len(A))

    # start from i=1 because slice can't start at index 0
    for i in range(1,len(A)):
            slice1LocalMax[i] = max(slice1LocalMax[i - 1] + A[i], 0)
    # start from i=A.length-2 because slice can't end at index A.length-1

    for i in range(len(A) - 2, 0, -1):
            slice2LocalMax[i] = max(slice2LocalMax[i + 1] + A[i], 0)

    maxDoubleSliceSum = 0
    # compute sums of all slices to find absolute max
    for i in range(1,len(A)-1):
            maxDoubleSliceSum = max(maxDoubleSliceSum, slice1LocalMax[i - 1] + slice2LocalMax[i + 1])

    return maxDoubleSliceSum


A = [3,2,6,-1,4,5,-1,2]
print(solution(A))