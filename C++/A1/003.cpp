#include <iostream>
#include <stdio.h>
using namespace std;
int main(){
    int A,B,C = 0;
    cin >> A >> B >> C;
    printf("%d",max(A,max(B,C)));
}