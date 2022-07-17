"""
    Ex27:   Check palindrome and >= factors
            1<=a,b<=1e7
    Status: tle, acp with C++
"""

import math

def checkPalindrome(n):
    temp = n
    rev = 0
    while temp > 0:
        rev = rev*10+temp%10
        temp //= 10
    return rev == n
    
def check(n):
    cnt = 0;
    for i in range(2, int(math.sqrt(n)+1)):
        if n % i == 0:
            cnt = cnt+1
            while n % i == 0:
                n//=i
        if cnt == 3:
            return True
    if n > 1:
        cnt = cnt+1
    return cnt >= 3

a, b = input().split(" ")
a, b = int(a), int(b)
flag = 0
for i in range(a, b+1):
    if checkPalindrome(i)and check(i):
            print (i, end = " ")
            flag = 1
if flag == 0:
    print(-1)