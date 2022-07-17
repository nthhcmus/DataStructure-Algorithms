/*
    Ex27:   Check palindrome and >= factors
            1<=a,b<=1e7
    Status: acp
*/
#include <iostream>
#include <cmath>
#include <algorithm>
#include<vector>
#define ll long long 
using namespace std ;

bool check(ll n)
{
    int cnt = 0;
    for(ll i = 2; i*i<=n;i++)
    {
        if(n%i == 0)
        {
            while(n%i == 0)
            {
                n = n /i;
            }
            cnt++;
        }
        if(cnt == 3) return true;
    }
    if(n > 1) cnt++;
    return cnt >= 3;
}

bool checkPalindrome(ll n)
{
    ll res = 0;
    ll temp = n;
    while(temp > 0)
    {
        res = res*10 + (temp%10);
        temp /=10;
    }
    return res == n;
}

int main()
{
    ll a, b; cin >> a >> b;
    int flag = 0;
    for(ll i = a; i <= b; i++)
    {
        if(checkPalindrome(i) && check(i))
        {
            cout << i << ' ';
            flag = 1;
        }
    }
    if(flag == 0) cout << -1;
    return 0;
}