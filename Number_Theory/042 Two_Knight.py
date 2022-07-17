'''
    Ex42:   2 Knights
        (Count the number of ways to place 2 Knights on the chessboard 
        so that they don't take each other)
            1 <= n <= 1e4
    Status: acp
'''

def count_ways(k):
    res = (k*k*k*k - k*k) / 2
    return int(res - (k-1)*(k-2)*4)

k = int(input())
for i in range(1, k+1):
    print(count_ways(i))