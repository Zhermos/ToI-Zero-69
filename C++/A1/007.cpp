#include <iostream>
#include <stdio.h>
using namespace std;
int main(){
    char A;
    cin >> A;
    switch (tolower(A)){
    case 'a':
    case 'e':
    case 'i':
    case 'o':
    case 'u':
        cout << "yes";
        break;
    
    default:
        cout << "no";
        break;
    }

}