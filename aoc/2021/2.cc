#include <bits/stdc++.h>
#include <string>

using namespace std;

int SolvePartOne(const vector<pair<string, int>> &commands) {
    pair<int, int> pos{0, 0};

    for (auto &[direction, step] : commands) {
        if (direction == "forward") {
            pos = make_pair(pos.first, pos.second + step);
        } else if (direction == "up") {
            pos = make_pair(pos.first - step, pos.second);
        } else {
            pos = make_pair(pos.first + step, pos.second);
        }
    }

    return pos.first * pos.second;
}

long long SolvePartTwo(const vector<pair<string, int>> &commands) {
    pair<long long, long long> pos{0, 0};
    long long aim = 0;

    for (auto &[direction, step] : commands) {
        if (direction == "forward") {
            pos = make_pair(pos.first, pos.second + step);
            pos = make_pair(pos.first + aim * step, pos.second);
        } else if (direction == "up") {
            aim -= step;
        } else {
            aim += step;
        }
    }

    return pos.first * pos.second;
}

int main(int argc, char *argv[]) {
    string input_file = "input.txt";
    ifstream fin(input_file, ifstream::in);

    vector<pair<string, int>> commands;
    string direction;
    int step;
    while (fin >> direction >> step) {
        commands.emplace_back(direction, step);
    }

    cout << SolvePartOne(commands) << endl;
    cout << SolvePartTwo(commands) << endl;

    return 0;
}
