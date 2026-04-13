#include <iostream>
#include <stdio.h>
using namespace std;
int main() {
    int A;
    float B = 0;
    cin >> A;
    float FT =  A * 0.5;
    if (A > 200) {
        B += (A - 200) * 15;
        A = 200; 
    }
    if (A > 100) {
        B += (A - 100) * 12;
        A = 100;
    }
    if (A > 50) {
        B += (A - 50) * 10;
        A = 50;
    }
    if (A > 10) {
        B += (A - 10) * 7;
        A = 10;
    }
    if (A > 0) {
        B += A * 5;
    }
    float VAT = B * 0.07;
    printf("%.2f",B+VAT+FT);
}