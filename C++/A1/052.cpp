#include <iostream>
#include <stdio.h>
using namespace std;
int main(){
    int A,Temp;
    cin >> A;
    if(A>=100 && A<=20000 && A%100==0){
        if(A/1000!=0){
            printf("1000 = %d\n",A/1000);
        }if(A%1000/500!=0){
            printf("500 = %d\n",A%1000/500);
        }
        if(A%1000%500/100!=0){
            printf("100 = %d\n",A%1000%500/100);
        }
    }else{
        cout << "ERROR";
    }
}