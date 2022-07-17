''' 
    Ex33:   Kth factor of n
            1 <= n,k <= 1e9
    Status: acp
'''
import math
def find_Kth_factor(n, k):
    for i in range (2, int(math.sqrt(n)+1)):
        while n%i == 0:
            n//=i
            k = k - 1
            if k == 0:
                return i
    if n > 1 and k == 1:
        return n
    return -1

a, b = input().split(" ")
a, b = int(a), int(b)
print(find_Kth_factor(a, b))