#include <iostream>
#include <string>
using namespace std;

int main() {
	string s;
	int a[3] = {0};
	for (int i = 0; i < 3 ; i++) {
		cin >> s;
		if(s[1] == '>') a[s[0]- 'A']++;
		else a[s[2] - 'A']++;
	}
	int i = 0;
	if (a[0] == a[1] || a[0] == a[2] || a[1] == a[2]) cout << "Impossible";
	else {
		while (i < 3) {
		for (int j = 0; j < 3; j++) {
			if (a[j] == i) cout << (char) (j + 'A');
		}
		++i;
	}
		
	}
	
	return 0;
}