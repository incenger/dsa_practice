#include <stdio.h>
#include <iostream>
#include <bits/stdc++.h>
#include <stdlib.h>
using namespace std;

int v[9][9];

int moveX[8] = {-1, -2, -2, -1, 1, 2, 2, 1};
int moveY[8] = {2, 1, -1, -2, -2, -1, 1, 2};

bool validMove(int a, int b) {
	return (0 < a && a < 9) && (0 < b && b< 9);
}

int sol(int a, int b, int finalA, int finalB) {
	pair<int, int> init{a, b};
	queue< pair<int, int> > q;
	q.push(init);
	v[a][b] = 0;
	while(!q.empty()) {
		pair<int, int> current = q.front();
		q.pop();
		if (current.first == finalA && current.second == finalB) return v[finalA][finalB];
		for (int i = 0; i < 8; i++) {
			int nextX = current.first + moveX[i];
			int nextY = current.second + moveY[i];
			if (validMove(nextX, nextY)) {
				if (v[nextX][nextY] == 0) {
					v[nextX][nextY] = v[current.first][current.second] + 1;
					q.push(pair<int, int>{nextX, nextY});
				}
			}
		}
	}
}

int main() {
	string cell1, cell2;
	while (cin >> cell1 >> cell2) {
		memset(v, 0, sizeof(v[0])*9*9);
		int startY = cell1[0] - 'a' +1;
		int finalY = cell2[0] - 'a' +1;
		int startX = cell1[1] - '0';
		int finalX = cell2[1] - '0';
		cout <<"To get from " << cell1 << " to " <<  cell2 << " takes " << sol(startX, startY, finalX, finalY) << " knight moves.\n";
	}
	return 0;
}