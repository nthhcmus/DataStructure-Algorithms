''' 
    Ex38:   Cal f(n) = -1 + 2 - 3 +...+ (-1)^n * n
            1 <= n <= 1e16
    Status: acp
'''
def cal(n):
    if n&1:
        return n//2 - n
    else:
        return n//2

n = int(input())
print(cal(n))