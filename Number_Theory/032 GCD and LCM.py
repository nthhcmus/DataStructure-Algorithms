'''
    Ex32:   Find greatest common divisor(GCD) and least common multiple(LCM)
            1 <= a, b <= 1e12
    Status: acp
'''

def gcd(a, b):
    while a*b != 0:
        if a > b:
            a %= b
        else:
            b %= a
    return a+b

a, b = input().split(" ")
a, b = int(a), int(b)
gcd = gcd(a, b)
print(gcd, end=" ")
print(a*b // gcd)
