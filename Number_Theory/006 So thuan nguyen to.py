'''
    Ex6:    So thuan nguyen to: so nguyen to, cac chu so va tong cac chu so deu nguyen to
            in cac so thuan nguyen to trong khoang [a, b]
            1 <= a,b < 1e9
    Status: acp with C++
'''
from math import sqrt
def isPrime(n):
    for i in range(2, int(sqrt(n) + 1)):
        if(n%i==0):
            return False
    return n >= 2

def isPrimeDigit_and_PrimeSumDigit(n):
    sum = 0
    while(n > 0):
        temp = n%10
        if temp != 3 and temp != 5 and temp != 7 and temp != 2:
            return False
        n = n//10
        sum = sum + temp
    return isPrime(sum)

a, b = input().split(' ')
a = int(a)
b = int(b)
cnt = 0
for i in range(a, b+1):
    if isPrimeDigit_and_PrimeSumDigit(i):
        if isPrime(i):
            cnt = cnt + 1
print(cnt)