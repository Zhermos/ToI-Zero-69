#include <iostream>
#include <stdio.h>
using namespace std;
int main(){
    int r1,g1,b1,r2,g2,b2;
    cin >> r1 >> g1 >> b1 >> r2 >> g2 >> b2;
    printf("%d %d %d",(r1+r2)/2,(g1+g2)/2,(b1+b2)/2);
}