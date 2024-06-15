# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S):
    # Implement your solution here
    map_left = []
    map_right = []
    for c in S:
        if c=='(': map_left.append(c)
        else:
            map_right.append(c)
            if len(map_left)!=0: map_left.pop(); map_right.pop()
    return 1 if len(map_left)==0 and len(map_right)==0 else 0


S = "(()(())())"
print(solution(S))