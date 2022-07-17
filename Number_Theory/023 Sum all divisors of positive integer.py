'''
    Ex23:   Sum all divisors of positive integer
            1<=n<=1e12
    Status: acp
'''

import math
def sumOfDivisors(n):
    sum = 0
    for i in range (1, int(math.sqrt(n)+1)):
        if n % i == 0:
            sum += i
            if n // i != i:
                sum += n // i
    return sum

n = int(input())
print(sumOfDivisors(n))
