'''
    Ex31:   Count Co-prime numbers with n
            Euler's Totient function
            1 <= n <= 1e12
    Status: acp
'''
import math

def phi(n):
    cnt = n
    for i in range(2, int(math.sqrt(n)+1)):
        if n % i == 0:
            while n % i == 0:
                n //=i
            cnt = cnt - cnt//i
    if n > 1:
        cnt = cnt - cnt//n
    return cnt

n = int(input())
print(phi(n))
