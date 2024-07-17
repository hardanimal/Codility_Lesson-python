# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S):
    # Implement your solution here
    uppercharactor_range=range(65,91)
    lowercharactor_range=range(97,123)
    number_range=range(48,58)

    wordArray = S.split(' ')
    charactor_count=-1
    for word in wordArray:
        letterCount=0
        numberCount=0
        f_word_validate = True
        for c in word:
            ascii_value = ord(c)
            if ascii_value in uppercharactor_range:
                letterCount+=1
            elif ascii_value in lowercharactor_range:
                letterCount+=1
            elif ascii_value in number_range:
                numberCount+=1
            else:
                f_word_validate = False
                break
        if f_word_validate and letterCount%2==0 and numberCount%2==1:
            charactor_count=max(charactor_count, len(word))

    return charactor_count


# S="test 5 a0A pass007 ?xy1"
S="ab0_00 abc_00 ab+000 ab+c00 0a00b 0ad0b 0ab? 04d?"
print(solution(S))