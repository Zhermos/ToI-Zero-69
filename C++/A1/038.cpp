#include <iostream>
using namespace std;
int main(){
    int A;
    cin >> A;
    for(int i=1;i<=A;i++){
        if(i%5==0)cout << "X";
        else cout << "*";
    }
}