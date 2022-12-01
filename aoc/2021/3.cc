#include <bits/stdc++.h>
#include <fstream>
#include <string>

using namespace std;

long long SolvePartOne(const vector<string> &numbers) {
    int bit_length = numbers[0].length();
    vector<int> col_sum(bit_length, 0);

    for (auto &number : numbers) {
        for (int i = 0; i < (int)number.length(); i++) {
            auto c = number[i];
            if (c == '1') {
                col_sum[i] += 1;
            }
        }
    }
    vector<char> gamma_rate(bit_length, '0');
    vector<char> epsilon_rate(bit_length, '0');

    int threshold = (int)numbers.size() / 2;

    for (int i = 0; i < bit_length; i++) {
        if (col_sum[i] > threshold)
            gamma_rate[i] = '1';
        if (gamma_rate[i] == '0')
            epsilon_rate[i] = '1';
    }

    auto ToDecimal = [](const vector<char> &bits) {
        string bit_str(bits.begin(), bits.end());
        return stoi(bit_str, 0, 2);
    };
    return ToDecimal(gamma_rate) * ToDecimal(epsilon_rate);
}

long long SolvePartTwo(const vector<string> &numbers) {
    pair<int, int> oxy_range(0, (int)numbers.size() - 1);
    pair<int, int> co2_range(0, (int)numbers.size() - 1);

    int bit_length = numbers[0].length();
    int n = numbers.size();
    vector<vector<int>> bits(bit_length, vector<int>(n));

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < bit_length; j++) {
            bits[j][i] = (int)(numbers[i][j] - '0');
        }
    }

    auto selection = [](const vector<string> &numbers,
            const vector<int> &valid_idx, int col, bool oxy) {
        if (valid_idx.size() == 1)
            return valid_idx;

        vector<int> index_0, index_1;

        for (auto idx : valid_idx) {
            if (numbers[idx][col] == '1')
                index_1.push_back(idx);
            else
                index_0.push_back(idx);
        }
        int zero_count = index_0.size();
        int half = valid_idx.size() / 2;

        if (oxy) {
            if (zero_count <= half)
                return index_1;
            else
                return index_0;
        } else {
            if (zero_count <= half)
                return index_0;
            else
                return index_1;
        }
    };

    vector<int> oxy_idx, co2_idx;

    for (int i = 0; i < n; i++) {
        oxy_idx.push_back(i);
        co2_idx.push_back(i);
    }

    for (int i = 0; i < bit_length; i++) {
        oxy_idx = selection(numbers, oxy_idx, i, true);
        co2_idx = selection(numbers, co2_idx, i, false);
    }

    auto ToDecimal = [](const vector<char> &bits) {
        string bit_str(bits.begin(), bits.end());
        return stoi(bit_str, 0, 2);
    };

    vector<char> oxy_rating, co2_rating;

    for (int i = 0; i < bit_length; i++) {
        oxy_rating.push_back(numbers[oxy_idx[0]][i]);
        co2_rating.push_back(numbers[co2_idx[0]][i]);
    }

    return ToDecimal(oxy_rating) * ToDecimal(co2_rating);
}

int main(int argc, char *argv[]) {
    ifstream fin("input.txt", fstream::in);
    vector<string> numbers;
    string line;
    while (fin >> line) {
        numbers.push_back(line);
    }
    cout << SolvePartOne(numbers) << endl;
    cout << SolvePartTwo(numbers) << endl;

    return 0;
}
