''' 
    Ex58:   Count divisors (Easy)
            Count divisors of product of all elements in positive array
            1<=n<=1000; 1<=a[i]<=10^6
    Status: acp
'''
import math
MAX = int(1e6+5)
MOD = int(1e9+7)
count = [1 for i in range(0, MAX)]

def factorize(n):
    global count
    temp = n
    for i in range(2, int(math.sqrt(n)+1)):
        while n % i == 0:
            count[i]+=1
            n //= i
    if n > 1:
        count[n]+=1
    n = temp

n = int(input())
k = input().split()
max = 0
for i in k:
    factorize(int(i))
    if int(i) > max:
        max = int(i)

res = 1
for i in range(2, max+1):
    if count[i] != 1:
        res = res * count[i]
        res %= MOD
print(res%MOD)