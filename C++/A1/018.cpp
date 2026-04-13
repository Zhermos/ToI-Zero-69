#include <iostream>
using namespace std;
int main(){
    int num;
    cin >> num;
    if(num < 0)cout << "Error : Please input positive number";
    else if(num == 0 || num >= 10)cout << "Error : Out of range";
    else{
        switch(num) {
            case 1: cout << "I"; break;
            case 2: cout << "II"; break;
            case 3: cout << "III"; break;
            case 4: cout << "IV"; break;
            case 5: cout << "V"; break;
            case 6: cout << "VI"; break;
            case 7: cout << "VII"; break;
            case 8: cout << "VIII"; break;
            case 9: cout << "IX"; break;
        }
    }
    
}