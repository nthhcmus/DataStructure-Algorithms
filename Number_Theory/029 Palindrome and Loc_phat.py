'''
    Ex29:   Palindrome + Loc phat (palindrome, contains 6, last digit of sum of digits is 8)
            1 <= a, b <= 1e6
    Status: acp
'''
def check(n):
    temp = n
    rev = 0
    sum = 0
    flag_6 = False
    last_digit = 0
    while temp > 0:
        last_digit = temp % 10
        rev = rev*10 + last_digit
        sum += last_digit
        if last_digit == 6:
            flag_6 = True
        temp //= 10
    return flag_6 and sum % 10 == 8 and rev == n

a, b = input().split(" ")
a, b = int(a), int(b)

for i in range(a, b+1):
    if check(i):
        print(i, end = ' ')