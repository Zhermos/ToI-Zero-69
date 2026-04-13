#include <iostream>
#include <stdio.h>
using namespace std;
int main() {
    int m, d;
    cin >> m >> d;
    if ((m == 12 && d >= 21) || (m == 1) || (m == 2) || (m == 3 && d < 21))printf("winter\n");
    else if ((m == 3 && d >= 21) || (m == 4) || (m == 5) || (m == 6 && d < 21)) printf("spring\n");
    else if ((m == 6 && d >= 21) || (m == 7) || (m == 8) || (m == 9 && d < 21)) printf("summer\n");
    else printf("fall\n");
}