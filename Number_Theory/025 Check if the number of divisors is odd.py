'''
    Ex25:   Check if the number of divisors is odd
            1<=n<=1e18
    Status: acp
'''

import math
def checkSquare(n):
    Sqrt = int(math.sqrt(n))
    return float(Sqrt*Sqrt) == n

n = int(input())
print("YES") if checkSquare(n) else print("NO")