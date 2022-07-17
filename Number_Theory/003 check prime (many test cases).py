'''
    Ex3:    Check prime number with many test cases
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

def Try():
    n = int(input())

    if(isPrime(n)):
        print("YES")
    else:
        print("NO")

t = int(input())
while(t > 0):
    t = t -1
    Try()
