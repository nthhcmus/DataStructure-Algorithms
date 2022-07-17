'''
    Ex40:   LCM of x,y,z
            Tim so nguyen duong nho nhat co n chu so chia het cho x,y,z
            1 <= x,y,z <= 1e4
            n <= 16
    Status: acp
'''
import math

x, y, z, n = input().split()
x = int(x)
y = int(y)
z = int(z)
n = int(n)

gcd = math.gcd(x, y)
lcm = int((x*y)/gcd)
gcd = math.gcd(z, lcm)
lcm = int((lcm*z) / gcd)

min = 1
max = 9
for i in range(1, n):
    min = min*10
    max = max*10+9

begin = int(min // lcm)
if min % lcm == 0:
    print(min)
elif lcm*(begin+1) <= max:
    print(lcm*(begin+1))
else:
    print(-1)