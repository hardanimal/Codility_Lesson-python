# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, B):
    # Implement your solution here
    def gcd(a,b):
        if a%b==0: return b
        else: return gcd(b, a%b)

    def hasSamePrimeDivisors(a,b):
        gcdValue=gcd(a,b)
        gcdA=0
        gcdB=0
        while a!=1:
            gcdA=gcd(a, gcdValue)
            if gcdA==1:
                break
            a=a/gcdA
        if a!=1: return False
        while b!=1:
            gcdB=gcd(b,gcdValue)
            if gcdB==1:
                break
            b=b/gcdB
        return b==1
    
    count=0
    for i in range(len(A)):
        if hasSamePrimeDivisors(A[i],B[i]):
            count+=1
    return count


A = [15,10,3]
B = [75,30,5]
print(solution(A,B))