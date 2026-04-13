#include <iostream>
#include <stdio.h>

using namespace std;

int main() {
    int N; // จำนวนเครื่อง
    if (!(cin >> N)) return 0;

    for (int i = 0; i < N; i++) {
        double plastic, can, glass; // ใช้ชื่อตัวแปรให้ตรงประเภทขยะ
        cin >> plastic >> can >> glass;

        double total = plastic + can + glass;
        printf("%.1f", total); // แสดงผลทศนิยม 1 ตำแหน่ง

        if (total > 50.0) cout << ",Overloaded"; // เกิน 50 กก.
        if (plastic > 20.0) cout << ",Check Type Plastic"; // เกิน 20 กก.
        if (can > 20.0) cout << ",Check Type Can";
        if (glass > 20.0) cout << ",Check Type Glass";
        
        cout << "\n";
    }
    return 0;
}