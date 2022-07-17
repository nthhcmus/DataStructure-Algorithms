'''
    Ex57:   Bang nhan
            Hinh vuong n hang, n cot danh so 1->n^2
            O o vi tri (i, j) co gia tri i*j
            Cho x, xac dinh xem x xuat hien bao nhieu lan trong bang hinh vuong
            1<=n<=10^6; 1<=x<=10^9
    Status: acp
'''
import math

def count(n, x):
    cnt = 0
    for i in range(1, int(math.sqrt(x)+1)):
        j = x // i
        if x % i == 0 and i <= n and j <= n:
            cnt += 2
            if i == j: cnt-=1
    return cnt

n, x = input().split(" ")
n, x = int(n), int(x)
print(count(n, x))
