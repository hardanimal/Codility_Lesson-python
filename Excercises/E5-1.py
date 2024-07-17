# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(E, L):
    # Implement your solution here
    enter_hour=int(E.split(":")[0])
    enter_minute=int(E.split(":")[1])
    leave_hour=int(L.split(":")[0])
    leave_minute=int(L.split(":")[1])
    total_time=leave_hour-enter_hour+(1 if (leave_minute-enter_minute)>0 else 0)
    if total_time>0:
        parking_fee=2+3+(total_time-1)*4
        return parking_fee
    else: return 0


E="21:53"
L="22:48"
print(solution(E, L))