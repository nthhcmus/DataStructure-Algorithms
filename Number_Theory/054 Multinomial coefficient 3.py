''' 
    Ex54:   Multinomial coefficient 3
            Xep hoa qua (Hard)
            n la so hoa qua, k1, k2, k3, k4 la so cam, quyt, tao, sau rieng
            1<=n<=10^6; 0<=k1,k2,k3,k4<=n and k1 + k2 + k3 + k4 = n
            Tinh so cach chon hoa qua
    Status: acp
'''
MOD = int(1e9+7)
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

n = int(input())
k = input().split(" ")
res = fact(n, MOD)
denom = 1
for i in k:
    denom = denom * fact(int(i),MOD) % MOD
denom = BiPowMod(denom, MOD-2, MOD)
print((res%MOD)*(denom%MOD) % MOD)