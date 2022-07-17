''' 
    Ex19:   Square of a prime number 2 
            1 <= a,b <= 1e6
    Status: TLE, acp with C++
'''

import math

def check_SoDep(n):
    for i in range(2, int(math.sqrt(n)+1)):
        e = 0
        while n % i == 0:
            e= e+1
            n //= i
        if e != 0 and e < 2:
            return False
    return n <= 1

a, b = input().split(" ")
a, b = int(a), int(b)
for i in range(a, b+1):
    if check_SoDep(i):
        print(i, end = " ")