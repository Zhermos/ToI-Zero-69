#include <iostream>
using namespace std;
int main(){ 
    string A;
    int times;
    cin >> A >> times;
    int len = A.length();
    for(int i=0;i<len;i++){
        cout << (char)((A[i]- 'a' +times)% 26 + 'a');
    }
}