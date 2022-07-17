"""
    Ex16:   Smith number
            So Smith la so: Not prime, tong cac chu so cua n = tong chu so cua cac thua so nguyen to
            trong phan tich cua n
            1 <= n <= 1e18
    Status: acp
"""

import math
def sumOfDigits(n):
    sum = 0
    while n > 0:
        sum = sum + n%10
        n //= 10
    return sum

def is_Smith(n):
    sum_digits = 0
    sum = 0
    temp = n
    
    for i in range (2, int(math.sqrt(n)+1)):
        while n%i == 0:
            n //= i
            sum_digits = sumOfDigits(i)
            sum += sum_digits
    if n == temp:
        return False
    if n > 1: 
        sum += sumOfDigits(n)
    sum_digits = sumOfDigits(temp)
    return sum == sum_digits

n = int(input())
print("YES") if(is_Smith(n)) else print("NO")