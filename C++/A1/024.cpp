#include <iostream>
using namespace std;
int main(){
    int A,B;
    cin >> A >> B;
    if(A<=1990){
        if(B<=1500)cout<<1250;
        else if(B>=1500&&B<=2000)cout<<1400;
        else if(B>=2000)cout<<2000;
    }else if(A>=1991 && A<=1999){
        if(B<=1500)cout<<1100;
        else if(B>=1500&&B<=2000)cout<<1300;
        else if(B>=2000)cout<<1700;
    }else if(A>=2000){
        if(B<=1500)cout<<1000;
        else if(B>=1500&&B<=2000)cout<<1200;
        else if(B>=2000)cout<<1500;
    }
}