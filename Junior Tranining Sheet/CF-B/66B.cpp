#include <iostream>
using namespace std;

int main() {
	int n;
	cin >> n;
	int a[1000];
	int maxc = 0;
	for (int i = 0; i < n; i++) cin >> a[i];
	for (int i = 0; i < n; i++) {
		int c = 1;
		int index = i -1;
		while(index >= 0 && a[index] <= a[index + 1]) {
			index--;
			c++;
		}
		index = i + 1;
		while(index < n && a[index] <= a[index -1]) {
			index++;
			c++;
		}
		if (c > maxc) maxc = c;
	}
	cout << maxc;
	return 0;
}