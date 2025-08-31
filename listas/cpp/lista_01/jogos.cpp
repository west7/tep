#include <bits/stdc++.h>

using namespace std;

int main () {
    char res;
    int count = 0;
    for (auto i = 0; i < 6; ++i) {
        cin >> res;
        if (res == 'V') {
            count++;
        }
    }
    if (count > 4) {
        cout << 1 << '\n';
    } else if (count > 2) {
        cout << 2 << '\n';
    } else if (count > 0) {
        cout << 3 << '\n';
    } else {
        cout << -1 << '\n';
    }
    return 0;
}   