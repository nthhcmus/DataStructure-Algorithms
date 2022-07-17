''' 
    Ex14:   Count trailing zeroes in factorial of a number
            1 <= n <= 1e18
    Status: acp
'''
def find_PowerOf_p_in_n_factorial(n, p):
    cnt = 0
    i = p
    while i <= n:
        cnt += n//i
        i *= p
    return cnt

n = int(input())
mod = 1000000007
print(min(find_PowerOf_p_in_n_factorial(n, 2), find_PowerOf_p_in_n_factorial(n, 5))%mod)