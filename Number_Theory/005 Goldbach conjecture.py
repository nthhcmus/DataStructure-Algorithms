'''
    Ex5:    Goldbach conjecture
            Theo Goldbach conjecture 1 so nguyen duong chan >= 4 deu co the bieu dien duoc bang 2 so nguyen to
            Cho so nguyen duong chan n >= 4. Liet ke cac cap prime p,qq co tong bang n
            1 <= T <= 1000 (so test case)
            4 <= N <=1000000
    Status: acp
'''

from math import sqrt
def sieve_Of_Eratosthenes(n, prime):
    for i in range (2, int(sqrt(n)+1)):
        if(prime[i]):
            for j in range(i*i, n+1, i):
                prime[j] = False

def Try(prime):
    n = int(input())
    for i in range(3, int(n/2)+1):
        if prime[i] and prime[n-i]:
            print(i, end = ' ')
            print(n-i)
    
prime = [True for i in range (0, 1000002, 1)]
sieve_Of_Eratosthenes(1000001, prime)
t = int(input())
while(t > 0):
    Try(prime)
    t = t-1