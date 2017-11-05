#include <iostream>
using namespace std;

int main() {
	
	int n, m;
	cin >> n >> m;
	int task[1000000];
	for (int i = 0; i < m; i++) {
		cin >> task[i];
	}
	long long time = task[0] -1;
	for (int i = 0; i < m-1; i++) {
		if (task[i] <= task[i+1]) {
			time += task[i+1] - task[i];
		} else {
			time += task[i+1] - task[i] + n;
		}
	}
	cout << time;
	return 0;
}