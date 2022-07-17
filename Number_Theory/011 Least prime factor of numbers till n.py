''' 
    Ex11:   In ra uoc so nguyen to nho nhat cua cac so tu 1->n
            Least prime factor of numbers till n
            1 <= n <= 1e5
    Status: acp
'''
import math

def sieve(n):
    least_factor = [i for i in range(0, n+1)]
    for i in range (2, int(math.sqrt(n))+1):
        if least_factor[i] == i:
            for j in range(i*i, n+1, i):
                if least_factor[j] > i:
                    least_factor[j] = i
    least_factor[1] = 1
    for i in range(1, n+1):
        print(least_factor[i])

n = int(input())

sieve(n)