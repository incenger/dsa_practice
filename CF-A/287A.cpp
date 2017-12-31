#include <iostream>
using namespace std;

int main() {
	char a[4][4];
	for(int i = 0; i < 4; i++) {
		for (int j = 0; j < 4; j++) {
			cin >> a[i][j];
		}
		cin.get();
	}
	bool paint = false;
	for (int i = 0; i < 3; i++) {
		for (int j = 0; j < 3; j++) {
			int a1 = a[i][j], a2 = a[i][j+1], a3 = a[i+1][j], a4 = a[i+1][j+1];
			int dist = a1 + a2 + a3 + a4;
			if (dist == 151 || dist  == 173 || dist == 184 || dist == 140) paint = true;
		}
	}
	if(paint) cout << "YES";
	else cout << "NO";
	return 0;
}