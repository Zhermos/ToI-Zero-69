#include <iostream>
using namespace std;
int main(){
    int A,sum=0;
    cin >> A;
    if(A<=1)sum = 35;
    else if(A<=10)sum += 35+(5*(A-1));
    else sum += 35+45+(8*(A-10));
    cout << sum;
}