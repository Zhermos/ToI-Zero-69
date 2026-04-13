#include <iostream>
using namespace std;
int main(){
    string A;
    cin >> A;
    int len = A.length();
    switch (toupper(A[0]))
    {
    case 'A':
        cout << "ace";
        break;
    case 'J':
        cout << "jack";
        break;
    case 'Q':
        cout << "queen";
        break;
    case 'K':
        cout << "king";
        break;
    default:
        cout << A[0];
        break;
    }
    if(len == 3)cout << A[1];
    cout << " of ";
    switch (toupper(A[len-1]))
    {
    case 'D':
        cout << "diamonds";
        break;
    case 'H':
        cout << "hearts";
        break;
    case 'S':
        cout << "spades";
        break;
    case 'C':
        cout << "clubs";
        break;
    default:
        break;
    }
    
}