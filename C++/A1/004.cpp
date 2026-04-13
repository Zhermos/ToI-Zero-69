#include <iostream>
#include <stdio.h>
using namespace std;
int main(){
    int A,B,C = 0;
    cin >> A >> B >> C;
    if(A >= 5 && B >= 20 && C >= 25){
        printf("pass");
    }else{
        printf("fail");
    }
}