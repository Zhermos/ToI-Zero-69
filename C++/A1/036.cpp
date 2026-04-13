#include <iostream>
#include <stdio.h>
using namespace std;
int main(){
    int A;
    cin >> A;
    for(int i=A;i>=0;i--){
        if(i%10==0)printf("%d ",i);
    }
}