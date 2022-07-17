'''
    Ex12:   Print Prime Factorization of n
            1 <= N <= 1e16
    Status: acp with C++
'''
import math

def factorize(n):
    for i in range (2, int(math.sqrt(n)+1)):
        if n % i == 0:
            e = 0
            prime_flag = False
            while n % i == 0:
                n = int(n/i)
                e = e+1
            res = str(i)+"^"+str(e)
            print(res, end = "")
            if n != 1:
                print(" * ", end = "")
    if n > 1:
        res = str(n)+"^1"
        print(res)

n = int(input())
#n = 1, not print
factorize(n)