#include <iostream>
using namespace std;
int main(){
    int A,score=0;
    char B;
    cin >> A;
    for(int i=0;i<A;i++){
        cin >> B;
        switch (B)
        {
        case '+':
            score += 10;
            break;
        case '-':
            score -= 5;
            break;
        default:
            break;
        }
    }
    cout << score;
}