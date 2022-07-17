'''
    Ex1:    Check prime number
            0 <= n <= 1e9
    Status: acp
'''
from math import sqrt
def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(sqrt(n) + 1)):
        if(n%i==0):
            return False
    return True

n = int(input())
if(isPrime(n)):
    print("YES")
else:
    print("NO")