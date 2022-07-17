'''
    Ex 9:   T-prime 2, dem cac so <= n co 3 uoc so
            Ta chung minh duoc cac so nay la binh phuong cua so nguyen to
            1 <= n <= 1e12
    Status: acp
'''

import math

def sieve(n):
    m = int(math.sqrt(n))
    cnt = 0
    prime = [True for i in range(0, m+1)]
    for i in range(2, int(math.sqrt(m))+1):
        if(prime[i]):
            for j in range(i*i, m+1, i):
                prime[j] = False

    for i in range(2, m+1):
        if prime[i] == True:
            cnt = cnt+1
    print(cnt)

n = int(input())
sieve(n)
