'''
    Ex50:   Extended Euclidean algorithm
            mx + ny = p, p = GCD(m, n). Find & check if x + y is even
            1<=m,n,p<=10^18
    Status: acp
''' 
x, y, d = 1, 0, 1
def extended_Euclidean_Algo(m, n):
    global x, y, d
    if n == 0:
        x, y = 1, 0
        d = m
    else:
        extended_Euclidean_Algo(n, m % n)
        temp = x
        x = y
        y = int(temp - m//n *y)

m, n, p = input().split(" ")
m, n, p = int(m), int(n), int(p)
extended_Euclidean_Algo(m, n)
if (x+y) % 2 == 1 or d!=p:print("NO")
else: print("YES")
