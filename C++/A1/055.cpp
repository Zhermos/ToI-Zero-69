#include <iostream>
using namespace std;
int main(){
    int A,B,C,sum=0;
    cin >> A >> B >> C;
    sum += A*25+B*40+C*55;
    // if(A+B+C >= 3)sum -= sum*10/100;
    cout << (A+B+C >= 3 ? sum*90/100 : sum);
}