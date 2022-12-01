#include <bits/stdc++.h>
#include <fstream>
#include <iostream>
#include <string>

using namespace std;

int solve(const vector<int>& depths, int window_size) {
    int res = 0;

    for (int i = 0; i + window_size < (int) depths.size(); i++) {
        if (depths[i + window_size] - depths[i] > 0) res += 1;
    }

    return res;
}

int main (int argc, char *argv[])
{
    string input_file = "input.txt";
    ifstream fin(input_file, ifstream::in);
    vector<int> depths;

    for(string line; getline(fin, line); ) {
        int depth = stoi(line);
        depths.push_back(depth);
    }

    cout << solve(depths, 3);
    
    return 0;
}
