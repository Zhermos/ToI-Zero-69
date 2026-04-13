#include <iostream>
#include <stdio.h>
using namespace std;
int main(){
    int A,B,C,sum=0;
    cin >> A >> B >> C;
    sum += A+B;
    if(C > 3)sum *= 1.5;printf("%d\n",sum);
    if(sum >= 1500){
        printf("5\n");
        if(C >= 7)printf("99");
        else printf("0");
    } 
    else if(sum >= 1000){
        printf("4\n");
        if(B >= 300)printf("88");
        else printf("0");
    }
    else if(sum >= 500)printf("3\n0");
    else if(sum >= 200)printf("2\n0");
    else if(sum < 200)printf("1\n0");



}