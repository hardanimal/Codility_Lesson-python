# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(P, C):
    # Implement your solution here
    max_game_by_player = P//2
    max_game_by_court = C
    return min(max_game_by_court, max_game_by_player)


P = 5
C = 3
print(solution(P, C))