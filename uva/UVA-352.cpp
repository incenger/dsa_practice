#include <iostream>
#include <vector>
#include <stack>

using namespace std;

char a[25][25];
int n;


int countWE(int i, int j) {
    if (i < 0 || i >= n) return 0;
    if (j < 0 || j >= n) return 0;
    if (a[i][j] == '0')    return 0;
    a[i][j] = '0';
    return 1 + countWE(i+ 1, j) + countWE(i+ 1, j -1) + countWE(i+ 1, j + 1) + countWE(i, j-1)
             + countWE(i, j+1)  + countWE(i - 1, j) + countWE(i -1 , j+1) + countWE(i - 1, j -1);
}

int main()
{
    int index  = 1;
    while (cin >> n) {
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                cin >> a[i][j];
            }
        }
        vector<char> v;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j ++) {
                if (a[i][j] == '1')
                    v.push_back(countWE(i, j));
            }
        }
        cout << "Image number " << index++ <<" contains " << v.size() << " war eagles." << endl;
    }
}
