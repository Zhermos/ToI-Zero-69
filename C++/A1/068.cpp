#include <iostream>
#include <stdio.h>
using namespace std;
int main(){
    int A,B;
    float avg=0;
    bool check = true;
    cin >> A;
    for(int i=0;i<A;i++){
        cin >> B;
        if(B<=50)check = false;
        avg += B;
    }avg /= A;
    if(avg >= 60 && check) printf("%.1f\nPASS",avg);
    else printf("%.1f\nFAIL",avg);
}