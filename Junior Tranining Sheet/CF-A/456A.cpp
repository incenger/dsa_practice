#include <iostream>
using namespace std;

int main() {
	int n;
	cin >> n;
	int price[n], qual[n];
	bool alex = false;
	for (int i = 0; i < n; i++) {
		cin >> price[i] >> qual[i];
	}
	for (int i = 0; i < n; i++) {
		if (price[i] != qual[i]) alex= true;
	}
	if (alex) cout << "Happy Alex";
	else cout << "Poor Alex";
	return 0;
}