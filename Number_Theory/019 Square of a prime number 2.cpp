/*
    Ex19:   Square of a prime number 2 
            1 <= a,b <= 1e6
    Status: acp
*/
#include <iostream>
#include <cmath>
#include <algorithm>
#include<vector>
#define ll long long 
using namespace std ;

bool check(int n)
{
    for(int i = 2; i<=sqrt(n);i++)
    {
        int e = 0;
        while(n%i == 0)
        {
            e++;
            n/=i;
        }
        if(e == 1) return false;
    }
    return n <= 1;
}

int main()
{
    int a, b; cin >> a >> b;
    for (int i=a;i<=b;i++)
    {
        if(check(i)) cout << i<<" ";
    }
    return 0;
}