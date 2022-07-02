#include <iostream>
using namespace std;

int main() {
	int n, m;
	cin >> n >> m;
	char a[100][100];
	bool marked[26];
	char c;
	cin >> c;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m ; j++) {
			cin >> a[i][j];
		}
	}
	
	int res = 0;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m ; j++) {
			if (a[i][j] != '.' && a[i][j] != c) {
				if (i > 0 && a[i-1][j] == c) marked[a[i][j] - 'A'] =  true;
				if (i < n-1 && a[i+1][j] == c) marked[a[i][j] - 'A'] =  true;
				if (j > 0 && a[i][j-1] == c) marked[a[i][j] - 'A'] =  true;
				if (j < m-1 && a[i][j+1] == c) marked[a[i][j] - 'A'] =  true;
			}
		}
	}
	for (int i = 0; i < 26; i++) {
		if (marked[i]) res++;
	}
	cout << res;
	
	return 0;
}