# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S, P, Q):
    # Implement your solution here
    l = len(S)    
    lastSeen = [[-1,-1,-1,-1] for x in range(l)]
    for x in range(len(S)):
        for i,j in enumerate(list("ACGT")):
            if S[x] == j:
                lastSeen[x][i] = x
            elif x>0: 
                lastSeen[x][i] = lastSeen[x-1][i]

    res = []
    for x in range(len(P)):
        startIdx = P[x]
        relevantLastSeen = lastSeen[Q[x]]
        res.append((min([i+1 for i,x in enumerate(relevantLastSeen) if x>=startIdx])))
    return res


S = "CAGCCTA"
P = [2,5,0]
Q = [4,5,6]
print(solution(S, P, Q))