''' 
    Ex52:   Modulo 2
            Give a, m = 1000000007 and a*b % m = 1. Find min b (b>0)
            1<=a<=10^9
    Status: acp
'''
def BiPowMod(x, n, MOD = 1e15+7):
    res = 1
    x %= MOD
    if n < 1:
        return res
    res = BiPowMod(x, n//2, MOD)
    res *= res
    if n&1:
        res*=x
    return res % MOD
def find_Modular_multiplicative_inverse(a, MOD):
    return BiPowMod(a, MOD-2, MOD)
m = 1000000007
a = int(input())
print(find_Modular_multiplicative_inverse(a, m))