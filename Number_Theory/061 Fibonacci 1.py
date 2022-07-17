'''
    Ex61:   Fibonacci 1
            Print kth of Fibonacci
            1 <= n <= 10^6
    Status: acp
'''
MOD = 1000000007
MAX = 1000005
def create_Fibonacci():
    Fibonacci = [0 for i in range(0, MAX)]
    Fibonacci[2] = 1
    for i in range(3, MAX):
        Fibonacci[i] = Fibonacci[i-1] + Fibonacci[i-2]
        Fibonacci[i] %= MOD
    return Fibonacci

k = int(input())
Fibonacci = create_Fibonacci()
print(Fibonacci[k])