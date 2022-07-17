''' 
    Ex47:   Find 2 elements have GCD is the largest in array
            2 <= n <= 1e6
            1 <= array[i] <= 1e6
    Status: acp
'''
import math
def find():
    n = int(input())
    cnt = [0 for i in range(0, int(1e6+5))]
    Max = 0
    save = input().split(" ", n-1)
    for i in range(0, n):
        x = int(save[i])
        cnt[x] += 1
        if x > Max:
            Max = x

    for divisor in range(Max, 0, -1):
        cnt_multiple = 0
        for ele in range(0, Max+1, divisor):
            cnt_multiple += cnt[ele]
            if cnt_multiple >= 2:
                return divisor
print(int(find()))