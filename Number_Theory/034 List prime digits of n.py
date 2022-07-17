''' 
    Ex34:   list prime digits in n
            1 <= n <= 1e18
    Status: acp
'''

def solve(n):
    cnt = [0 for i in range(0, 10)]
    save = [0 for i in range(0, 20)]
    count = 0
    while n > 0:
        last = n%10
        n //= 10
        if not(last == 2 or last == 3 or last == 5 or last == 7):
            continue
        count += 1;
        save[count] = last
        cnt[last] += 1
    if cnt[2] != 0:
        print(2, end = " ")
        print(cnt[2])
    if cnt[3] != 0:
        print(3, end = " ")
        print(cnt[3])
    if cnt[5] != 0:
        print(5, end = " ")
        print(cnt[5])
    if cnt[7] != 0:
        print(7, end = " ")
        print(cnt[7])
    print()
    for i in range(19, 0, -1):
        if save[i] != 0 and cnt[save[i]] != 0:
            print(save[i], end = " ")
            print(cnt[save[i]])
            cnt[save[i]] = 0
n = int(input())
solve(n)