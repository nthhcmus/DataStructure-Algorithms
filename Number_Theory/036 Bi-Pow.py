''' 
    Ex36:   Pow. Cal a^b%1000000007
            1 <= a, b <= 1e12
    Status: acp
'''
mod = int(1000000007)
def bi_pow(x, n):
    if n == 1 or n == 0:
        return x
    res = bi_pow(x, n//2) % mod
    if n&1:
        return (res*res*x) % mod
    else:
        return (res*res) % mod

a, b = input().split(" ")
a, b = int(a), int(b)
print(bi_pow(a, b))