'''
    Ex10:   Dem uoc cua 1 so nguyen duong, (Cho phan tich thua so nguyen to)
            Count all divisors of a positive integer number
            1 <= T <=100 (So luong thua so nguyen to) 
            2 <= p <=100000 (Thua so nguyen to) 
            1 <= e <=100000 (So mu tuong ung)
    Status: acp
'''
import math

t = int(input())
cnt = 1
while(t > 0):
    t = t - 1
    a, b = input().split(' ')
    a, b = int(a), int(b)
    cnt = (cnt*(b+1))%1000000007
print(int(cnt))