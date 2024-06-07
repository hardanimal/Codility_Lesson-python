# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N, P, Q):
    # Implement your solution here
    import math
    primeArray = [True]*(N+1)

    primeArray[0]=False
    primeArray[1]=False
    sqrtN=int(math.sqrt(N))
    for i in range(2,sqrtN):
        j=i+i
        for j in range(j, N+1, i):
            primeArray[j]=False

    primeList=[]
    for i in range(2, N+1):
        if primeArray[i]:
            primeList.append(i)

    semiprimeArray = [False]*(N+1)
    semiprimeTemp=0
    for i in range(0, len(primeList)):
        for j in range(i, len(primeList)):
            semiprimeTemp=primeList[i]*primeList[j]
            if semiprimeTemp>N:
                break
            else:
                semiprimeArray[int(semiprimeTemp)]=True

    semiprimeCumulateCount=[0]*(N+1)
    for i in range(1, N+1):
        semiprimeCumulateCount[i]=semiprimeCumulateCount[i-1]
        if semiprimeArray[i]==True:
            semiprimeCumulateCount[i]+=1

    numQuery=len(Q)
    result=[0]*numQuery
    for i in range(0, numQuery):
        result[i]=semiprimeCumulateCount[Q[i]]-semiprimeCumulateCount[P[i]-1]

    return result


N=26
P = [1,4,16]
Q = [26,10,20]
print(solution(N,P,Q))