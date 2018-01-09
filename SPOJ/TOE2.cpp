#include <iostream>
using namespace std;

char a[3][3];

bool isFull()
{
	for (int i = 0; i < 3; i++)
		{
			for (int j = 0; j < 3; j++)
			{
				if (a[i][j] == '.') return false;
			}
		}
	return true;
}

bool win(char c)
{
	bool w = false;
	for (int i = 0 ; i < 3; i++) 
	{
		w = (a[i][0] == c) && (a[i][1] == c) && (a[i][2] == c);
		if (w) return true;
	}
	
	for (int i = 0 ; i < 3; i++) 
	{
		w = (a[0][i] == c) && (a[1][i] == c) && (a[2][i] == c);
		if (w) return true;
	}
	
	w = ((a[0][0] == c) && (a[1][1] == c) && (a[2][2] == c)) || ((a[2][0] == c) && (a[1][1] == c) && (a[0][2] == c));
	return w;
}

int main() 
{
	string s;
	
	while (true) 
	{
		cin >> s;
		if (s == "end") break;
		int x = 0, o = 0;
		for (int i = 0; i < 3; i++)
		{
			for (int j = 0; j < 3; j++)
			{
				a[i][j] = s[3*i + j];
				if (a[i][j] == 'X') x++;
				else if (a[i][j] == 'O') o++;
			}
		}
		if (win('X') && win('O')) cout << "invalid" << endl;
		else if (win('X'))
		{
			if (x == o + 1) cout << "valid" << endl;
			else cout << "invalid" << endl;
		}
		else if (win('O'))
		{
			if (o == x) cout << "valid" << endl;
			else cout << "invalid" << endl;
		} 
		else if (!win('X') && !win('O'))
		{
			if (x == 5 && o == 4) cout << "valid" << endl;
			else cout << "invalid" << endl;
		}
		else
		{
			cout << "invalid" << endl;
		}
	}		
	return 0;
}