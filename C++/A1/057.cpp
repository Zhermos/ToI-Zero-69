#include <iostream>
using namespace std;
int main(){
    int A,B;
    cin >> A >> B;
    if(A>6 || A<1 || B>6 || B<1)cout << "Invalid";
    else cout << (A == B ? "Correct!" : "Wrong!");
}