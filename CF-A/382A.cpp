#include <iostream>
#include <string>
using namespace std;

int main() {
	string s;
	cin >>s;
	string letter;
	cin >> letter;
	int add = letter.length();
	int index = (int) s.find('|');
	string left, right;
	for (int i = 0; i < index; i++) left += s[i];
	for (int i = index +1; i < s.length(); i++) right += s[i];
	int l = left.length(), r = right.length(), i = 0;
	if ((l + r + add) % 2 == 1) cout << "Impossible";
	else {
		if (l > r) {
			while (r < l && add > 0) {
				right += letter[i];
				i++;
				r++;
				add--;
			}
			
			while(add > 0) {
				right +=letter[i];
				left += letter[i+1];
				i +=2;
				add -= 2;
			}
		} else {
			while (l < r && add > 0) {
				left += letter[i];
				i++;
				l++;
				add--;
			}
			while(add > 0) {
				right +=letter[i];
				left += letter[i+1];
				i +=2;
				add -= 2;
			}	
		}
		if (l != r) cout << "Impossible";
		else cout << left << "|" << right;
	}
	
	return 0;
}