/*
    Ex15:   Sphenic number
            So n la Sphenic neu n duoc phan tich duy nhat dang tich 3 thua so ngto khac nhau
            Vd: 30 = 2*3*5 -> Sphenic, 60 = 2*2*3*5 -> NOT Sphenic
            1 <= n <= 1e18
    Status: acp
*/
#include <iostream>
#include <math.h>
#include <algorithm>

#define ll long long 
using namespace std ;

bool check(ll n)
{
    long long cnt = 0;
    for(long long i = 2; i*i <= n; i++)
    {
        long long e = 0;
        while(n%i==0)
        {
            e++;
            cnt++;
            if(e > 1) return false;
            n /= i;
        }
    }
    if (n > 1) cnt++;
    return cnt == 3;
}

int main()
{
    ll n = 0;
    cin >> n;
    if(check(n)) cout << 1;
    else cout << 0;
    return 0;
}