#include <iostream>
#include <algorithm>
using namespace std;



bool win(int a, int b) {
	if (a < b) swap(a, b);
	if (b == 0) return false;
	if (a / b == 1) return !win(a%b, b);
	return true;
	
}

int main() {
	int x, y;
	while (true) {
		cin >> x >> y;
		if (x == 0 && y ==0) break;
		if (!win(x, y)) cout << "Ollie wins" << endl;
		else cout << "Stan wins" << endl;
	}
	return 0;
}