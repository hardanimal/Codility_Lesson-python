# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(X, Y, D):
    # Implement your solution here
    if (Y-X)%D==0:
        return int((Y-X)/D)
    else:
        return (Y-X)//D+1


X = 10
Y = 85
D = 30
print(solution(X, Y, D))