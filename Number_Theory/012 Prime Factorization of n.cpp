/*
    Ex12:   Print Prime Factorization of n
            1 <= N <= 1e16
    Status: acp
*/
#include<iostream>
#include<string>

using namespace std;

void factorize(long long n)
{
    for(long long i = 2; i*i<=n;i++)
    {
        if(n%i==0)
        {
            int e = 0;
            while(n%i==0)
            {
                e++;
                n = n/i;
            }
            cout << i <<"^"<<e;
            if(n!=1)
            {
                cout <<" * ";
            }
        }
    }
    if(n > 1)
            cout << n <<"^1";
}

int main()
{
    long long n = 0;
    cin >> n;
    factorize(n);
    return 0;
}