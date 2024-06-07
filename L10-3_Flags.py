# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # Implement your solution here
    import math
    peaks=[]
    for i in range(1,len(A)-1):
        if A[i-1]<A[i]>A[i+1]: peaks.append(i)
    
    if len(peaks)<=1: return len(peaks)

    maxFlags = math.ceil(math.sqrt(peaks[-1]-peaks[0]))
    for flags in range(maxFlags,1,-1):
        startFlagIndex=0
        endFlagIndex=len(peaks)-1

        startFlag=peaks[startFlagIndex]
        endFlag=peaks[endFlagIndex]

        flagsPlaced=2

        while (startFlagIndex<endFlagIndex):
            startFlagIndex+=1
            endFlagIndex-=1

            if peaks[startFlagIndex] >= startFlag+flags:
                if peaks[startFlagIndex] <= endFlag-flags:
                    flagsPlaced+=1
                    startFlag=peaks[startFlagIndex]

            if peaks[endFlagIndex] >= startFlag+flags:
                if peaks[endFlagIndex] <= endFlag-flags:
                    flagsPlaced+=1
                    endFlag=peaks[endFlagIndex]

            if flagsPlaced==flags:
                return flags
    
    return 0


A = [1,5,3,4,3,4,1,2,3,4,6,2]
print(solution(A))