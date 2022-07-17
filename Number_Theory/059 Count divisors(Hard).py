'''
    Ex59:   Count divisors (Hard)
            Count divisors of product of all elements in positive array
            1<=n<= 10^6; 1<=a[i]<=10^6
    Status: acp
'''
import math
MAX = int(1e6+5)
MOD = int(1e9+7)

def find_Least_prime_factor(save):
    for i in range(2, int(math.sqrt(MAX+1))):
        if save[i] == i:
            for j in range(i*i, MAX, i):
                if i < save[j]:
                    save[j] = i
            
def factorize(n, least_prime, count):
    while n > 1:
        temp = least_prime[n]
        while n % temp == 0:
            count[temp] += 1
            n //= temp


n = int(input())
k = input().split()
max = 0
res = 1
least_prime = [i for i in range(0, MAX)]
count = [1 for i in range(0, MAX)]

find_Least_prime_factor(least_prime)
for i in k:
    factorize(int(i), least_prime, count)
    if max < int(i):
        max = int(i)
for i in range(2, max+1):
    if count[i] != 1:
        res *= count[i]
        res %= MOD
print(res)