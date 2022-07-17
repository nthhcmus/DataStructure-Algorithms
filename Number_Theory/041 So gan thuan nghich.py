'''
    Ex41:   So gan thuan nghich
            (2th digit -> chu so gan cuoi la palindrome and first digit = 2 last digit (or 1/2))
            99 <= n <= 1e18
    Status: acp
'''

def check(n):
    last = n % 10
    n //= 10
    temp = n
    digit = 0
    rev = 0
    cnt = 0

    while temp > 0:
        digit = temp % 10
        temp //= 10
        rev = rev*10 + digit
        cnt += 1
    cnt-= 1
    rev //= 10
    return n - rev == digit*10**cnt and (last == digit*2 or digit == last*2)

n = int(input())
if check(n):
    print("YES")
else:
    print("NO")
    
