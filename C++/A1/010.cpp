#include <iostream>
#include <stdio.h>
using namespace std;
int main(){
    int A;
    char B;
    cin >> A >> B;
    if(A < 18 || 's' == tolower(B))cout << 20;
    else cout << 50;
}