/*
    Ex6:    So thuan nguyen to: so nguyen to, cac chu so va tong cac chu so deu nguyen to
            in cac so thuan nguyen to trong khoang [a, b]
            1 <= a,b < 1e9
    Status: acp
*/
#include<iostream>
#include<string>

using namespace std;

bool isPrime(long long n)
{
    for(long long i = 2; i*i <=n;i++)
    {
        if(n%i == 0) return false;
    }
    return n >= 2;
}

bool check(long long n)
{
    long long sum = 0;
    while(n > 0)
    {
        long long temp = n%10;
        if (temp != 3 && temp != 5 && temp != 7 && temp != 2)
        return false;
        n = n/10;
        sum = sum + temp;
    }
    return isPrime(sum);
}

int main()
{
    long long a, b;
    cin >> a >> b;
    int cnt = 0;
    for(long long i = a; i <=b; i++)
    {
        if (check(i) && isPrime(i))
            cnt = cnt + 1;
    }
    cout << cnt;
}