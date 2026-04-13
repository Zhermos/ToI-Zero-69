#include <iostream>
using namespace std;
int main(){
    string A;
    int count=0;
    cin >> A;
    char check[] = {'a','e','i','o','u'};
    for(int i=0;i<A.length();i++){
        for(int j=0;j<5;j++){
            if(A[i] == check[j]){
                count++;
            }
        }
    }
    cout << count;
}