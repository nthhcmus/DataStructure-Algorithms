'''
    Ex22:   Count square number in [a, b]
            1<=a,b<=1e18
    Status: acp
'''

import math
def countSquare(a, b):
    begin = int(math.ceil(math.sqrt(a)))
    end = int(math.sqrt(b))+1
    return end - begin

a, b = input().split(" ")
a, b = int(a), int(b)
print(countSquare(a, b))