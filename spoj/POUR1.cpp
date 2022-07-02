#include <iostream>
#include <bits/stdc++.h>

using namespace std;

int gcd(int a, int b)
{
	if (b == 0) return a;
	return gcd(b, a%b);
}

int sol(int a, int b, int c)
{
	int move = 1,  x = a, y = 0;
	while (x != c && y!=c)
	{
		int pour = min(x, b - y);
		x -= pour;
		y += pour;
		move++;
		if (x == c || y == c) break;
		if (x == 0) 
		{
			x = a;
			move++;
		}
		if (y == b)
		{
			y = 0;
			move++;
		}
 	}
 	return move;
}

int main() 
{
	int t;
	cin >> t;
	while(t--)
	{
		int a, b, c;
		cin >> a >> b >> c;
		if  (c > max(a, b) ) cout << "-1" << endl;
		else if (c % gcd(a, b) != 0) cout << "-1" << endl;
		else if (a == c || b == c) cout << "1" << endl;
		else cout << min(sol(a, b, c), sol(b, a, c)) << endl;
	}
	return 0;
}