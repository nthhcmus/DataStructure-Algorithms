'''
    Ex60:   Cal nCk
            0<=K<=N<=1000000
            MOD = 1e9 + 7
    Status: acp
'''
MAX = 1000000
MOD = int(1e9+7)
def fact(n):
    res = 1
    for i in range(2, n+1):
        res*=i
        res %= MOD
    return res % MOD

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

def nCk(n, k):
    res = fact(n)
    denom = fact(n-k)*fact(k) % MOD
    denom = BiPowMod(denom, MOD-2, MOD)
    return res*denom % MOD
    

n, k = input().split(" ")
n, k = int(n), int(k)
print(nCk(n, k))