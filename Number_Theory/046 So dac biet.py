''' 
    Ex46:   So dac biet
            (M duoc goi la so dac biet cua N neu M duoc tao boi cac luy thua ko am khac nhau cua N)
            Prob: In ra so dac biet thu K cua N (cac so dac biet cua N xep tang dan)
            2<=N<=1e9; 1<=K<=1e9
    Status: acp
    Note: Ban chat gan giong viec chuyen doi co so
    
'''
MOD = int(1e9+7)

def convert_dec_to_bin(k):
    res = ""
    while k > 0:
        res = res + str(k%2)
        k //= 2
    return res

n, k = input().split(' ')
n, k = int(n), int(k)
bin = convert_dec_to_bin(k)
res = 0
leng = len(bin)
for i in range(0, leng):
    if bin[i] == '1':
        res = (res + n**i) % MOD
print(res)
