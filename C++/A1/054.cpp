#include <iostream>
#include <iomanip>
using namespace std;

int main() {
    char A;
    long long B, C, bonus_base = 0;
    double percent = 0;
    if (!(cin >> A >> B >> C)) return 0;
    if (A == 'M') bonus_base = 1500;
    else if (A == 'B') bonus_base = 1000;
    else if (A == 'G') bonus_base = 500;
    if (A == 'M') {
        if (B < 5) percent = 0.06;
        else if (B < 10) percent = 0.08;
        else percent = 0.10;
    } 
    else if (A == 'B') {
        if (B < 5) percent = 0.05;
        else if (B < 10) percent = 0.06;
        else percent = 0.07;
    } 
    else if (A == 'G') {
        if (B < 5) percent = 0.04;
        else if (B < 10) percent = 0.05;
        else percent = 0.06;
    }
    long long total_bonus = bonus_base + (C * (percent * 100) / 100);
    cout << total_bonus << endl;
}