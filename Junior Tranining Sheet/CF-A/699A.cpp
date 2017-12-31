#include <iostream>

using namespace std;

int main() {
	char move[200000];
	int p[200000];
	int n;
	cin >> n;
	for (int i = 0; i < n; i++) {
		cin >> move[i];
	}
	for (int i = 0; i < n; i++) {
		cin >> p[i];
	}
	int collide = -1;
	for (int i = 0; i < n-1; i++) {
		if (move[i] == 'R' && move[i+1] == 'L') {
			int t = (p[i+1] - p[i])/2;
			if (collide == -1) collide = t;
			if (t < collide) collide =t;
		}
	}
	cout << collide;
	return 0;
}