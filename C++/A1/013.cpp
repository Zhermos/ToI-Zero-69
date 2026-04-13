#include <iostream>
using namespace std;
int main(){
    char A;
    int B;
    cin >> A >> B;
    switch (A)
    {
    case 'H':
        switch (B)
        {
        case 4567:
            cout << "safe unlocked";
            break;
        
        default:
            cout << "safe locked - change digit";
            break;
        }
        break;
    
    default:
        switch (B)
        {
        case 4567:
           cout << "safe locked - change char";
            break;
        
        default:
            cout << "safe locked";
            break;
        }
        break;
    }
}