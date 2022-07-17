'''
    Ex28:   Check so Loc Phat (the number just contains: 0,6,8)
            0 <= n <=1e18
    Status: acp
'''

def check_Loc_Phat(n):
    temp = n
    last_digit = 0
    while temp > 0:
        last_digit = temp % 10
        if last_digit != 0 and last_digit != 6 and last_digit != 8:
            return False
        temp //= 10
    return True

n = int(input())
print(1) if check_Loc_Phat(n) else print(0)