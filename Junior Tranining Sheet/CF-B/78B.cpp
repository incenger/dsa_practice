#include <iostream>
using namespace std;

int main() {
	char color[] = {'R', 'O', 'Y', 'G', 'B', 'I', 'V'};
	int n;
	cin >> n;
	for (int i = 0; i < n; i++) {
		int q = n /7;
		if (n % 7 > 0 && n % 7 < 5 && i >= 7*q) cout << color[(i % 7) + 3];
		else cout << color[i%7];
	}
	return 0;
}