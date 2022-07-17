''' 
    Ex44:   Candy distribution (Euler) 1
            Distribute m apples to n children
            1 <= m,n <= 25
    Status: acp
    Note:   Dung factorial or recursion thi bi time error
'''
mod = 100000000000000000007
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

print(int(nCr(m+n-1, n-1)))
