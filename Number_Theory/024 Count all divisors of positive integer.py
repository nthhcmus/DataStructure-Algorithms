'''
    Ex24:   Count all divisors of positive integer
            1<=n<=1e14
    Status: acp
'''

import math
def countDivisors(n):
    cnt = 0
    for i in range (1, int(math.sqrt(n)+1)):
        if n % i == 0:
            cnt = cnt+ 1
            if n // i != i:
                cnt = cnt+1
    return cnt

n = int(input())
print(countDivisors(n))
