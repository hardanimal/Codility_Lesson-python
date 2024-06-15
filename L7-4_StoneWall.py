# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(H):
    # Implement your solution here
    stone_count=0
    stone_list=[]
    for i in H:
        while len(stone_list) !=0 and stone_list[-1]>i:
            stone_list.pop(-1)
            stone_count+=1
        if len(stone_list)==0 or i>stone_list[-1]:
            stone_list.append(i)
    stone_count+=len(stone_list)
    return stone_count


H = [8,8,5,7,9,8,7,4,8]
print(solution(H))