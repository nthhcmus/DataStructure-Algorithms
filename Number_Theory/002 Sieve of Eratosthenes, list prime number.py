'''
    Ex2:    Cho n ko am, liet ke tat ca so nguyen to nho hon n
            Sieve of Eratosthenes
            0 <= n <= 1e7
    Status: acp
'''

from math import sqrt
def sieve_Of_Eratosthenes(n):
    prime = [True for i in range (0, n+1, 1)]
    for i in range (2, int(sqrt(n)+1)):
        if(prime[i]):
            for j in range(i*i, n+1, i):
                prime[j] = False

    # Print
    for i in range(2, n+1):
        if prime[i]:
            print(i, end = ' ')

n = int(input())
sieve_Of_Eratosthenes(n)