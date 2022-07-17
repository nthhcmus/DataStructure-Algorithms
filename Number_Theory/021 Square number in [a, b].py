''' 
    Ex21:   Print square number in [a,b]
            1<=a,b<=1e12
    Status: acp
'''

import math
def printSquare(a, b):
    for i in range(int(math.ceil(math.sqrt(a))), int(math.sqrt(b))+1):
        print(i*i, end = " ")

a, b = input().split(" ")
a, b = int(a), int(b)
printSquare(a, b)