'''
    Ex13:   Power of prime number p in n!
            1<=n<=1e14; 2<=p<=5000  
    Status: acp
'''

def find_PowerOf_p_in_n_factorial(n, p):
    cnt = 0
    i = p
    while i <= n:
        cnt += n//i
        i *= p
    return cnt

n, p = input().split()
n, p = int(n), int(p)
print(find_PowerOf_p_in_n_factorial(n, p))