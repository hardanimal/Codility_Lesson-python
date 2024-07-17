# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S):
    # Implement your solution here
    if len(S)==0: return -1
    if len(S)==1: return 0
    if len(S)%2==0: return -1
    left=0
    right=len(S)-1
    idx=-1
    while left<right:
        if S[left]==S[right]: idx=left+1; left+=1; right-=1
        else: break
    return idx if idx==left==right else -1


S="abbaabbaabbaabbaabbaabcabbaabbaabbaabbaabba" # should return -1
# S="barakarab"
print(solution(S))