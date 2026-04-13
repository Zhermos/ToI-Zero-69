#include <iostream>
using namespace std;
int main(){
    int A[5];
    for(int i=0;i<5;i++){
        cin >> A[i];
        if(A[i]==0){
            cout << "-";
        }
        else{
            if(A[i]/1000>0){
                A[i]=A[i]%1000;
                cout << "#";
            }
            if(A[i]/100>0){
                A[i]=A[i]%100;
                cout << "/";
            }
            if(A[i]/10>0){
                A[i]=A[i]%10;
                cout << "+";
            }
            if(A[i]>0){
                cout << "*";
            }
        }
        
    }

}