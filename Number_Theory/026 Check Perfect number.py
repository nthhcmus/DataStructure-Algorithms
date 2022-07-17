'''
    Ex26:   Check Perfect number
            1 <= n <= 9*1e18
            Use Euclid: If p and 2^p - 1 are prime => 2^(p-1)*(2^p-1) is perfect number
    Status: acp
'''
import math

def isPrime(n):
    for i in range(2, int(math.sqrt(n)+1)):
        if n % i == 0:
            return False
    return n >= 2

def create_Perfect_List(n):
    save = []
    for p in range(2, n):
        if isPrime(p) and isPrime(2**p-1):
            save.append(int((2**(p-1))*(2**p-1)))
    return save

n = int(input())
save = create_Perfect_List(33)
flag = 0
for i in save:
    if i == n:
        print("YES")
        flag = 1
if flag == 0:
    print("NO")