# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S):
    # Implement your solution here
    match_result=[]
    for c in S:
        if c in '([{': match_result.append(c)
        else:
            if not match_result or \
            (c==')' and match_result[-1]!='(') or \
            (c==']' and match_result[-1]!='[') or \
            (c=='}' and match_result[-1]!='{'):
                return 0
            match_result.pop()
    return 0 if match_result else 1


S="{[()()]}"
print(solution(S))