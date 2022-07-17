''' 
    Ex37:   The number of divisors of n!
            1 <= n <= 1e5
    Status: acp
'''
mod = 1000000007
import math
def factorize_N_Factorial(n):
    cnt = 1
    save = [1 for i in range(0, 100005)]
    for i in range(2, n+1):
        temp = i
        for j in range(2, int(math.sqrt(i)+1)):
            while(temp % j == 0):
                save[j]+=1
                temp //= j
        if temp > 1:
            save[temp]+=1
    for i in range (0, 100005):
        if save[i]!=1:
            cnt*=(save[i])
    return cnt % mod

n = int(input())
print(factorize_N_Factorial(n))               
