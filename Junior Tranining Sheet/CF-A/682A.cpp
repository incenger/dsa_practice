#include <iostream>
using namespace std;

int main() {
	int n, m;
	cin >> n >> m;
	unsigned long long pairs = 0;
	for (int i = 1; i <= n; i++) {
		int r = 5 - (i%5);
		if (m < r) pairs += 0;
		else pairs += (m -r)/5 + 1;
	}
	cout << pairs << endl;
	return 0;
}