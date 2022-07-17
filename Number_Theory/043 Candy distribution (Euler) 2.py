''' 
    Ex43:   Candy distribution (Euler) 2
            Chia n qua tao vao m hop sao cho moi hop >= 1 qua
            1 <= m, n <= 1000
    Status: acp
    Note:   Dung factorial or recursion thi bi time error
'''
mod = 1000000007
MAX = 1005

def nCr(n, r):
    Comb = [[1 for i in range(0, MAX+1)] for j in range (0, MAX+1)]
    for i in range(0, MAX+1):
        for j in range(0, MAX+1):
            if j == 0 or j == i:
                Comb[i][j] = 1
            else:
                Comb[i][j] = Comb[i-1][j] + Comb[i-1][j-1]
                Comb[i][j] %= mod
    return Comb[n][r] % mod

n, m = input().split(' ')
n, m = int(n), int(m)

print(int(nCr(n-1, m-1)))
