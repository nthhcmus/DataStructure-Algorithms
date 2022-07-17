'''
    Ex55:   Cal (A^B) / C % M with M is prime
            1<=A,B,C,M<=1000000022
    Status: acp
'''

def fact(n, MOD = int(1e9+7)):
    res = 1
    for i in range (2, n+1):
        res = res * i % MOD
    return res

def BiPowMod(x, n, MOD = int(1e9+7)):
    res = 1
    x %= MOD
    if n < 1:
        return res
    res = BiPowMod(x, n//2, MOD)
    res *= res
    if n&1:
        res*=x
    return res % MOD

k = input().split(" ")
a, b, c, m = int(k[0]), int(k[1]), int(k[2]), int(k[3])
res = BiPowMod(a, b, m)
denom = BiPowMod(c, m-2, m)
print(res*denom % m)