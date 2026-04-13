#include <iostream>
#include <stdio.h>
using namespace std;
int main(){
    int A,M=0,W=0,Sum=0;
    while(cin >> A && A >= 0){
        if((A%10)%2==0)W++;
        else M++;
        Sum++;
    }printf("%d %d %d",M,W,Sum);
}