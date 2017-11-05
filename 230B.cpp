#include <iostream>
using namespace std;

const long long MAX = 1000000000000;

void fillArray(bool a[]);

int main() {
	bool a[MAX+1] = {true};
	fillArray(a);
	int n;
	cin >> n;
	for (int i = 0; i < n; i++) {
		long long x;
		cin >> x;
		}
		if (a[x] == true) {
			cout << "YES" <<endl;
		} else {
			cout << "NO" <<endl;
		}
		
	}
	return 0;
}

void fillArray(bool a[]) {
	a[1] = false;
	for (int i = 2; i * i <= MAX; i++) {
		if (a[i] == true) {
			for (int j = i*2; j <= MAX; j+= i) {
				if (i*i !=j) {
					a[j] = false;
				}
				
			}
		}
	}
}