''' 
    Ex35:   Pascal's triangle
            1 <= n <= 100
    Status: acp
'''

mod = int(1e9+7)
def print_row(row):
    for i in row:
        if i == 0:
            break
        print(i, end = " ")
    print()

def print_Pascal_Tri(h):
    row = [0 for i in range(0, h+5)]
    temp = [0 for i in range(0, h+5)]
    row[0] = 1
    row[1] = 1
    temp[0] = 1
    temp[1] = 1
    print(1)
    if h == 1:
        return
    print_row(row)
    loop = h - 2
    while loop > 0:
        loop-=1
        for i in range(1, h):
            if row[i] == 0:
                temp[i] = 1
                break
            temp[i] = (row[i-1]+row[i])%mod
        
        print_row(temp)

        for i in range(0, h):
            if temp[i] == 0:
                break
            row[i] = temp[i]

n = int(input())
print_Pascal_Tri(n)    