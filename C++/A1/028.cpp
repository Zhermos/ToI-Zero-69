#include <iostream>
using namespace std;
int main(){
    string A;
    cin >> A;
    int len = A.length();
    for(int i=len;i>=0;i--)cout << A[i];
}