''' 
    Ex62:   Fibonacci 2
            Check if the given number is in Fibonacci sequence
            0 <= n <= 9*10^18
    Status: acp
    
'''
MOD = 1000000007
def check_Fibonacci(k):
    #Cach giai khac la duyet tu dau den khoang ~so thu 92 trong day
    f0 = 1
    f1 = 0
    fi = 1
    i = 2
    while fi < k:
        fi = (f0 + f1)
        if fi == k:
            return True
        f0 = f1
        f1 = fi
    if(k == 1 or k == 0):
        return True
    return False

k = int(input())
if check_Fibonacci(k): print("YES")
else: print("NO")