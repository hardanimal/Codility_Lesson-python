# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(K, M, A):
    # Implement your solution here
    def divisionSolvable(mid, k, a):
        sum = 0
        for i in range(len(a)):
                sum += a[i]
                if (sum > mid):
                        sum = a[i]
                        k-=1
                if (k < 0):
                    return False
        return True
    
    min_v = 0
    max_v = 0
    for i in range(len(A)): # get the sum as max, and the largest number as min
            max_v += A[i]
            min_v = max(min_v, A[i])

    result = max_v
    while (min_v <= max_v):
            mid = (min_v + max_v) // 2
            if (divisionSolvable(mid, K - 1, A)):
                    max_v = mid - 1
                    result = mid
            else:
                    min_v = mid + 1
    return result


K = 3
M = 5
A = [2,1,5,1,2,2,2]
print(solution(K, M, A))