#include <iostream>
#include <stdio.h>
using namespace std;
int main(){
    int A,B;
    cin >> A >> B;
    if(A+B>=50)printf("%d\npass",A+B);
    else printf("%d\nfail",A+B);
}