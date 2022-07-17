'''
    Ex4:    Dem so nguyen to co cac chu so nguyen to trong [a, b]
    1<= a, b <= 1e7
    Status: acp
'''
from math import sqrt
    
def sieve_Of_Eratosthenes(a, n):
    prime = [True for i in range (0, n+1, 1)]
    for i in range (2, int(sqrt(n)+1)):
        if(prime[i]):
            for j in range(i*i, n+1, i):
                prime[j] = False
    cnt = 0
    for i in range(a, n+1, 1):
        if prime[i] == True:
            flag = True
            while(i > 0):
                temp = i%10
                i = i//10
                if(temp == 2 or temp == 3 or temp == 5 or temp == 7):
                    continue
                flag = False
            if flag == True:
                cnt = cnt+1
    print(cnt)

a, b = input().split()
a = int(a)
b = int(b)
sieve_Of_Eratosthenes(a, b)