''' 
    Ex45:   The number is created by: 11,111,1111,...
            1 <= n <= 1e9
    Status: acp
    Note:   Chi can xem so do co duoc bieu dien boi 2 so: 11 va 111 ko la dc
'''
def check(n):
    for i in range(0, int(n//111+1)):
        if (n - 111*i) % 11 == 0:
            return True
    return False
n = int(input())
if check(n):
    print("YES")
else:
    print("NO")