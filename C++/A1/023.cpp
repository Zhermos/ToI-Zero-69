#include <iostream>
using namespace std;
int main(){
    int A;
    char B;
    cin >> A >> B;
    
    if(toupper(B) == 'C'){
        if(A <= 0)cout << "solid";
        else if(A >= 100)cout << "gas";
        else cout << "liquid";
    }else if(toupper(B) == 'F')
        if(A <= 32)cout << "solid";
        else if(A >= 212)cout << "gas";
        else cout << "liquid";

}   