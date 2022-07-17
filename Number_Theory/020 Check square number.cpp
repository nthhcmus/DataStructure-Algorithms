/*
    Ex20:   Check Square number (1<= N <= 1e18)
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
    for(ll i = 0; i*i<=n;i++)
    {
        if(i*i == n)
            return true;
    }
    return false;
}

int main()
{
    ll n; cin >> n;
    if(check(n)) cout << "YES";
    else cout << "NO";
    return 0;
}