#include <iostream>
using namespace std;
int main(){
    int A,B,C;
    cin >> A >> B >> C;
    cout << min(A,min(B,C));
}