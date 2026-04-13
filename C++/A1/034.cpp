#include <iostream>
using namespace std;
int main(){
    int A,B,mi;
    cin >> A;
    cin >> mi;
    if(A > 1){
        for(int i=0;i<A-1;i++){
            cin >> B;
            if(B < mi)mi = B;
        }
    }
    cout << mi;
}
