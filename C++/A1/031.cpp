#include <iostream>
using namespace std;
int main(){
    string A;
    cin >> A;
    int len = A.length(),index = len-4;
    for(int i=0;i<len;i++){
        cout << A[i];
        if(index>=0 && i==index)cout << ",";
    }
}