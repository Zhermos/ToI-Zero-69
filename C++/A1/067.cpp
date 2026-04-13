#include <iostream>
#include <stdio.h>
using namespace std;
int main(){
    char A;
    float B,sum=0;
    cin >> A >> B;
    for(int i=0;i<B;i++){
        float C;
        cin >> C;
        sum += C;
    }
    if(A=='Y')printf("%.2f",sum/100*95);
    else if(A=='N' && sum >= 500)printf("%.2f",sum/100*97);
    else printf("%.2f",sum);
}