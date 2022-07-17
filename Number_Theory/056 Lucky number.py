'''
    Ex56:   Lucky number
            Check if a number has at least 1 divisor with all digits 4 and 7
            1<=n<=10^12
    Status: acp
'''
import math
def check_Digits_4_7(n):
    m = n
    while m > 0:
        temp = m % 10
        m //= 10
        if temp != 4 and temp != 7:
            return False
    return True

def check_Luck(n):
    for i in range(1, int(math.sqrt(n)+1)):
        if n % i == 0:
            if check_Digits_4_7(i) or check_Digits_4_7(n//i):
                return True
    return False

n = int(input())
if(check_Luck(n)): print("YES")
else: print("NO")

