#include <iostream>
using namespace std;
int main(){
    int A,sum=1;
    cin >> A;
    for(int i=1;i<=A;i++){
        sum *= i;
    }
    cout << sum;
}