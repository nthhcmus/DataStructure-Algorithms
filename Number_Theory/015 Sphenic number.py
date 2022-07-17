"""
    Ex15:   Sphenic number
            So n la Sphenic neu n duoc phan tich duy nhat dang tich 3 thua so ngto khac nhau
            Vd: 30 = 2*3*5 -> Sphenic, 60 = 2*2*3*5 -> NOT Sphenic
            1 <= n <= 1e18
    Status: tle, (acp with C++)
"""

import math
def check_Sphenic(n):   
    cnt = 0
    for i in range(2, int(math.sqrt(n)+1)):
        e = 0
        while n%i == 0:
            cnt = cnt+1
            e = e + 1
            n //=i
        if e > 1:
            return False
    if n > 1:
        cnt = cnt+1
    return cnt == 3

n = int(input())
print(int(check_Sphenic(n)))
