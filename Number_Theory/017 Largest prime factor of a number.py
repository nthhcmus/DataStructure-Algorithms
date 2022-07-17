'''
    Ex17:   Find largest prime factor of a positive integer
            1 <= t <= 500 (number of test cases)
            2 <= n <= 1e7
    Status: acp
'''

import math
def find_largest_prime_factor(n):
    #sieve
    ans = 0
    for i in range(2, int(math.sqrt(n)+1)):
        while n%i == 0:
            ans = i
            n//=i
    if n > 1 and n > ans:
        ans = n
    return ans

t = int(input())
while t > 0:
    t = t-1
    n = int(input())
    print(find_largest_prime_factor(n))

