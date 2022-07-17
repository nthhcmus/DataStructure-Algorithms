''' 
    Ex49:   Multinomial coefficient
            Count number of new strings can create by characters of given string
            1 <= n <= 1e6
    Status: acp
'''
MOD = int(1e9+7)
def fact(n, MOD):
    res = 1
    for i in range (2, n+1):
        res = res * i % MOD
    return res

def BiPowMod(x, n, MOD):
    res = 1
    x %= MOD
    if n < 1:
        return res
    res = BiPowMod(x, n//2, MOD)
    res *= res
    if n&1:
        res*=x
    return res % MOD    

string = input()
res = fact(len(string), MOD)

char_num = [0 for i in range(0, 26)]
for char in string:
    char_num[ord(char)-ord('a')] += 1
denom = 1
for cnt in char_num:
    denom = denom * fact(cnt, MOD)
denom = BiPowMod(denom, MOD-2, MOD)
print((res%MOD)*(denom%MOD) % MOD)