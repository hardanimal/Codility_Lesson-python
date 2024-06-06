# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # Implement your solution here
    if len(A)==0: return 0
    min_price=A[0]
    max_profit=0
    for i in A[1:]:
        max_profit=max(max_profit, i-min_price)
        min_price=min(min_price, i)
    return max_profit


A = [23171,21011,21123,21366,21013,21367]
print(solution(A))