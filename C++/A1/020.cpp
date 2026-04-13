#include <iostream>
using namespace std;
int main(){
    int A,B,C;
    cin >> A >> B >> C;
    if(A < B && B < C)cout << "increasing";
    else if(A > B && B > C)cout << "decreasing";
    else cout << "neither";
}
