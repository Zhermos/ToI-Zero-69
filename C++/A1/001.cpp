#include <iostream>
#include <stdio.h>
using namespace std;
int main(){
    char A[99],B[99];
    cin >> A >> B;
    printf("Hello %s %s \n",A,B);
    printf("%c%c%c%c",A[0],A[1],B[0],B[1]);
}