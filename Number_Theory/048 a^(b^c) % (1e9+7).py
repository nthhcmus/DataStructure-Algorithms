'''
    Ex48:   Find a^(b^c) % (1e9+7)
            1 <= n <= 10^5
            0 <= a,b,c <= 10^9
    Status: acp
    Note:   Use Fermat's little theorem:  
            a^(b^c) % MOD = a^((b^C) % (MOD-1)) % MOD
'''

def BiPowMod(x, n, MOD):
    res = 1
    if n < 1:
        return res
    res = BiPowMod(x, n//2, MOD)
    res *= res
    if n&1:
        res*=x
    return res % MOD

def solve(MOD):
    a, b, c = input().split(" ")
    a, b, c = int(a), int(b), int(c)
    e = BiPowMod(b, c, MOD-1)
    res = BiPowMod(a, e, MOD)
    print(res)

MOD = int(1e9+7)
t = int(input())
while t > 0:
    t-=1
    solve(MOD)
