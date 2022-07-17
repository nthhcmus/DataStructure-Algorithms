''' 
    Ex51:   Modulo 1
            Give a, b and (a * m) % b = 1. Find m (>=0)
            1<=a,b<=10^18
    Status: acp
'''

x,y,d = 1, 0, 1
def extended_Euclidean_Algo(a, b):
    global x, y, d
    if b == 0:
        x,y = 1,0
        d = a
    else:
        extended_Euclidean_Algo(b, a%b)
        temp = x
        x = y
        y = temp - a//b * y

a, b = input().split(" ")
a, b = int(a), int(b)
extended_Euclidean_Algo(a, b)
if d != 1:
    print(-1)
else:
    print((x % b + b)%b) #de tranh TH am