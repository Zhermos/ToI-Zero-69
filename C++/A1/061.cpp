#include <iostream>
#include <cmath>
using namespace std;
int main(){
    int r,x,y,L;
    cin >> r >> x >> y;
    L = pow(x,2)+pow(y,2);
    cout << (pow(r,2)==L ? "ON" : (pow(r,2)> L ? "IN" : "OUT"));
}