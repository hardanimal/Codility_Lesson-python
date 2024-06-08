# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, B, C):
    # Implement your solution here
    # for each plank , we can use binary search to get the minimal index of the
    # sorted array of nails, and we should check the candidate nails to get the
    # minimal index of the original array of nails.
    def getMinIndex(startPlank, endPlank, nail, preIndex):
        min_v = 0
        max_v = len(nail) - 1
        minIndex = -1
        while (min_v <= max_v):
            mid = (min_v + max_v) // 2
            if (nail[mid][0] < startPlank):
                    min_v = mid + 1
            elif (nail[mid][0] > endPlank):
                    max_v = mid - 1
            else:
                    max_v = mid - 1
                    minIndex = mid
        if (minIndex == -1): return -1
        minIndexOrigin = nail[minIndex][1]
        # find the smallest original position of nail that can nail the plank
        for i in range(minIndex, len(nail)):
            if (nail[i][0] > endPlank):
                break
            minIndexOrigin = min(minIndexOrigin, nail[i][1])
            # we need the maximal index of nails to nail every plank, so the
            # smaller index can be omitted
            if (minIndexOrigin <= preIndex):
                return preIndex
        return minIndexOrigin


    # the main algorithm is that getting the minimal index of nails which
    # is needed to nail every plank by using the binary search
    N = len(A)
    M = len(C)
    # two dimension array to save the original index of array C
    sortedNail = [[0 for col in range(2)] for row in range(M)]
    for i in range(M):
        sortedNail[i][0] = C[i]
        sortedNail[i][1] = i

    # use the lambda expression to sort two dimension array
    # Arrays.sort(sortedNail, (int x[], int y[]) -> x[0] - y[0]);
    sortedNail = sorted(sortedNail)
    result = 0
    for i in range(N): # find the earlist position that can nail each plank, and the max value for all
                                                                # planks is the result
        result = getMinIndex(A[i], B[i], sortedNail, result)
        if (result == -1):
            return -1
    return result + 1


A = [1,4,5,8]
B = [4,5,9,10]
C = [4,6,7,10,2]
print(solution(A, B, C))