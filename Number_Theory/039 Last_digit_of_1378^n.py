''' 
    Ex39:   Last digit of 1378^n
            0 <= n <= 1e18
    Status: acp
'''

def find_Last_digit(n):
    if n == 0:
        return 1
    if n % 4 == 1:
        return 8
    if n % 4 == 2:
        return 4
    if n % 4 == 3:
        return 2
    if n % 4 == 0:
        return 6

n = int(input())
print(find_Last_digit(n))