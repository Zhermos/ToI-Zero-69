#include <iostream>
using namespace std;
int main(){
    string A;
    cin >> A;
    int len = A.length();
    for(int i=len-1;i>=0;i--)cout << (char)tolower(A[i]);
}