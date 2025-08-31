#include <bits/stdc++.h>

int main () {
    int p1, p2, c1, c2;
    std::cin >> p1 >> c1 >> p2 >> c2;
    int l = p1 * c1;
    int r = p2 * c2;

    if (l > r) {
        std::cout << -1 << '\n';
    } else if ( l < r) {
        std::cout << 1 << '\n';
    } else {
        std::cout << 0 << '\n';
    }

    return 0;
}