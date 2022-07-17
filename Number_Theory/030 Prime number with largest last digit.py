'''
    Ex30:   Prime number with largest last digit
            1 <= n <= 1e7
    Status: acp
'''

import math
def check_lastDigit(n):
    temp = n
    last_digit = n % 10
    while temp > 0:
        if last_digit < temp % 10:
            return False
        temp = temp // 10
    return True

def sieve_Prime(n):
    prime = [True for i in range(0, n+1)]
    for i in range(2, int(math.sqrt(n)+1)):
        if prime[i]:
            for j in range(i*i, n+1, i):
                prime[j] = False
    return prime

prime = sieve_Prime(10000007)
n = int(input())
cnt = 0
for i in range(2, n+1):
    if prime[i] and check_lastDigit(i):
        print(i, end = ' ')
        cnt = cnt+1
print()
print(cnt)