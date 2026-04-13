#include <iostream>
using namespace std;
int main(){
    int A,B,C;
    cin >> A >> B >> C;
    if(A == B && B == C && A == C)cout << "all the same";
    else if(A == B || B == C || A == C)cout << "neither";
    else cout << "all different";
}
