#include <iostream>
using namespace std;
int main(){
    int A;
    cin >> A;
    for(int i=0;i<A;i++)cout << "*";
    cout << "\n";
    for(int i=0;i<A-2;i++)cout << "*";
    cout << "\n";
    for(int i=0;i<A-4;i++)cout << "*";
}