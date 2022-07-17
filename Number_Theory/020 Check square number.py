'''
    Ex20: Check Square number (1<= N <= 1e18)
    Status: TLE, accepted with C++
'''

import math

def check_Square(n):
    i = 0
    while i*i <= n:
        if i*i == n:
            return True
        i = i+1
    return False

n = int(input())

print("YES") if check_Square(n) else print("NO")