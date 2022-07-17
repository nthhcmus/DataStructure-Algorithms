'''
    Ex7:    2 so nguyen to cung nhau trong [a, b]
    2<=a<=b<=1000
    Status: acp
'''
import math
def is_CoPrime(a, b):
    return math.gcd(a, b) == 1
a, b = input().split(' ')
a = int(a)
b = int(b)
for i in range (a, b+1):
    for j in range(i+1, b+1):
        if is_CoPrime(i, j):
            res = "(" + str(i) +","+str(j)+")"
            print(res)
