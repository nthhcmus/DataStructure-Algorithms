''' 
    Ex53:   Multinomial coefficient 2
            Xep hoa qua (Easy)
            n la so hoa qua, k1, k2, k3, k4 la so cam, quyt, tao, sau rieng
            Tinh so cach chon hoa qua
            1<=n<=20; 0<=k1,k2,k3,k4<=n và k1 + k2 + k3 + k4 = n
    Status: acp
'''
n = int(input())
k1, k2, k3, k4 = input().split(" ")
k1, k2, k3, k4 = int(k1), int(k2), int(k3), int(k4)
def fact(n, MOD = 1e30+7):
    res = 1
    for i in range (2, n+1):
        res = res * i % MOD
    return res

res = fact(n) / (fact(k1)*fact(k2)*fact(k3)*fact(k4))
print(int(res))