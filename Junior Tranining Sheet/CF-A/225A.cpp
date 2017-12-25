#include <iostream>
using namespace std;

int main() {
	int n, top;
	cin >> n >> top;
	int bottom = 7 - top;
	while (n--) {
		int x, y;
		cin >> x >> y;
		int xop = 7 -x, yop = 7 - y;
		int top = 0;
		for (int i = 1; i <= 6; i++) {
			if (i != x && i!= y && i!= xop && i != yop) top = i;
		}
		if (top == bottom || (7 - top) == bottom) {
			if (top == bottom ) bottom = top;
			else bottom = 7 - top;
		} else {
			cout << "NO";
			return 0;
		}
	}
	cout << "YES";
	return 0;
}