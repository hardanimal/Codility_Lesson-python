# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, B, C):
    # Implement your solution here
    zero_30bits=[False]*30
    possible_conforms=[]
    # first to add A, B, C themself
    possible_conforms.append(A)
    possible_conforms.append(B)
    possible_conforms.append(C)
    print(possible_conforms)

    for idx in range(len(bin(A)[2:])):
        if bin(A)[idx+2]=='0':
            zero_30bits[idx]=True
            print(idx)
    # for idx in range(len(bin(B)[2:])):
    #     if bin(B)[idx+2]=='0':
    #         zero_30bits[idx]=True
    # for idx in range(len(bin(C)[2:])):
    #     if bin(C)[idx+2]=='0':
    #         zero_30bits[idx]=True
    # count_True=0
    # for elem in zero_30bits:
    #     if elem==True:
    #         count_True+=1
    # return 2**count_True


A = 0b111111111111111111111110011111
B = 0b111111111111111111111100111111
C = 0b111111111111111111111101101111
print(solution(A, B, C))