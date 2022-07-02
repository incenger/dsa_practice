#include <iostream>
using namespace std;

bool isIncreasing (long long a[], int i1, int i2);
bool isDecreasing (long long a[], int i1, int i2);
long long maxElement(long long a[], int i1, int i2);
long long minElement(long long a[], int i1, int i2);


int main() {
	long long a[100000];
	int n;
	cin >> n;
	for (int i = 0; i < n; i++) {
		cin >> a[i];
	}
	if(isIncreasing(a, 0, n-1)) {
		cout << "yes" <<endl;
		cout << "1 1" <<endl;
		return 0;
	}
	
	int leftIndex, rightIndex;
	for (int i = 0; i < n-1; i++) {
		if (a[i] > a[i+1]) {
			leftIndex = i;
			break;
		}
	}
	for (int i = n-1; i > 0; i--) {
		if (a[i] < a[i-1]) {
			rightIndex = i;
			break;
		}
	}
	if(isDecreasing(a, leftIndex, rightIndex)) {
		long long min = minElement(a, leftIndex, rightIndex);
		long long max = maxElement(a, leftIndex, rightIndex);
		if ((leftIndex == 0 || min > a[leftIndex-1]) 
			&& (rightIndex == n-1 || max < a[rightIndex+1])) {
				cout << "yes" << endl;
				cout << leftIndex +1 <<" " <<rightIndex +1;
			}
		else {
			cout << "no";
		}
		
	} else {
		cout << "no";
	}
	return 0;
}


bool isIncreasing (long long a[], int i1, int i2) {
	for (int i = i1; i<i2; i++) {
		if (a[i] > a[i+1]) {
			return false;
		}
	}
	return true;
}

bool isDecreasing (long long a[], int i1, int i2) {
	for (int i = i1; i<i2; i++) {
		if (a[i] < a[i+1]) {
			return false;
		}
	}
	return true;
}

long long maxElement(long long a[], int i1, int i2) {
	long long max = a[i1];
	for (int i = i1; i<=i2; i++) {
		if (a[i] > max) {
			max = a[i];
		}
	}
	return max;
}
long long minElement(long long a[], int i1, int i2) {
	long long min = a[i1];
	for (int i = i1; i<=i2; i++) {
		if (a[i] < min) {
			min = a[i];
		}
	}
	return min;
}