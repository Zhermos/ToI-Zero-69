#include <iostream>
#include <stdio.h>
using namespace std;
int main(){
    int A = 0;
    cin >> A;
    printf("10 = %d\n",A/10);
    printf("5 = %d\n",A%10/5);
    printf("2 = %d\n",A%10%5/2);
    printf("1 = %d\n",A%10%5%2/1);
}